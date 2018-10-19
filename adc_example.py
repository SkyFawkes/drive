from dual_g2_hpmd_rpi import motors
from time import sleep
import Adafruit_ADS1x15

GAIN = 1
adc = Adafruit_ADS1x15.ADS1115()

def convertInput(contInput1, contInput2):
    contHigh1 = 5589 #ch1
    contLow1 = 3767 #ch1
    contHigh2 = 5758
    contLow2 = 4061
    
    motorHigh = 480
    motorLow = -480

    contRange1 = contHigh1 - contLow1
    contRange2 = contHigh2 - contLow2
    motorRange = motorHigh - motorLow
    
    if contInput1 <= contHigh1 and contInput1 >= contLow1:
        contScaled1 = float(contInput1 - contLow1) / float(contRange1)
        if contInput2 <= contHigh2 and contInput2 >= contLow2:
            contScaled2 = float(contInput2 - contLow2) / float(contRange2)
    
            speed1 = motorLow + (contScaled1 * motorRange)
            speed2 = motorLow + (contScaled2 * motorRange)
    
            print(str(speed1) + " " + str(speed2))
            return (speed1, speed2)
    else:
        return False
    
'''    if speed1 >= motorLow and speed1 <= motorHigh and speed2 >= motorLow and speed2 <= motorHigh:
        return (speed1, speed2)
    else:
        return False'''

def drive(left, right):
    speed = convertInput(left, right)
    if speed is not False:
        motors.setSpeeds(speed[0], speed[1])

#max_ch2 = 4000
#min_ch2 = 4500

while True:
    ch1 = adc.read_adc(0, gain=GAIN)
    ch2 = adc.read_adc(1, gain=GAIN)
    #print(str(convertInput(ch1, ch2)[0]))
    #print(str(convertInput(ch1, ch2)[1]))
    print(str(convertInput(ch1, ch2)))
    #drive(ch1, ch2)
    '''
    #ch1 = adc.read_adc(0, gain=GAIN)
    ch2 = adc.read_adc(1, gain=GAIN)
    if ch2 > 4000:
        if ch2 > max_ch2:
            max_ch2 = ch2
        if ch2 < min_ch2:
            min_ch2 = ch2
        print('Channel 2 = ' + str(ch2) + ", Max = " + str(max_ch2) + ", Min = " + str(min_ch2))

    #if ch2 > 2000:
        #print('Channel 2 = ' + str(ch2))
    sleep(0.2)
    '''
