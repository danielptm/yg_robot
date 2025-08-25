import time
from adafruit_motorkit import MotorKit

# Create a MotorKit object
# By default, it uses the I2C address 0x60
kit = MotorKit()

# Control motor 1 (connected to M1 terminals)
#kit.motor1.throttle = 0.5  # Set speed to full forward (0.0 for stop, -1.0 for full backward)
kit.motor1.throttle = -1
kit.motor2.throttle = 0
time.sleep(2)            # Run for 0.5 seconds
#kit.motor1.throttle = 0.0  # Stop the motor
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0