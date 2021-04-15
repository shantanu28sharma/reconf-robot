import time
import math
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)
i = 0
pin1 = 4
pin2 = 5
kit.servo[0].set_pulse_width_range(660, 2300)
kit.servo[1].set_pulse_width_range(610, 2250)
kit.servo[pin1].set_pulse_width_range(400, 2450)
kit.servo[pin2].set_pulse_width_range(490, 2270)
while i<3:
    kit.servo[pin1].angle = 110
    kit.servo[pin2].angle = 110
    time.sleep(0.5)
    kit.servo[pin1].angle = 90
    kit.servo[pin2].angle = 90
    time.sleep(0.5)
    i+=1