
from adafruit_motorkit import MotorKit
import time
import threading


class Controls(threading.Thread):
    kit = MotorKit()

    def __init__(self):
        super().__init__()
        self.name = "motor"

    char = "s"
    keep_going = True

    def run(self):
        while self.keep_going:
            time.sleep(1/60)
            self.call()

    def stop_thread(self):
        self.keep_going = False

    def setChar(self, char):
        if (char != self.char):
            self.char = char

    def call(self):
        if self.char == 'f':
            self.forward(None)
        if self.char == 'b':
            self.backward(None)
        if self.char == 'r':
            self.hard_right_90()
        if self.char == "l":
            self.hard_left_90()
        if self.char == "sl":
            self.soft_left()
        if self.char == "sr":
            self.soft_right()
        else:
            self.stop_motor()

    def forward(self, duration: int):
        if duration is None:
            self.kit.motor1.throttle = -1
            self.kit.motor2.throttle = -1
        else:
            self.kit.motor1.throttle = -1
            self.kit.motor2.throttle = -1

    def backward(self, duration: int):
        if duration is None:
            self.kit.motor1.throttle = 1
            self.kit.motor2.throttle = 1
        else:
            self.kit.motor1.throttle = 1
            self.kit.motor2.throttle = 1

    def stop_motor(self):
        self.kit.motor1.throttle = 0
        self.kit.motor2.throttle = 0

    def hard_right_90(self):
        self.kit.motor1.throttle = 1
        self.kit.motor2.throttle = -1

    def hard_left_90(self):
        self.kit.motor1.throttle = -1
        self.kit.motor2.throttle = 1

    def soft_right(self):
        self.kit.motor1.throttle = 0.5
        self.kit.motor2.throttle = -0.75


    def soft_left(self):
        self.kit.motor1.throttle = -0.75
        self.kit.motor2.throttle = 0.5



