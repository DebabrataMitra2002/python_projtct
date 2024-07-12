import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .ai_model.one_people import OnePeopleActivity
from .ai_model.two_people import TwoPeopleActivity
from .models import Plugs, Motion

import paho.mqtt.publish as publish
from django.conf import settings

MQTT_BROKER_HOST = settings.MQTT_BROKER

# Create your views here.
def index(request):
    data = Plugs.get_average_activity()
    return JsonResponse(data, safe=False)


def avg_by_date(request):
    data = Plugs.get_average_activity_by_date()
    return JsonResponse(data, safe=False)


@csrf_exempt
def predict_two_people(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            TPA = TwoPeopleActivity()

            result = []
            for d in data:
                prediction = TPA.predict([d])
                result.append(list(prediction[0]))

            response = {
                "predictions": result
            }
            return JsonResponse(response, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


"""

"""


@csrf_exempt
def predict_one_people(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            OPA = OnePeopleActivity()

            result = []
            for d in data:
                prediction = OPA.predict([d])
                result.append(list(prediction))

            response = {
                "predictions": result
            }
            return JsonResponse(response, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


"""
Insert Motion Data API
----------------------

This API is used to insert motion data into the database. The data is sent as a POST request with the following parameters:

SensorId: The ID of the sensor
SensorStatus: The status of the sensor (0 or 1)

After inserting 10 data points, the data is processed using the preprocessing function.
It combines different sensor data to generate insights.
"""
counter = 0
MAX_DATA_POINTS = 10


@csrf_exempt
def insert_motion_data(request):
    if request.method == 'POST':
        try:
            # read sensorId and value from x-www-form-urlencoded
            sensor_id = request.POST.get('SensorId')
            sensor_status = request.POST.get('SensorStatus')

            # store sensor data in the database
            data = Motion.objects.create(
                sensor_id=sensor_id,
                sensor_status=sensor_status
            )

            global counter
            counter += 1

            response = {
                "message": "Data inserted successfully",
                "data": {
                    "timestamp": data.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "sensor_id": data.sensor_id,
                    "sensor_status": data.sensor_status
                }
            }

            print(response["data"])

            if counter == MAX_DATA_POINTS:
                print("Starting processing ...")
                preprocessing()
                counter = 0

            publish.single(topic="sensor_data", payload=f"{response["data"]}", hostname=MQTT_BROKER_HOST)
            return JsonResponse(response, safe=True)
        except Exception as e:
            counter = 0
            return JsonResponse({"error": str(e)}, status=400)


def preprocessing():
    print("Starting preprocessing in shared task ...")

    # get latest 10 motion data
    data = Motion.get_n_from_last(10)

    print("Data:", data)

    # process the data
    start_time = data[0].get('timestamp')
    end_time = data[-1].get('timestamp')

    sensor_info = {
        "start_time": start_time,
        "end_time": end_time
    }

    for d in data:
        print(
            f"Processing data: timestamp={d['timestamp']}, sensor_id={d['sensor_id']}, sensor_status={d['sensor_status']}"
        )

        # if d['sensor_id'] not in sensor_info:
        #     sensor_info[d.get("sensor_id")] = []
        #
        # sensor_info[d.get('sensor_id')].append(d["sensor_status"])

        if d['sensor_id'] not in sensor_info:
            sensor_info[d.get("sensor_id")] = 0
        sensor_info[d.get('sensor_id')] += d["sensor_status"]

    print("Sensor Info:", sensor_info)

    sensor_vales = []
    for key, value in sensor_info.items():
        if key == "start_time" or key == "end_time":
            continue
        sensor_vales.append(value)

    if len(sensor_vales) < 5:
        for _ in range(5 - len(sensor_vales)):
            sensor_vales.append(0)

    OPA = OnePeopleActivity()
    prediction = OPA.predict([sensor_vales[0:6]])
    print("Prediction:", prediction)

    # To start the MQTT server, run the following command:
    # mosquitto.exe -c .\mosquitto.conf -v
    #
    # mosquitto.conf file:
    # listener 1883 0.0.0.0
    # allow_anonymous true
    publish.single(topic="sensor_data", payload=f"{sensor_info=}, {prediction[0]}", hostname=MQTT_BROKER_HOST)
