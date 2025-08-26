
from motor.controls import Controls
from pubsub import pub

print("Starting user input mode...")

controls: Controls = None

prev = 'prev'
while char != 'c':
    print("f:forward, b:backward, r:right, l:left,s:stop ... c:cancel program")
    char = input("Input: ")
    if char != prev:
        if controls is not None:
            if controls.is_alive():
                controls.join()
    controls = Controls()
    controls.start()
    pub.subscribe(controls.listener, "motor_topic")
    pub.sendMessage("motor_topic", arg1=char, arg2=None)
    prev = char

controls.stop_motor()
pub.unsubscribe(controls.listener, 'motor_topic')

