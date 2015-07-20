import time
import pygame
# Requires PyBluez
# import bluetooth
import serial

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
    RThumbX = 4
    RThumbY = 3
    RTrigger = 5


bluetoothEnabled = False
if bluetoothEnabled:
    macAddr = '30:14:06:17:02:72'
    port = 1

    blue = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    blue.connect((macAddr, port))
    print 'Bluetooth connection established.'
# Bluetooth Communication for Windows
ser = serial.Serial('COM6', 9600, timeout=0.1)

done = False
base = 110
arm = 140
forearm = 165
gripper = 25
motor_speed = 0

# Initialize joystick
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print 'Joystick initalized, press A to exit'


def button(i):
    return joystick.get_button(i) == 1


def axis(i):
    return -joystick.get_axis(i)


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

    # print axis(Axis.LTrigger)

    if button(Button.X) and gripper < 70:
        gripper += 1
    elif button(Button.B) == 1 and gripper > 25:
        gripper -= 1

    if axis(Axis.RThumbX) >= 0.2 and base < 175:
        base += axis(Axis.RThumbX) * 2
    if axis(Axis.RThumbX) <= -0.2 and base > 5:
        base += axis(Axis.RThumbX) * 2
    if axis(Axis.RThumbY) >= 0.2 and arm < 175:
        arm += axis(Axis.RThumbY) * 5
    if axis(Axis.RThumbY) <= -0.2 and arm > 5:
        arm += axis(Axis.RThumbY) * 5
    if button(Button.RBumper) and forearm < 175:
        forearm += 1
    if button(Button.LBumper) and forearm > 5:
        forearm -= 1
    leftMotor = (axis(Axis.LThumbY) + axis(Axis.LThumbX)) * -255
    rightMotor = (axis(Axis.LThumbY) - axis(Axis.LThumbX)) * -255
    if leftMotor > 255:
        leftMotor = 255
    if leftMotor < -255:
        leftMotor = -255
    if rightMotor > 255:
        rightMotor = 255
    if rightMotor < -255:
        rightMotor = -255
    time.sleep(0.05)
    ser.write('[%d] [%d] [%d] [%d] [%d] [%d]' % (
    int(base), int(arm), int(forearm), int(gripper), int(leftMotor), int(rightMotor)))
    # blue.send('[%d] [%d] [%d] [%d] [%d] [%d]' % (int(base), int(arm), int(forearm), int(gripper), int(leftMotor), int(rightMotor)))
    print '[%d] [%d] [%d] [%d] [%d] [%d]' % (
    int(base), int(arm), int(forearm), int(gripper), int(leftMotor), int(rightMotor))
# Ends with left right motor at PWM value of 0
leftMotor = 0
rightMotor = 0
print '[%d] [%d] [%d] [%d] [%d] [%d]' % (
int(base), int(arm), int(forearm), int(gripper), int(leftMotor), int(rightMotor))
ser.write('[%d] [%d] [%d] [%d] [%d] [%d]' % (
int(base), int(arm), int(forearm), int(gripper), int(leftMotor), int(rightMotor)))
# blue.send('[%d] [%d] [%d] [%d] [%d] [%d]' % (int(base), int(arm), int(forearm), int(gripper), int(leftMotor), int(rightMotor)))
joystick.quit()
pygame.joystick.quit()
pygame.quit()
