# Smart Aging: Enhancing Elderly Well-Being Through App-Based Activity Monitoring"

It has been assumed that a geriatric person is living alone in an apartment. Moreover, the room plan within the apartment is known beforehand. The problem in a single sentence is to build a low-cost solution for identifying the daily activities of the person in real time. The first challenge is to prepare a kit for sensing the presence of the concerned person in a specific location within the flat. The necessary ambient sensors and the strategic locations within the apartment need to be identified and the sensed data need to be properly stored within a server for subsequent analysis. The second challenge is to analyze the sensed data through machine learning and deep learning techniques for activity detection. 

## Demo
[![Demo](https://img.youtube.com/vi/W3peQtuGI2U/1.jpg)](https://www.youtube.com/watch?v=W3peQtuGI2U)

[Demo](https://youtu.be/W3peQtuGI2U) video.


# Building the project
In order to build the project, you will need following: 

1. Backend Server - Build with Django.
1. MQTT Server - It allow us to communicate data in realtime.between the server and the app. 
1. App - Build with Kotlin and Jetpack Compose.
1. Sensor Devices - Require for actual tracking the motions.


## Running the server 
```bash
pip install -r requirements.txt
```

Before, running backend server. You will need to change `MQTT_BROKER` in `settings.py` to match your MQTT IP.

```bash
python manage.py runserver 0.0.0.0
```

## Running the MQTT Server

You will need a MQTT Broker, Mosquitto is an open-source MQTT Broker. You can download from [here](https://mosquitto.org/download/).

Setting up `mosquitto.conf`
```bash
listener 1883 0.0.0.0
allow_anonymous true
```

Running the MQTT Server

```bash
mosquitto -c .\mosquitto.conf -v
```

## Build the app
Similiarly before building the app, you will need the MQTT Broker host and Server Url in the app. 

Change these variables in `AppModule.kt` to the IOT Server IP
and MQTT Broker host

```kotlin
private const val BASE_URL = "http://192.168.1.9:8000/"
private const val MQTT_BROKER_HOST = "192.168.1.9"
```

## Configuring your arduino
You will need to change wifi ssid and password as well as the 
server url to match your server URL. 

Change these variables accordingly: 
```c
const char* ssid = "<wifi_name>";
const char* password = "<wifi_password>";
String URL = "http://192.168.1.9:8000/api/motion/";
```
