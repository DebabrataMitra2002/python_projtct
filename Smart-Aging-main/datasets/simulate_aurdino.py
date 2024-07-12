import requests
import random
import time

sensor_ids = [ i for i in range(0, 5)]

if __name__ == "__main__":
    while True:
        sensor_id = random.choice(sensor_ids)
        sensor_status = random.choice([0, 1])
        response = requests.post("http://localhost:8000/api/motion/", data={"SensorId": sensor_id, "SensorStatus": sensor_status})
        print(response.json())
        time.sleep(0.2)