
import time


from adafruit_motorkit import MotorKit
from adafruit_servokit import ServoKit

import threading


class Controls:
    kit = MotorKit()
    servo = ServoKit(channels=16)


    thread = None
    keep_going = True
    def __init__(self, char):
        self.name = "motor"
        self.char = char

    def start_motor(self):
        self.thread = threading.Thread(target=self.call, args=self.char)
        self.thread.start()

    def stop(self):
        self.keep_going = False


    def call(self, char):
        if char == 'f':
            self.forward(None)
        if char == 'b':
            self.backward(None)
        if char == 'r':
            self.right()
        if char == "l":
            self.left()
        if char == "u":
            self.up()
        else:
            self.keep_going = False
            self.stop_motor()

    def forward(self, duration: int):
        while self.keep_going:
            self.kit.motor1.throttle = -1
            self.kit.motor2.throttle = -1
            self.kit.motor3.throttle = -1
            self.kit.motor4.throttle = -1

    def backward(self, duration: int):
        while self.keep_going:
            self.kit.motor1.throttle = 0.65
            self.kit.motor2.throttle = 0.65
            self.kit.motor3.throttle = 0.65
            self.kit.motor4.throttle = 0.65

    def stop_motor(self):
        self.kit.motor1.throttle = 0
        self.kit.motor2.throttle = 0
        self.kit.motor3.throttle = 0
        self.kit.motor4.throttle = 0

    def right(self):
        while self.keep_going:
            self.kit.motor1.throttle = 0.65
            self.kit.motor2.throttle = -0.65
            self.kit.motor3.throttle = 0.65
            self.kit.motor2.throttle = -0.65

    def left(self):
        while self.keep_going:
            self.kit.motor1.throttle = -0.65
            self.kit.motor2.throttle = 0.65
            self.kit.motor3.throttle = -0.65
            self.kit.motor4.throttle = 0.65

    def up(self):
        self.servo = ServoKit(channels=16)

        # --- Standard Servo Control ---
        # Set servo 0 to 90 degrees
        print("Setting servo 0 to 90 degrees...")
        self.servo.servo[0].angle = 90
        time.sleep(2)  # Wait for 2 seconds

        # Set servo 0 to 0 degrees
        print("Setting servo 0 to 0 degrees...")
        self.servo.servo[0].angle = 0
        time.sleep(2)  # Wait for 2 seconds

        print("Setting servo 0 to 90 degrees...")
        self.servo.servo[0].angle = 90
        time.sleep(2)  # Wait for 2 seconds

        # --- Continuous Rotation Servo Control ---
        # Set continuous servo 1 to full speed forward
        # print("Setting continuous servo 1 to full speed...")
        # self.servo.continuous_servo[1].throttle = 1.0
        # time.sleep(2)  # Run for 2 seconds
        #
        # # Set continuous servo 1 to full speed backward
        # print("Setting continuous servo 1 to full speed backward...")
        # self.servo.continuous_servo[1].throttle = -1.0
        # time.sleep(2)  # Run for 2 seconds
        #
        # # Stop continuous servo 1
        # print("Stopping continuous servo 1...")
        # self.servo.continuous_servo[1].throttle = 0.0






