import argparse
import time
import threading
import cv2
import numpy as np
from dronekit import connect, VehicleMode, mavutil
from gpiozero import DistanceSensor
from picamera2 import Picamera2

# Command line argument for connection
parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='127.0.0.1:14550', help='Connection string to the vehicle')
args = parser.parse_args()

# GPIO Sensor Setup
SENSORS = {
    'front': DistanceSensor(echo=27, trigger=17, max_distance=4),
    'left': DistanceSensor(echo=23, trigger=22, max_distance=4),
    'right': DistanceSensor(echo=6, trigger=5, max_distance=4),
    'back': DistanceSensor(echo=26, trigger=19, max_distance=4)
}

# Movement mapping (With Acceleration Integration)
MOVEMENT = {
    'front': (-1, 0, 0, -0.5, 0, 0),
    'back': (1, 0, 0, 0.5, 0, 0),
    'left': (0, 1, 0, 0, 0.5, 0),
    'right': (0, -1, 0, 0, -0.5, 0),
    'up': (0, 0, -1, 0, 0, -0.5),
    'down': (0, 0, 1, 0, 0, 0.5)
}

# Initialize Pi Camera
camera = Picamera2()
camera_config = camera.create_preview_configuration(main={"size": (640, 480)})
camera.configure(camera_config)
camera.start()

def measure_distance(sensor):
    try:
        distance = round(sensor.distance * 100, 2)
        return distance if distance <= 400 else 999
    except Exception as e:
        return 999

def send_velocity(vehicle, vx, vy, vz, ax, ay, az, duration):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0, 0, 0, mavutil.mavlink.MAV_FRAME_BODY_NED,
        0b0000111111000111,
        0, 0, 0, vx, vy, vz, ax, ay, az, 0, 0
    )
    for _ in range(duration * 10):
        vehicle.send_mavlink(msg)
        time.sleep(0.02)

def check_landing_zone():
    frame = camera.capture_array()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) > 0: 
        return False  # Obstacle detected
    return True  # Safe Landing Zone


class DroneObstacleAvoidance:

    def __init__(self, connection_string):
        self.vehicle = connect(connection_string, baud=921600, wait_ready=True)
        self.obstacle_distance = 200
        self.obstacle_thread = threading.Thread(target=self.obstacle_avoidance_system, daemon=True)
        self.obstacle_thread.start()

    def obstacle_avoidance_system(self):
        while True:
            distances = {dir: measure_distance(sensor) for dir, sensor in SENSORS.items()}
            obstacles = {dir: dist < self.obstacle_distance for dir, dist in distances.items()}

            if all(obstacles.values()):
                self.ensure_guided_mode()
                self.move_drone('up')
                print("Obstacle in all directions. Moving Upward.")
            else:
                for direction, detected in obstacles.items():
                    if detected:
                        self.ensure_guided_mode()
                        self.move_drone(direction)
                        break

            time.sleep(0.1)

    def move_drone(self, direction):
        args = MOVEMENT.get(direction, (0, 0, 0, 0, 0, 0))
        send_velocity(self.vehicle, *args, duration=1)

    def auto_landing(self):
        print("Initiating Auto-Landing...")

        while True:
            safe_to_land = check_landing_zone()
            if safe_to_land:
                self.vehicle.mode = VehicleMode("LAND")
                print("Landing Zone is Clear ✅. Drone Landing Successfully!")
                break
            else:
                print("Obstacle Detected! Holding Position...")
                send_velocity(self.vehicle, 0, 0, 0, 0, 0, 0, duration=1)
                time.sleep(1)

    def ensure_guided_mode(self):
        if self.vehicle.mode != VehicleMode("GUIDED"):
            self.vehicle.mode = VehicleMode("GUIDED")
            while self.vehicle.mode != VehicleMode("GUIDED"):
                time.sleep(0.1)

    def close(self):
        self.vehicle.close()


if __name__ == '__main__':
    drone_control = DroneObstacleAvoidance(args.connect)

    try:
        while True:
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Auto Landing Activated...🚀")
        drone_control.auto_landing()
        drone_control.close()
