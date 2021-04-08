from leg import Leg
from kit import Kit
import time

class Robot:
    def __init__(self, cog, m, f, s):
        self.cog = cog
        self.m = m
        self.f = f
        self.s = s
        self.kit = Kit()
        self.f1 = Leg(0, 1, "f1", self.kit, 60, [-25, 30], [20, 20], (f, s, 0))
        self.f2 = Leg(2, 3, "f2", self.kit, 120, [25, 30], [20, 20], (f, -s, 0))
        self.m1 = Leg(7, 8, "f1", self.kit, 60, [-15, 0], [20, 20], (f, s, 0))
        self.m2 = Leg(9, 10, "f1", self.kit, 60, [-15, 0], [20, 20], (f, s, 0))
        self.b1 = Leg(10, 11, "f1", self.kit, 60, [-15, 0], [20, 20], (f, s, 0))
        self.b2 = Leg(12, 13, "f1", self.kit, 60, [-15, 0], [20, 20], (f, s, 0))
        self.functional = [True]*6
        self.frames = []
        self.delay = 0.2

    def get_polygon(self):
        x_cor = [self.m+self.cog[0], self.f+self.cog[0], -self.f+self.cog[0], -self.m+self.cog[0], -self.f+self.cog[0], self.f+self.cog[0], self.m+self.cog[0]]
        y_cor = [self.cog[1], self.s+self.cog[1], self.s+self.cog[1], self.cog[1], -self.s+self.cog[1], -self.s+self.cog[1], self.cog[1]]
        z_cor = [0, 0, 0, 0, 0, 0, 0]
        return (x_cor, y_cor, z_cor, "polygon")
    
    def get_cords(self):
        x_cor = []
        y_cor = []
        z_cor = []
        label = []
        pol_cor = self.get_polygon()
        x_cor.append(pol_cor[0])
        y_cor.append(pol_cor[1])
        z_cor.append(pol_cor[2])
        label.append(pol_cor[3])
        pol_cor = self.f1.abs_cordinates(self.cog)
        x_cor.append(pol_cor[0])
        y_cor.append(pol_cor[1])
        z_cor.append(pol_cor[2])
        label.append(pol_cor[3])
        pol_cor = self.f2.abs_cordinates(self.cog)
        x_cor.append(pol_cor[0])
        y_cor.append(pol_cor[1])
        z_cor.append(pol_cor[2])
        label.append(pol_cor[3])
        pol_cor = self.m1.abs_cordinates(self.cog)
        x_cor.append(pol_cor[0])
        y_cor.append(pol_cor[1])
        z_cor.append(pol_cor[2])
        label.append(pol_cor[3])
        pol_cor = self.m2.abs_cordinates(self.cog)
        x_cor.append(pol_cor[0])
        y_cor.append(pol_cor[1])
        z_cor.append(pol_cor[2])
        label.append(pol_cor[3])
        pol_cor = self.b1.abs_cordinates(self.cog)
        x_cor.append(pol_cor[0])
        y_cor.append(pol_cor[1])
        z_cor.append(pol_cor[2])
        label.append(pol_cor[3])
        pol_cor = self.b2.abs_cordinates(self.cog)
        x_cor.append(pol_cor[0])
        y_cor.append(pol_cor[1])
        z_cor.append(pol_cor[2])
        label.append(pol_cor[3])
        return [x_cor, y_cor, z_cor, label] 

    def post_process(self):
        self.frames.append(self.get_cords())
        time.sleep(self.delay)    
    
    def simulate_tripod(self, inc, time):
        frames = []
        self.f1.inc_up_angle(inc/2)
        self.m2.inc_up_angle(inc/2)
        self.b1.inc_up_angle(inc/2)
        self.m1.inc_up_angle(inc/2)
        self.b2.inc_up_angle(inc/2)
        self.f2.inc_up_angle(inc/2)
        self.post_process()
        for i in range(time):
            self.f2.inc_up_angle(-inc/2)
            self.m1.inc_up_angle(-inc/2)
            self.b2.inc_up_angle(-inc/2)
            self.m2.inc_up_angle(-inc/2)
            self.b1.inc_up_angle(-inc/2)
            self.f1.inc_up_angle(-inc/2)
            self.f2.inc_below_angle(-inc)
            self.m2.inc_below_angle(-inc)
            self.b2.inc_below_angle(-inc)
            self.post_process()
            self.f2.inc_up_angle(-inc/2)
            self.m1.inc_up_angle(-inc/2)
            self.b2.inc_up_angle(-inc/2)
            self.m2.inc_up_angle(-inc/2)
            self.b1.inc_up_angle(-inc/2)
            self.f1.inc_up_angle(-inc/2)
            self.f2.inc_below_angle(inc)
            self.m2.inc_below_angle(inc)
            self.b2.inc_below_angle(inc)
            self.post_process()
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
            self.f2.inc_up_angle(inc/2)
            self.m1.inc_up_angle(inc/2)
            self.b2.inc_up_angle(inc/2)
            self.m2.inc_up_angle(inc/2)
            self.b1.inc_up_angle(inc/2)
            self.f1.inc_up_angle(inc/2)
            self.m1.inc_below_angle(-inc)
            self.b1.inc_below_angle(-inc)
            self.f1.inc_below_angle(-inc)
            self.post_process()
            self.f2.inc_up_angle(inc/2)
            self.m1.inc_up_angle(inc/2)
            self.b2.inc_up_angle(inc/2)
            self.m2.inc_up_angle(inc/2)
            self.b1.inc_up_angle(inc/2)
            self.f1.inc_up_angle(inc/2)
            self.m1.inc_below_angle(inc)
            self.b1.inc_below_angle(inc)
            self.f1.inc_below_angle(inc)
            self.post_process()
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
        return frames 
    
    def simulate_ripple(self, inc, _time):
        frames = []
        self.f1.inc_up_angle(inc/2)
        self.f2.inc_up_angle(-inc/4)
        self.m1.inc_up_angle(-inc/4)
        self.m2.inc_up_angle(-inc/2)
        self.b1.inc_up_angle(-inc/4)
        self.b2.inc_up_angle(-inc/4)
        self.post_process()
        for i in range(_time):
            self.f1.inc_up_angle(-inc/2)
            self.f2.inc_up_angle(inc/4)
            self.m1.inc_up_angle(inc/4)
            self.m2.inc_up_angle(inc/2)
            self.b1.inc_up_angle(inc/4)
            self.b2.inc_up_angle(inc/4)
            self.f1.inc_below_angle(-inc)
            self.m2.inc_below_angle(-inc)
            self.post_process()
            self.f1.inc_up_angle(-inc/2)
            self.f2.inc_up_angle(inc/4)
            self.m1.inc_up_angle(inc/4)
            self.m2.inc_up_angle(inc/2)
            self.b1.inc_up_angle(inc/4)
            self.b2.inc_up_angle(inc/4)
            self.f1.inc_below_angle(inc)
            self.m2.inc_below_angle(inc)
            self.post_process()
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
            self.f1.inc_up_angle(inc/4)
            self.f2.inc_up_angle(inc/4)
            self.m1.inc_up_angle(-inc/2)
            self.m2.inc_up_angle(-inc/4)
            self.b1.inc_up_angle(inc/4)
            self.b2.inc_up_angle(-inc/2)
            self.m1.inc_below_angle(-inc)
            self.b2.inc_below_angle(-inc)
            self.post_process()
            self.f1.inc_up_angle(inc/4)
            self.f2.inc_up_angle(inc/4)
            self.m1.inc_up_angle(-inc/2)
            self.m2.inc_up_angle(-inc/4)
            self.b1.inc_up_angle(inc/4)
            self.b2.inc_up_angle(-inc/2)
            self.m1.inc_below_angle(inc)
            self.b2.inc_below_angle(inc)
            self.post_process()
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
            self.f1.inc_up_angle(inc/4)
            self.f2.inc_up_angle(-inc/2)
            self.m1.inc_up_angle(inc/4)
            self.m2.inc_up_angle(-inc/4)
            self.b1.inc_up_angle(-inc/2)
            self.b2.inc_up_angle(inc/4)
            self.f2.inc_below_angle(-inc)
            self.b1.inc_below_angle(-inc)
            self.post_process()
            self.f1.inc_up_angle(inc/4)
            self.f2.inc_up_angle(-inc/2)
            self.m1.inc_up_angle(inc/4)
            self.m2.inc_up_angle(-inc/4)
            self.b1.inc_up_angle(-inc/2)
            self.b2.inc_up_angle(inc/4)
            self.f2.inc_below_angle(inc)
            self.b1.inc_below_angle(inc)
            self.post_process()
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
        return frames

    def fault(self, arr):
        for leg in arr:
            self.functional[leg.index] = False
            leg._disable()
        self.reconfigure()

    def recover(self, arr):
        for leg in arr:
            self.functional[leg.index] = True
            leg._enable()
        self.reconfigure()
    
    def get_number_legs(self):
        num = 0
        for leg in self.functional:
            if leg:
                num = num+1
        return num

    def reconfigure(self):
        num = self.get_number_legs()
        if num == 6:
            self.simulate_ripple(30, 2)
            # do nothing
        elif num == 5:
            print()
            #disable one odd leg walk with four legs
        elif num == 4:
            print()
            # reconfigure according to the position of functional legs
        elif num == 3:
            print()
            # disable one odd leg, crawl witb two legs
        elif num == 2:
            print()
            #   reconfigure according to the position of legs and then crawl
        else:
            print()
            # crawl
        return
            
    def walk(self):
        return
    
    def crawl(self):
        return