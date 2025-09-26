
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
    if 'servo' not in char:
        controls = MotorControls(char)
        controls.start_motor()
    else:
        if char == 'servo_f':
            servo = ServoControls()
            servo.forward( 0)
        elif char == 'servo_r':
            servo = ServoControls()
            servo.right(0)
        elif char == 'servo_l':
            servo = ServoControls()
            servo.left(0)

    print("set prev to char")
    prev = char
    print("end of loops")

controls.stop()


