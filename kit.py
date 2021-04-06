import time
import math
from adafruit_servokit import ServoKit

class Kit:
    def __init__(self):
       self.kit = ServoKit(channels = 16)
       self.kit.servo[0].set_pulse_width_range(660, 2300)
       self.kit.servo[1].set_pulse_width_range(610, 2250)
       self.kit.servo[4].set_pulse_width_range(400, 2450)
       self.kit.servo[2].set_pulse_width_range(550, 2250)

    def set_angle(self, num, angle):
        self.kit.servo[num].angle = angle
        print(num, angle)
        time.sleep(0.2)