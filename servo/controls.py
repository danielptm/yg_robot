from numbers import Number

from adafruit_servokit import ServoKit
import time

class Control:
    servo = ServoKit(channels=16)

    angle = 110

    def forward(self, servo):
        self.angle = 110
        self.servo.servo[servo].angle = self.angle

    def right(self, servo: Number):
        # --- Standard Servo Control ---
        # Set servo 0 to 90 degrees
        self.angle = 0
        self.servo.servo[servo].angle = self.angle

    def left(self, servo: Number):
        for i in range(180):
            self.angle += 1
            time.sleep(0.1)
            if self.angle > 180:
                self.angle = 180
                break
            self.servo.servo[servo].angle = self.angle


    def right(self, servo: Number):
        for i in range(180):
            self.angle -= 1
            time.sleep(0.1)
            if self.angle < 0:
                self.angle = 0
                break
            self.servo.servo[servo].angle = self.angle
