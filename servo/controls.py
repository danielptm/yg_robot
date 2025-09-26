from numbers import Number

from adafruit_servokit import ServoKit
import time

class Control:
    servo = ServoKit(channels=16)

    def forward(self, servo):
        self.servo.servo[servo].angle = 90

    def right(self, servo: Number):
        # --- Standard Servo Control ---
        # Set servo 0 to 90 degrees
        self.servo.servo[servo].angle = 180

    def left(self, servo: Number):
        self.servo.servo[servo].angle = 0
