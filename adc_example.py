from dual_g2_hpmd_rpi import motors
from time import sleep
import Adafruit_ADS1x15

GAIN = 1
adc = Adafruit_ADS1x15.ADS1115()

contHigh1 = 5589 #ch1
contLow1 = 3767 #ch1
_contHigh1 = 0
_contLow1 = 0
contHigh2 = 5758 #ch2
contLow2 = 4061 #ch2
_contHigh2 = 0
_contLow2 = 0
    
motorHigh = 480
motorLow = -480

contRange1 = contHigh1 - contLow1
contRange2 = contHigh2 - contLow2
motorRange = motorHigh - motorLow

def convertInput(contInput1, contInput2):
    print(str(contInput1) + " " + str(contInput2))
    if contInput1 in range(contLow1, contHigh1) and contInput2 in range(contLow2, contHigh2):
        
        contScaled1 = float(contInput1 - contLow1) / float(contRange1)
        contScaled2 = float(contInput2 - contLow2) / float(contRange2)
    
        speed1 = int(motorLow + (contScaled1 * motorRange))
        speed2 = int(motorLow + (contScaled2 * motorRange))
    
        print(str(speed1) + " " + str(speed2))
        #return (speed1, speed2)
    else:
        print("value out of range")
        #return False


def drive(left, right):
    speed = convertInput(left, right)
    if speed is not False:
        motors.setSpeeds(speed[0], speed[1])

#max_ch2 = 0
#min_ch2 = 1000

while True:
    ch1 = adc.read_adc(0, gain=GAIN)
    ch2 = adc.read_adc(1, gain=GAIN)
    #print(str(convertInput(ch1, ch2)[0]))
    #print(str(convertInput(ch1, ch2)[1]))
    convertInput(ch1, ch2)
    print()
    sleep(0.2)
    #drive(ch1, ch2)
    '''
    ch1 = adc.read_adc(0, gain=GAIN)
    ch2 = adc.read_adc(1, gain=GAIN)
    if ch2 < 500:
        if ch2 > max_ch2:
            max_ch2 = ch2
        if ch2 < min_ch2:
            min_ch2 = ch2
        print('Channel 2 = ' + str(ch2) + ", Max = " + str(max_ch2) + ", Min = " + str(min_ch2))
    sleep(0.2)
    '''
