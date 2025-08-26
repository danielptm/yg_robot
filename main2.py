from motor.controls import Controls

print("Starting user input mode...")
from motor.controls import Controls
controls = Controls()
char = ''
while char != 'c':
    print("f:forward, b:backward, r:right, l:left,s:stop ... c:cancel program")
    char = input("Input: ")
    if char == 'f':
        controls.forward(None)
    if char == 'b':
        controls.backward(None)
    if char == 'r':
        controls.hard_right_90()
    if char == "l":
        controls.hard_left_90()
    if char == "sl":
        controls.soft_left()
    if char == "sr":
        controls.soft_right()
    else:
        controls.stop()

controls.stop()
