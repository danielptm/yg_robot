
from adafruit_motorkit import MotorKit
import time
import threading


class Controls:
    kit = MotorKit()
    thread = None
    keep_going = True
    def __init__(self):
        self.name = "motor"

    def listener(self, data):
        self.thread = threading.Thread(target=self.call, args=data)
        self.thread.start()

    def stop(self):
        self.keep_going = False
        if self.thread is not None:
            self.thread.join()


    def call(self, char):
        if char == 'f':
            self.forward(None)
        if char == 'b':
            self.backward(None)
        if char == 'r':
            self.hard_right_90()
        if char == "l":
            self.hard_left_90()
        if char == "sl":
            self.soft_left()
        if char == "sr":
            self.soft_right()
        else:
            self.keep_going = False
            self.stop_motor()

    def forward(self, duration: int):
        while self.keep_going:
            self.kit.motor1.throttle = -1
            self.kit.motor2.throttle = -1

    def backward(self, duration: int):
        if duration is None:
            self.kit.motor1.throttle = 1
            self.kit.motor2.throttle = 1
        else:
            self.kit.motor1.throttle = 1
            self.kit.motor2.throttle = 1
        time.sleep(1000)

    def stop_motor(self):
        self.kit.motor1.throttle = 0
        self.kit.motor2.throttle = 0
        time.sleep(1000)

    def hard_right_90(self):
        self.kit.motor1.throttle = 1
        self.kit.motor2.throttle = -1
        time.sleep(1000)

    def hard_left_90(self):
        self.kit.motor1.throttle = -1
        self.kit.motor2.throttle = 1
        time.sleep(1000)

    def soft_right(self):
        self.kit.motor1.throttle = 0.5
        self.kit.motor2.throttle = -0.75
        time.sleep(1000)

    def soft_left(self):
        self.kit.motor1.throttle = -0.75
        self.kit.motor2.throttle = 0.5
        time.sleep(1000)


