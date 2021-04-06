import time
import math
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)
i = 0
kit.servo[0].set_pulse_width_range(660, 2300)
kit.servo[1].set_pulse_width_range(610, 2250)
kit.servo[4].set_pulse_width_range(400, 2450)
kit.servo[2].set_pulse_width_range(550, 2250)
while i<3:
    kit.servo[0].angle = 30
    kit.servo[2].angle = 150
    time.sleep(0.5)
    kit.servo[1].angle = 150
    kit.servo[4].angle = 150
    time.sleep(0.5)
    kit.servo[0].angle = 90
    kit.servo[2].angle = 90
    time.sleep(0.5)
    kit.servo[1].angle = 90
    kit.servo[4].angle = 90
    time.sleep(0.5)
    i = i+1