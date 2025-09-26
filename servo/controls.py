from numbers import Number

from adafruit_servokit import ServoKit
import time

class Control:
    servo = ServoKit(channels=16)

    def right(self, degrees: Number, servo: Number):
        # --- Standard Servo Control ---
        # Set servo 0 to 90 degrees
        for i in range(degrees):
            self.servo.servo[servo].angle = i
            time.sleep(0.025)  # Wait for 2 seconds