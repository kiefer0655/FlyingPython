import detectionvol1 as detectionfile
import cv2
import DroneControl as DroneControl
import KeyboardInputHandler as KeyboardInputHandler
from GuiHandler import main as Gui
import keyboard
from time import sleep
from time import time

tools = Gui()

NoDrone = False if tools == "drone" else True
AutoModeSaftyLock = 0.7

if NoDrone == False:
    drone = DroneControl.GetDroneAndConnect()
    print(drone.get_battery())
else:
    cap = cv2.VideoCapture(0)

def GetFrame():
    if NoDrone == False:
        frame = DroneControl.GetFrame(drone)
    else:
        ret, frame = cap.read()
    return frame


print("Ready to be Take Off \nSpace to Take Off \nEscape to Escape")

while True:
    frame = GetFrame()
    cv2.imshow("Frame",frame)

    if cv2.waitKey(90) == 32:
        break
    if cv2.waitKey(90) == 27:
        if NoDrone == True:
            cap.release()
        cv2.destroyAllWindows()
        exit()
print("Take Off")

if NoDrone == False:
    drone.takeoff()
sleep(0.5)
if NoDrone == False:
    DroneControl.SendDroneControl(drone, (0,0,0,0))
sleep(0.5)
ManualControl = True
print("Control Onlined")

start = time()

while True:
    frame = GetFrame()

    if ManualControl == True:
        motion = KeyboardInputHandler.GetMotionByKeyboard()

    ManualControl = KeyboardInputHandler.ManualControlControler(ManualControl)

    frame , motion = detectionfile.DetectAndDraw(frame,ManualControl,motion)

    cv2.imshow("Frame",frame)

    if NoDrone == False:
        if time() - start > AutoModeSaftyLock or ManualControl == True:
            DroneControl.SendDroneControl(drone, motion)
            start = time()
        else:
            DroneControl.SendDroneControl(drone, (0,0,0,0))
    if cv2.waitKey(90) == 32:
        break

    sleep(0.05)

if NoDrone == False:
    DroneControl.Landing(drone)
else:
    cap.release()
cv2.destroyAllWindows()
