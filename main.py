import time
from adafruit_motorkit import MotorKit
from motor.controls import Controls

controls = Controls()

controls.forward(None)
controls.stop()
controls.backward(None)
controls.stop()
controls.hard_right_90()
controls.stop()
controls.hard_left_90()
