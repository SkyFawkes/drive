from __future__ import print_function
from time import sleep
from dual_g2_hpmd_rpi import motors, MAX_SPEED

s = MAX_SPEED//2
on = False
dir = False

print("press 'e' to enable motors")
print()
while True:
    if dir == "exit":
        break
    dir = input(">> ")
    if dir == "exit":
        break
    elif dir == "e":
        motors.enable()
        print("motors enabled")
        on = True
        print("press 'w', 's', 'a', 'd' for movement")
        print("type int between 0 and " + str(MAX_SPEED) + " to change speed")
        print("press 'x' to disable motors")
        print()
    else:
        print("press 'e' to enable motors")
        print()
    while on == True:
        dir = input(">> ")
        if dir == "exit":
            break
        try:
            dir = int(dir)
            if dir >= 0 and dir <= MAX_SPEED:
                s = dir
            else:
                print("type int between 0 and " + str(MAX_SPEED) + " to change speed")
        except:
            if dir == "r":
                s = MAX_SPEED//2
                print("speed reset to " + str(MAX_SPEED//2))
            elif dir == "w":
                motors.setSpeeds(s, s)
                sleep(0.5)
                motors.setSpeeds(0, 0)
            elif dir == "s":
                motors.setSpeeds(-s, -s)
                sleep(0.5)
                motors.setSpeeds(0, 0)
            elif dir == "a":
                motors.setSpeeds(-s, s)
                sleep(0.5)
                motors.setSpeeds(0, 0)
            elif dir == "d":
                motors.setSpeeds(s, -s)
                sleep(0.5)
                motors.setSpeeds(0, 0)
            elif dir == "x":
                motors.disable()
                print("motors disabled")
                on = False
                print("press 'e' to enable motors")
                print()
            else:
                motors.setSpeeds(0, 0)
                print("press 'w', 's', 'a', 'd' for movement")
                print("type int between 0 and " + str(MAX_SPEED) + " to change speed")
                print("press 'x' to disable motors")
                print()
