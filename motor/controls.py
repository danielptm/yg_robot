
from adafruit_motorkit import MotorKit
import time
import threading
from pubsub import pub


class Controls(threading.Thread):
    kit = MotorKit()

    def __init__(self):
        threading.Thread.__init__(self)
        self.name = "motor"

    def listener(self, arg1, arg2):
        self.call(arg1)

    def pub(self, arg1):
        print("subscribing")
        pub.subscribe(self.listener, "motor_topic")
        print("send message")
        pub.sendMessage("motor_topic", arg1=arg1, arg2=None)

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
            self.stop_motor()

    def forward(self, duration: int):
        if duration is None:
            self.kit.motor1.throttle = -1
            self.kit.motor2.throttle = -1
        else:
            self.kit.motor1.throttle = -1
            self.kit.motor2.throttle = -1
        time.sleep(1000)

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


