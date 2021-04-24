import time
import math
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)
i = 0
pins = [0]
kit.servo[8].set_pulse_width_range(500, 2470)
while i<3:
    for pin in pins:
        kit.servo[pin].angle = 110
    time.sleep(0.5)
    for pin in pins:
        kit.servo[pin].angle=90
    time.sleep(0.5)
    i+=1