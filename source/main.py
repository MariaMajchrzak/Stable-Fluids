import keyboard

def loop():
    running = True
    while running:
        dt = 0.016
        print(dt)

        if keyboard.is_pressed('q'):
            running = False

loop()