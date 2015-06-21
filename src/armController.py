import XboxController
import serial
import time

#Right Joystick = xboxCont.RTRIGGER
#Trigger = xboxCont.RTHUMBX

angle = 0
# For Linux based systems
ser = serial.Serial('/dev/ttyACM2', 9600, timeout=0.1)
# For Windows based systems
# ser = serial.Serial('COM4', 9600, timeout=0.1)

xboxCont = XboxController.XboxController(
    controllerCallBack = None,
    joystickNo = 0,
    deadzone = 0.1,
    scale = 1,
    invertYAxis = False)
xboxCont.start()

while True:
    if xboxCont.A == 1.0:
        break
    elif xboxCont.X > 0 and angle < 180:
        angle += 1
    elif xboxCont.B > 0 and angle > 0:
        angle -= 1
    print angle
    time.sleep(0.01)
    ser.write('%d\n' % angle)

xboxCont.stop()
