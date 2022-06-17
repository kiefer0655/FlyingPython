import keyboard
ManualMotionPower = 50

def ManualControlControler(ManualControl):
    if keyboard.is_pressed('tab'):
        ManualControl = not ManualControl
    return ManualControl

def GetMotionByKeyboard():
    motion = [0,0,0,0]

    LR, FB, UD, Yaw = 0, 0, 0, 0

    if keyboard.is_pressed('a'):
        LR -= ManualMotionPower

    if keyboard.is_pressed('d'):
        LR += ManualMotionPower

    if keyboard.is_pressed('w'):
        FB += ManualMotionPower

    if keyboard.is_pressed('s'):
        FB -= ManualMotionPower

    if keyboard.is_pressed('up'):
        UD += ManualMotionPower

    if keyboard.is_pressed('down'):
        UD -= ManualMotionPower

    if keyboard.is_pressed('left'):
        Yaw -= ManualMotionPower

    if keyboard.is_pressed('right'):
        Yaw += ManualMotionPower

    motion = [LR, FB, UD, Yaw]

    return motion
