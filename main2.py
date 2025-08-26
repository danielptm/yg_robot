
from motor.controls import Controls
from pubsub import pub

print("Starting user input mode...")


char = ''
while char != 'c':
    print("f:forward, b:backward, r:right, l:left,s:stop ... c:cancel program")
    char = input("Input: ")
    controls = Controls()
    if controls.is_alive():
        controls.join()
    controls.start()
    pub.subscribe(controls.listener, "motor_topic")
    pub.sendMessage("motor_topic", arg1=char, arg2=None)

controls.stop_motor()
pub.unsubscribe(controls.listener, 'motor_topic')

