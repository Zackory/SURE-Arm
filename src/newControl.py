
import time
import pygame
# Requires PyBluez
import bluetooth
# import serial

class Button:
    A = 0
    B = 1
    X = 2
    Y = 3
    LBumper = 4
    RBumper = 5

class Axis:
    LThumbX = 0
    LThumbY = 1
    LTrigger = 2
    RThumbX = 3
    RThumbY = 4
    RTrigger = 5

macAddr = '30:14:06:17:02:72'
port = 1

blue = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
blue.connect((macAddr, port))
print 'Bluetooth connection established.'

# ser = serial.Serial('COM6', 9600, timeout=0.1)

done = False
base = 90
arm = 90
forearm = 90
gripper = 25

# Initialize joystick
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print 'Joystick initalized, press A to exit'

def button(i):
    return joystick.get_button(i) == 1
def axis(i):
    return joystick.get_axis(i)
def hat(i):
    return joystick.get_hat(i)

while not done:
    # Process all events from pygame
    for event in pygame.event.get():
        pass

    # print [(button(i), button(i)) for i in xrange(joystick.get_numbuttons())]
    # print [axis(i) for i in xrange(joystick.get_numaxes())]
    # print [hat(i) for i in xrange(joystick.get_numhats())]

    done = button(Button.A)

    if button(Button.X) and gripper < 70:
        gripper += 1
    elif button(Button.B) == 1 and gripper > 25:
        gripper -= 1

    if axis(Axis.LThumbX) >= 0.1 and base < 175:
        base += axis(Axis.LThumbX)*5
    if axis(Axis.LThumbX) <= -0.1 and base > 5:
        base += axis(Axis.LThumbX)*5

    if axis(Axis.LThumbY) >= 0.1 and arm < 175:
        arm += axis(Axis.LThumbY)*5
    if axis(Axis.LThumbY) <= -0.1 and arm > 5:
        arm += axis(Axis.LThumbY)*5

    if axis(Axis.RThumbY) >= 0.1 and forearm < 175:
        forearm += axis(Axis.RThumbY)*5
    if axis(Axis.RThumbY) <= -0.1 and forearm > 5:
        forearm += axis(Axis.RThumbY)*5

    time.sleep(0.05)
    # ser.write('[%d] [%d] [%d] [%d]' % (int(base), int(arm), int(forearm), int(gripper)))
    blue.send('[%d] [%d] [%d] [%d]' % (int(base), int(arm), int(forearm), int(gripper)))

joystick.quit()
pygame.joystick.quit()
pygame.quit()