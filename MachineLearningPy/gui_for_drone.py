import tkinter as tk
from tkinter import Label
import threading
import time
import random

# Dummy distance data for simulation
def get_distance(sensor):
    return random.randint(50, 300)

class DroneControlGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Drone Obstacle Avoidance GUI")
        self.root.geometry("600x400")
        
        # Heading
        self.heading = Label(root, text="Drone Obstacle Avoidance System", font=("Helvetica", 16))
        self.heading.pack(pady=10)

        # Distance Labels
        self.front_label = Label(root, text="Front Distance: 0 cm", font=("Helvetica", 14))
        self.front_label.pack(pady=5)

        self.back_label = Label(root, text="Back Distance: 0 cm", font=("Helvetica", 14))
        self.back_label.pack(pady=5)

        self.left_label = Label(root, text="Left Distance: 0 cm", font=("Helvetica", 14))
        self.left_label.pack(pady=5)

        self.right_label = Label(root, text="Right Distance: 0 cm", font=("Helvetica", 14))
        self.right_label.pack(pady=5)

        self.status_label = Label(root, text="Drone Status: Stable", font=("Helvetica", 14), fg="green")
        self.status_label.pack(pady=20)

        # Start Obstacle Avoidance Thread
        self.update_sensor_thread = threading.Thread(target=self.update_sensor_data)
        self.update_sensor_thread.daemon = True
        self.update_sensor_thread.start()

    def update_sensor_data(self):
        while True:
            front_distance = get_distance("front")
            back_distance = get_distance("back")
            left_distance = get_distance("left")
            right_distance = get_distance("right")

            self.front_label.config(text=f"Front Distance: {front_distance} cm")
            self.back_label.config(text=f"Back Distance: {back_distance} cm")
            self.left_label.config(text=f"Left Distance: {left_distance} cm")
            self.right_label.config(text=f"Right Distance: {right_distance} cm")

            # Obstacle Avoidance Logic
            if front_distance < 100:
                self.status_label.config(text="Obstacle Ahead - Moving Backward!", fg="red")
            elif back_distance < 100:
                self.status_label.config(text="Obstacle Behind - Moving Forward!", fg="red")
            elif left_distance < 100:
                self.status_label.config(text="Obstacle on Left - Moving Right!", fg="red")
            elif right_distance < 100:
                self.status_label.config(text="Obstacle on Right - Moving Left!", fg="red")
            else:
                self.status_label.config(text="Drone Status: Stable", fg="green")

            time.sleep(0.5)

if __name__ == "__main__":
    root = tk.Tk()
    app = DroneControlGUI(root)
    root.mainloop()



import argparse
import time
import threading
from dronekit import connect, VehicleMode, mavutil
from gpiozero import DistanceSensor

# Add argparse to parse command-line arguments for vehicle connection
parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='127.0.0.1:14550', help='Connection string to the vehicle')
args = parser.parse_args()

# GPIO setup for HC-SR04 on multiple directions (front, back, left, right)
SENSORS = {
    'front': DistanceSensor(echo=27, trigger=17, max_distance=4),
    'left': DistanceSensor(echo=23, trigger=22, max_distance=4),
    'right': DistanceSensor(echo=6, trigger=5, max_distance=4),
    'back': DistanceSensor(echo=26, trigger=19, max_distance=4)
}

# Movement mapping
MOVEMENT = {
    'front': (-1, 0, 0, -0.5, 0, 0),
    'back': (1, 0, 0, 0.5, 0, 0),
    'left': (0, 1, 0, 0, 0.5, 0),
    'right': (0, -1, 0, 0, -0.5, 0),
    'up': (0, 0, -1, 0, 0, -0.5)
}


def measure_distance(sensor):
    try:
        distance = round(sensor.distance * 100, 2)
        return distance if distance <= 400 else 999
    except Exception as e:
        print(f"Sensor error: {e}")
        return 999


def send_velocity(vehicle, velocity_x, velocity_y, velocity_z, accel_x, accel_y, accel_z, duration):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0, 0, 0,
        mavutil.mavlink.MAV_FRAME_BODY_NED,
        0b0000111111000111,
        0, 0, 0,
        velocity_x, velocity_y, velocity_z,
        accel_x, accel_y, accel_z,
        0, 0
    )
    for _ in range(duration * 10):
        vehicle.send_mavlink(msg)
        time.sleep(0.02)


class DroneObstacleAvoidance:

    def __init__(self, connection_string):
        self.vehicle = connect(connection_string, baud=921600, wait_ready=True)
        self.obstacle_distance = 200
        self.obstacle_thread = threading.Thread(target=self.obstacle_avoidance_system, daemon=True)
        self.obstacle_thread.start()

    def obstacle_avoidance_system(self):
        while True:
            distances = {dir: measure_distance(sensor) for dir, sensor in SENSORS.items()}
            print(distances)

            obstacles = {dir: dist < self.obstacle_distance for dir, dist in distances.items()}

            if all(obstacles.values()):
                self.ensure_guided_mode()
                self.move_drone('up')
                print("Obstacle in all directions. Ascending.")
            else:
                for direction, detected in obstacles.items():
                    if detected:
                        self.ensure_guided_mode()
                        self.move_drone(direction)
                        print(f"Obstacle detected {direction}. Moving away.")
                        break

            time.sleep(0.1)

    def move_drone(self, direction):
        args = MOVEMENT.get(direction, (0, 0, 0, 0, 0, 0))
        send_velocity(self.vehicle, *args, duration=1)

    def ensure_guided_mode(self):
        if self.vehicle.mode != VehicleMode("GUIDED"):
            print("Switching to GUIDED mode")
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
        print("Exiting...")
        drone_control.close()
