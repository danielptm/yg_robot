
from motor.controls import Controls as MotorControls
from servo.controls import Controls as ServoControls

def stop():
    controls.stop_motor()
    controls.join()

controls: MotorControls = None
servo = ServoControls(0)

prev = ''
char = ''
while char != 'c':
    controls = MotorControls()
    controls.stop()
    print("starting..")
    print("f:forward, b:backward, r:right, l:left,s:stop ... c:cancel program")
    print("prev: " + prev)
    print("char: " + char)
    char = input("Input: ")

    print("creating controls")
    if 'servo' not in char:
        controls = MotorControls(char)
        controls.start_motor()
    else:
        if char == 'servo_f':
            servo = ServoControls()
            servo.forward( 0)
        elif char == 'servo_full_r':
            servo = ServoControls()
            servo.full_right()
        elif char == 'servo_full_l':
            servo.full_left()
        elif char == 'servo_peek_l':
            servo.peek_left()
        elif char == 'servo_peek_r':
            servo.peek_right()
        elif char == 'servo_scan':
            servo.scan()
        elif char == 'servo_stop':
            servo.stop_scan()

    print("set prev to char")
    prev = char
    print("end of loops")

controls.stop()


