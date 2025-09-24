
from adafruit_motorkit import MotorKit
import threading


class Controls:
    kit = MotorKit()
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
        else:
            self.keep_going = False
            self.stop_motor()

    def forward(self, duration: int):
        while self.keep_going:
            self.kit.motor1.throttle = -1
            self.kit.motor2.throttle = -1
            self.kit.motor3.throttle = 1
            self.kit.motor4.throttle = 1

    def backward(self, duration: int):
        while self.keep_going:
            self.kit.motor1.throttle = 0.65
            self.kit.motor2.throttle = 0.65
            self.kit.motor3.throttle = -0.65
            self.kit.motor4.throttle = -0.65

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





