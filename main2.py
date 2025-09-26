
from motor.controls import Controls as MotorControls
from servo.controls import Control as ServoControls

def stop():
    controls.stop_motor()
    controls.join()

controls: MotorControls = None
servo: ServoControls = None

prev = ''
char = ''
while char != 'c':
    print("starting..")
    print("f:forward, b:backward, r:right, l:left,s:stop ... c:cancel program")
    print("prev: " + prev)
    print("char: " + char)
    char = input("Input: ")

    if controls is not None:
        print("stopping")
        controls.stop()
    print("creating controls")
    if char != 'sr' or char != "sl":
        controls = MotorControls(char)
        controls.start_motor()
    elif char == 'sr':
        servo = ServoControls()
        servo.right(180, 0)
    elif char == 'sl':
        servo = ServoControls()
        servo.right(180, 0)

    print("set prev to char")
    prev = char
    print("end of loops")

controls.stop()


