import math
import numpy as np

class Leg:
    def __init__(self, pinup, pinlo, label, kit, ref_angle, init_angle, length, origin, boid):
        self.l_up = length[0]
        self.l_lo = length[1]
        self.origin = origin
        self.label = label
        self.angle_x = ref_angle
        self.init_up_angle = init_angle[0]
        self.init_lo_angle = init_angle[1]
        self.angle_up = init_angle[0]
        self.angle_lo = init_angle[1]
        self.pinup = pinup
        self.pinlo = pinlo
        self.disable = False
        self.kit = kit
        self.boid = boid
        self.initialize(self.init_up_angle)

    def initialize(self, angle1 = 0):
        self.kit.set_angle(self.pinup, 90+angle1)
        self.kit.set_angle(self.pinlo, 90+self.init_lo_angle)
        self.angle_up = angle1

    def change_boid(self, boid):
        self.boid = boid

    def _disable(self):
        if self.disable == True:
            return
        self.inc_below_angle(60)
        self.disable = True
    
    def _enable(self):
        if self.disable == False:
            return
        self.inc_below_angle(-60)
        self.disable = False

    def set_up_angle(self, angle):
        self.angle_up = angle
        self.kit.set_angle(self.pinup, 90+self.angle_up)
    
    def inc_up_angle(self, inc):
        if self.disable:
            return
        self.angle_up += inc
        self.angle_up = max(self.angle_up, -90)
        self.angle_up = min(self.angle_up, 90)
        self.kit.set_angle(self.pinup, 90 + self.angle_up)

    def inc_below_angle(self, inc):
        if self.disable:
            return
        self.angle_lo += inc
        self.angle_lo = max(self.angle_lo, -90)
        self.angle_lo = min(self.angle_lo, 90)
        self.kit.set_angle(self.pinlo, 90 + self.angle_lo)
    
    def abs_cordinates(self, cog):
        the = self.angle_x
        rot_mat = np.array([[math.cos(the), -math.sin(the), 0], [math.sin(the), math.cos(the), 0], [0, 0, 1]])
        tra_mat = np.array([[self.origin[0]+cog[0]], [self.origin[1]+cog[1]], [self.origin[2]+cog[2]]])
        up_cord = self.get_up_cord(self.l_up, self.angle_up)
        up_cord = np.add(np.matmul(rot_mat, up_cord), tra_mat)
        low_cord = np.add(np.matmul(rot_mat, self.get_bel_cord()), tra_mat)
        origin_cord = tra_mat
        res_x = [origin_cord[0][0], up_cord[0][0], low_cord[0][0]]
        res_y = [origin_cord[1][0], up_cord[1][0], low_cord[1][0]]
        res_z = [origin_cord[2][0], up_cord[2][0], low_cord[2][0]]
        return [res_x, res_y, res_z, self.label]

    def get_up_cord(self, l, angle, z=0):
        return np.array([[l*math.cos(angle*math.pi/180)], [l*math.sin(angle*math.pi/180)], [z]])

    def get_bel_cord(self):
        return self.get_up_cord(self.l_up + self.l_lo*math.cos(self.angle_lo*math.pi/180), self.angle_up, -self.l_lo*math.sin(self.angle_lo*math.pi/180))

    def calc_inv(self, height):
        self.angle_lo = math.asin(height/self.l_lo)