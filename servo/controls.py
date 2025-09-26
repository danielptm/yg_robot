from numbers import Number

from adafruit_servokit import ServoKit
import time

class Controls:

    def __init__(self, servo_index: Number):
        self.servo_index = servo_index
        self.kit = ServoKit(channels=16)
        self.forward()
        self.is_scanning = False
        self.scan_dir = 'r'

    def forward(self):
        self.angle = 110
        self.kit.servo[self.servo_index].angle = self.angle


    def full_left(self):
        for i in range(180):
            print(self.angle)
            self.angle += 2
            time.sleep(0.05)
            if self.angle > 178:
                self.angle = 178
                break
            self.kit.servo[self.servo_index].angle = self.angle

    def full_right(self):
        for i in range(180):
            print(self.angle)
            self.angle -= 2
            time.sleep(0.05)
            if self.angle < 0:
                self.angle = 0
                break
            self.kit.servo[self.servo_index].angle = self.angle

    def peek_right(self):
        self.angle = self.angle - 1
        self.kit.servo[self.servo_index].angle = self.angle

    def peek_left(self):
        self.angle = self.angle + 1
        self.kit.servo[self.servo_index].angle = self.angle

    def scan(self):
        self.is_scanning = True
        while self.is_scanning:
            time.sleep(0.025)
            if self.scan_dir == 'r' and self.is_scanning:
                if self.angle > 3:
                    self.scan_dir = 'r'
                    self.peek_right();
                else:
                    self.scan_dir = 'l'
            else:
                if self.is_scanning and self.angle <177:
                    self.scan_dir = 'l'
                    self.peek_left()
                else:
                    self.scan_dir = 'r'
    def stop_scan(self):
        self.is_scanning = False
        self.forward()
