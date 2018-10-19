# forum.piborg.org/node/535

import pigpio
import time

pi = pigpio.pi()

rising = 0
falling = 0
lowTime = 0

pi.set_mode(17, pigpio.INPUT)

while True:
    if pi.wait_for_edge(17):
        rising1 = time.time()
        
    if pi.wait_for_edge(17, pigpio.FALLING_EDGE, 5.0):
        falling = time.time()
    
    if pi.wait_for_edge(17):
        rising2 = time.time()
    
    highTime = falling - rising1
    lowTime = rising2 - falling
    dutyIn = highTime / (highTime + lowTime)
    
    print(dutyIn)
    print(highTime)
    print(lowTime)
    print(highTime + lowTime)
    print("---")
