import time
from adafruit_motorkit import MotorKit
from motor.controls import Controls

controls = Controls()

controls.forward()
controls.stop()
controls.backward()
controls.stop()
controls.hard_right_90()