
from motor.controls import Controls

def stop():
    controls.stop_motor()
    pub.unsubscribe(controls.listener, 'motor_topic')
    controls.join()



controls: Controls = None

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
    controls = Controls(char)
    print("set prev to char")
    prev = char
    print("end of loops")

controls.stop()


