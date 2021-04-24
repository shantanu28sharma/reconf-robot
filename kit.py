import time
import math
from adafruit_servokit import ServoKit

class Kit:
    def __init__(self):
       self.kit = ServoKit(channels = 16)
       self.kit.servo[12].set_pulse_width_range(860, 2300)
       self.kit.servo[1].set_pulse_width_range(610, 2250)
       self.kit.servo[4].set_pulse_width_range(550, 2250)
       self.kit.servo[5].set_pulse_width_range(400, 2450)
       self.kit.servo[0].set_pulse_width_range(500, 2470)
       self.kit.servo[3].set_pulse_width_range(490, 2470)
       self.kit.servo[6].set_pulse_width_range(1080, 2250)
       self.kit.servo[7].set_pulse_width_range(560, 2270)
       self.kit.servo[8].set_pulse_width_range(740, 2300)
       self.kit.servo[9].set_pulse_width_range(610, 2250)
       self.kit.servo[10].set_pulse_width_range(570, 2350)
       self.kit.servo[11].set_pulse_width_range(740, 2350)

    def set_angle(self, num, angle):
        print("kit:-", num, angle)
        self.kit.servo[num].angle = angle
        
    def pwm(self, num, range):
        self.kit.servo[num].set_pulse_width_range(range[0], range[1])