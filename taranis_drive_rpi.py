'''
Working code to control motors with a Pololu Dual G2 High Power Motor Driver,
via an Arduino taking input data from a FrSky D4R-II receiver,
getting signals from a Taranis X9D+ RC controller
'''

from dual_g2_hpmd_rpi import motors
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

def arduino_input():
    '''
    Reads serial input from arduino, which gives values in the form:
    b'-480 -480\r\n'
    Splits this to get the two values, removes extra characters,
    then returns the speed of both motors as a list
    '''
    motor_speeds = []
    read_serial = ser.readline()
    new = str(read_serial).split()
    motor_speeds.append(int(new[0][2:]))
    motor_speeds.append(int(new[1][:-5]))
    return motor_speeds

while True:
    speed = arduino_input()
    motors.setSpeeds(speed[0], speed[1])
