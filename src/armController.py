import XboxController
import serial
import time
# Requires PyBluez
import bluetooth

macAddr = '30:14:06:17:02:72'
port = 1

socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
socket.connect((macAddr, port))

angle = 25
# For Linux based systems
# ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.1)
# ser = serial.Serial('/dev/rfcomm1', 9600, timeout=0.1)
# For Windows based systems
# ser = serial.Serial('COM4', 9600, timeout=0.1)

# xboxCont = XboxController.XboxController(
#     controllerCallBack=None,
#     joystickNo=0,
#     deadzone=0.1,
#     scale=1,
#     invertYAxis=False)
# xboxCont.start()

incr = True
while True:
    # if angle < 70 and incr:
    #     angle += 1
    # elif incr:
    #     incr = False
    # elif angle > 25 and not incr:
    #     angle -= 1
    # else:
    #     incr = True

    # if xboxCont.A == 1.0:
    #     break
    # elif xboxCont.X > 0 and angle < 70:
    #     angle += 1
    # elif xboxCont.B > 0 and angle > 25:
    #     angle -= 1
    print angle
    time.sleep(0.01)
    # ser.write('%d ' % angle)
    socket.send('%d ' % angle)


# xboxCont.stop()
socket.close()
