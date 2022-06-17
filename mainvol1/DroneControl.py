from djitellopy import tello
from time import sleep

def GetDroneAndConnect():
    drone = tello.Tello()
    drone.connect()
    drone.streamon()
    return drone

def GetFrame(drone):
    return drone.get_frame_read().frame


def Landing(drone):
    drone.send_rc_control(0,0,0,0)
    sleep(2)
    drone.land()

def SendDroneControl(drone, motion):

    LR, FB, UD, Yaw = motion
    drone.send_rc_control(LR,FB,UD,Yaw)
