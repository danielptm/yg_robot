
print("Starting user input mode...")
from motor.controls import Controls
controls = Controls()
controls.start()
char = ''
while char != 'c':
    print("f:forward, b:backward, r:right, l:left,s:stop ... c:cancel program")
    char = input("Input: ")
    controls.setChar(char)

controls.join()
controls.stop_motor()
controls.stop_thread()
