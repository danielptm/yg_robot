from main import controls
from motor.controls import Controls

print("Starting user input mode...")
from motor.controls import Controls
controls = Controls()
char = ''
char = input("f:forward, b:backward, r:right, l:left,s:stop ... c:cancel program")
while char != 'c':
    char = input("f:forward, b:backward, r:right, l:left,s:stop ... c:cancel program")
    if char == 'f':
        controls.forward()
    if char == 'b':
        controls.backward()
    if char == 'r':
        controls.hard_right_90()
    if char == "l":
        controls.hard_left_90()
    else:
        controls.stop()

controls.stop()
