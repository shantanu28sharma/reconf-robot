import time
import math
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)
i = 0
pin1 = 2
pin2 = 3
kit.servo[pin1].set_pulse_width_range(400, 2250)
kit.servo[pin2].set_pulse_width_range(550, 2250)
i = 0
while i<3:
    kit.servo[pin1].angle = 180
    kit.servo[pin1].angle = 90
    time.sleep(0.5)
    kit.servo[pin2].angle = 180
    kit.servo[pin2].angle = 90
    time.sleep(0.5)
    i = i+1