import cv2

GREEN = (0,255,0)
RED = (0,0,255)
BLUE = (255,0,0)

MotionPower = 20

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

def Detection(model,frame):
    if model == "face":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

        Detected = False

        mid = None

        for (x, y, w, h) in faces:

            mid = (int(x + w/2),int(y + h/2))

            cv2.rectangle(frame, (x,y), (x + w,y + h), GREEN , 2)

            Detected = True

        return frame, Detected, mid

def Draw(frame,ItemMid, mid, command, motion ,ManualControl):
    LineDeltaHigh = int(frame.shape[0]/3)
    LineDeltaWeight = int(frame.shape[1]/3)

    cv2.line(frame, (LineDeltaWeight,0), (LineDeltaWeight,frame.shape[0]), BLUE, 2)
    cv2.line(frame, (2 * LineDeltaWeight,0), (2 * LineDeltaWeight,frame.shape[0]), BLUE, 2)
    cv2.line(frame, (0,LineDeltaHigh), (frame.shape[1],LineDeltaHigh), BLUE, 2)
    cv2.line(frame, (0,2 * LineDeltaHigh), (frame.shape[1],2 * LineDeltaHigh), BLUE, 2)

    if ItemMid != None:
        cv2.circle(frame, mid, radius = 10, color = RED , thickness = -1)
        cv2.line(frame, ItemMid, mid, RED, 5)

    cv2.putText(frame, command , (50,70),cv2.FONT_HERSHEY_SIMPLEX, 2 , GREEN, 1, cv2.LINE_AA)
    cv2.putText(frame, str(motion) , (50,frame.shape[0] - 50),cv2.FONT_HERSHEY_SIMPLEX, 1 , RED, 2, cv2.LINE_AA)

    ManualControlText = "Manual Control: ON" if ManualControl else "Manual Control: OFF"

    cv2.putText(frame, ManualControlText , (frame.shape[1] - 350,60),cv2.FONT_HERSHEY_SIMPLEX, 1 , RED, 1, cv2.LINE_AA)

    return frame

def GetMotion(ItemMid, midpoint, command):
    motion = [0,0,0,0]
    if command[1] != "":
        if ItemMid[0] < midpoint[0]:
            motion[0] = -MotionPower
        if ItemMid[0] > midpoint[0]:
            motion[0] = MotionPower
    if command[0] != "":
        if ItemMid[1] < midpoint[1]:
            motion[2] = MotionPower
        if ItemMid[1] > midpoint[1]:
            motion[2] = -MotionPower
    return motion

def DetectAndDraw(frame,ManualControl,motion):

    midpoint = (int(frame.shape[1]/2),int(frame.shape[0]/2))

    cv2.circle(frame, midpoint, radius = 5, color = RED , thickness = -1)

    frame, Detected, ItemMid = Detection(model = "face", frame = frame)

    action = ["",""]

    if Detected == True:
        LineDeltaHigh = int(frame.shape[0]/3)
        LineDeltaWeight = int(frame.shape[1]/3)

        if ItemMid[0] < LineDeltaWeight:
            action[1] = "Left"
        if ItemMid[0] > 2 * LineDeltaWeight:
            action[1] = "Right"

        if ItemMid[1] < LineDeltaHigh:
            action[0] = "Up"
        if ItemMid[1] > 2 * LineDeltaHigh:
            action[0] = "Low"

    if ManualControl == False:
            motion = GetMotion(ItemMid, midpoint, action)

    command = action[0]+action[1]

    frame = Draw(frame,ItemMid, midpoint, command , motion, ManualControl)

    return frame , motion
