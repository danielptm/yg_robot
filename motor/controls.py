from adafruit_motorkit import MotorKit
import time

class Controls:
    kit = MotorKit()

    def __init__(self):
        pass

    def forward(self, duration: int):
        if duration is None:
            self.kit.motor1.throttle = -1
            self.kit.motor2.throttle = -1
            time.sleep(1.5)
        else:
            self.kit.motor1.throttle = -1
            self.kit.motor2.throttle = -1
            time.sleep(duration)

    def backward(self, duration: int):
        if duration is None:
            self.kit.motor1.throttle = 1
            self.kit.motor2.throttle = 1
            time.sleep(1.5)
        else:
            self.kit.motor1.throttle = 1
            self.kit.motor2.throttle = 1
            time.sleep(duration)

    def stop(self):
        self.kit.motor1.throttle = 0
        self.kit.motor2.throttle = 0
        time.sleep(1)

    def hard_right_90(self):
        self.kit.motor1.throttle = 1
        self.kit.motor2.throttle = -1
        time.sleep(1)

    def hard_left_90(self):
        self.kit.motor1.throttle = -1
        self.kit.motor2.throttle = 1
        time.sleep(1)

