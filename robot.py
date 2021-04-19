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
        self.f1 = Leg(12, 1, "f1", self.kit, 60, [-25, 20], [20, 20], (f, s, 0), 1)
        self.f2 = Leg(4, 5, "f2", self.kit, 120, [25, 20], [20, 20], (f, -s, 0), 2)
        self.m1 = Leg(0, 3, "m1", self.kit, 60, [0, 20], [20, 20], (f, s, 0), 1)
        self.m2 = Leg(6, 7, "m2", self.kit, 60, [0, 20], [20, 20], (f, s, 0), 2)
        self.b1 = Leg(8, 9, "b1", self.kit, 60, [25, 20], [20, 20], (f, s, 0), 1)
        self.b2 = Leg(10, 11, "b2", self.kit, 60, [-25, 20], [20, 20], (f, s, 0), 2)
        self.functional = [True]*6
        self.legs = [self.f1, self.f2, self.m2, self.b2, self.b1, self.m1]
        self.frames = []
        self.delay = 0.2

    def get_polygon(self):
        x_cor = [self.m+self.cog[0], self.f+self.cog[0], -self.f+self.cog[0], -self.m+self.cog[0], -self.f+self.cog[0], self.f+self.cog[0], self.m+self.cog[0]]
        y_cor = [self.cog[1], self.s+self.cog[1], self.s+self.cog[1], self.cog[1], -self.s+self.cog[1], -self.s+self.cog[1], self.cog[1]]
        z_cor = [0, 0, 0, 0, 0, 0, 0]
        return (x_cor, y_cor, z_cor, "polygon")

    def initialize(self):
        self.f1.initialize()
        self.f2.initialize()
        self.m1.initialize()
        self.m2.initialize()
        self.b1.initialize()
        self.b2.initialize()
        self.post_process(-1)
    
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

    def post_process(self, info):
        self.frames.append(self.get_cords())
        print(info)
        time.sleep(self.delay)    
        # input()
    
    def simulate_tripod(self, inc, inc_down, _time, move = 1, direc = 1):
        print("##### Tripod Gait #####")
        rotate = (move)*(direction)
        self.f1.inc_up_angle(inc/2*(rotate))
        self.m2.inc_up_angle(-inc/2*(-rotate))
        self.b1.inc_up_angle(inc/2*(rotate))
        self.m1.inc_up_angle(-inc/2*(rotate))
        self.b2.inc_up_angle(inc/2*(-rotate))
        self.f2.inc_up_angle(inc/2*(-rotate))
        self.post_process(0)
        for i in range(_time):
            self.f1.inc_up_angle(-inc/2*(rotate))
            self.m2.inc_up_angle(inc/2*(-rotate))
            self.b1.inc_up_angle(-inc/2*(rotate))
            self.m1.inc_up_angle(inc/2*(rotate))
            self.b2.inc_up_angle(-inc/2*(-rotate))
            self.f2.inc_up_angle(-inc/2*(-rotate))
            self.f2.inc_below_angle(inc_down/2)
            self.m1.inc_below_angle(inc_down/2)
            self.b2.inc_below_angle(inc_down/2)
            self.post_process(1)
            self.f1.inc_up_angle(-inc/2*(rotate))
            self.m2.inc_up_angle(inc/2*(-rotate))
            self.b1.inc_up_angle(-inc/2*(rotate))
            self.m1.inc_up_angle(inc/2*(rotate))
            self.b2.inc_up_angle(-inc/2*(-rotate))
            self.f2.inc_up_angle(-inc/2*(-rotate))
            self.f2.inc_below_angle(-inc_down/2)
            self.m1.inc_below_angle(-inc_down/2)
            self.b2.inc_below_angle(-inc_down/2)
            self.post_process(2)
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
            self.f1.inc_up_angle(inc/2*(-rotate))
            self.m2.inc_up_angle(-inc/2*(rotate))
            self.b1.inc_up_angle(inc/2*(-rotate))
            self.m1.inc_up_angle(-inc/2*(-rotate))
            self.b2.inc_up_angle(inc/2*(rotate))
            self.f2.inc_up_angle(inc/2*(rotate))
            self.f1.inc_below_angle(inc_down/2)
            self.m2.inc_below_angle(inc_down/2)
            self.b1.inc_below_angle(inc_down/2)
            self.post_process(3)
            self.f1.inc_up_angle(inc/2*(-rotate))
            self.m2.inc_up_angle(-inc/2*(rotate))
            self.b1.inc_up_angle(inc/2*(-rotate))
            self.m1.inc_up_angle(-inc/2*(-rotate))
            self.b2.inc_up_angle(inc/2*(rotate))
            self.f2.inc_up_angle(inc/2*(rotate))
            self.f1.inc_below_angle(-inc_down/2)
            self.m2.inc_below_angle(-inc_down/2)
            self.b1.inc_below_angle(-inc_down/2)
            self.post_process(4)
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
    
    def simulate_ripple(self, inc, inc_down, _time, move = 1, direc = 1):
        print("###### Ripple Gait #######")
        rotate = (move)*(direction)
        self.f1.inc_up_angle(inc/2*(rotate))
        self.m1.inc_up_angle(-inc/2*(rotate))
        self.m2.inc_up_angle(-inc/2*(-rotate))
        self.b2.inc_up_angle(inc/2*(-rotate))
        self.post_process(0)
        for i in range(_time):
            self.f1.inc_up_angle(-inc/4*(rotate))
            self.f2.inc_up_angle(inc/4*(-rotate))
            self.m1.inc_up_angle(inc/2*(rotate))
            self.m2.inc_up_angle(inc/4*(-rotate))
            self.b1.inc_up_angle(-inc/4*(rotate))
            self.b2.inc_up_angle(-inc/2*(-rotate))
            self.m1.inc_below_angle(inc_down)
            self.b2.inc_below_angle(inc_down)
            self.post_process(1)
            self.f1.inc_up_angle(-inc/4*(rotate))
            self.f2.inc_up_angle(inc/4*(-rotate))
            self.m1.inc_up_angle(inc/2*(rotate))
            self.m2.inc_up_angle(inc/4*(-rotate))
            self.b1.inc_up_angle(-inc/4*(rotate))
            self.b2.inc_up_angle(-inc/2*(-rotate))
            self.m1.inc_below_angle(-inc_down)
            self.b2.inc_below_angle(-inc_down)
            self.post_process(2)
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
            self.f1.inc_up_angle(-inc/4*(rotate))
            self.f2.inc_up_angle(-inc/2*(-rotate))
            self.m1.inc_up_angle(-inc/4*(rotate))
            self.m2.inc_up_angle(inc/4*(-rotate))
            self.b1.inc_up_angle(inc/2*(rotate))
            self.b2.inc_up_angle(inc/4*(-rotate))
            self.b1.inc_below_angle(inc_down)
            self.f2.inc_below_angle(inc_down)
            self.post_process(3)
            self.f1.inc_up_angle(-inc/4*(rotate))
            self.f2.inc_up_angle(-inc/2*(-rotate))
            self.m1.inc_up_angle(-inc/4*(rotate))
            self.m2.inc_up_angle(inc/4*(-rotate))
            self.b1.inc_up_angle(inc/2*(rotate))
            self.b2.inc_up_angle(inc/4*(-rotate))
            self.b1.inc_below_angle(-inc_down)
            self.f2.inc_below_angle(-inc_down)
            self.post_process(4)
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
            self.f1.inc_up_angle(inc/2*(rotate))
            self.f2.inc_up_angle(inc/4*(-rotate))
            self.m1.inc_up_angle(-inc/4*(rotate))
            self.m2.inc_up_angle(-inc/2*(-rotate))
            self.b1.inc_up_angle(-inc/4*(rotate))
            self.b2.inc_up_angle(inc/4*(-rotate))
            self.f1.inc_below_angle(inc_down)
            self.m2.inc_below_angle(inc_down)
            self.post_process(5)
            self.f1.inc_up_angle(inc/2*(rotate))
            self.f2.inc_up_angle(inc/4*(-rotate))
            self.m1.inc_up_angle(-inc/4*(rotate))
            self.m2.inc_up_angle(-inc/2*(-rotate))
            self.b1.inc_up_angle(-inc/4*(rotate))
            self.b2.inc_up_angle(inc/4*(-rotate))
            self.f1.inc_below_angle(-inc_down)
            self.m2.inc_below_angle(-inc_down)
            self.post_process(6)
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])

    def boid_count(self):
        boid1 = 0
        boid2 = 0
        for leg in legs:
            if leg.boid == 1:
                boid1+=1
            else:
                boid2+=1
        return (boid1, boid2)

    def fault(self, arr):
        for leg in arr:
            self.functional[leg] = False
            legs[leg]._disable()
        self.reconfigure()

    def recover(self, arr):
        for leg in arr:
            self.functional[leg] = True
            legs[leg]._enable()
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
            print("### Robot has Six legs ###")
            # self.simulate_tripod(40, 30, 3)
            self.simulate_ripple(50, 30, 10)
            # do nothing
        elif num == 5:
            print("### Robot has Five legs ###")
            for (index, leg) in enumerate(functional):
                if leg == False:
                    remove = (index+3)%6
                    self.fault([remove])
                    break
            #disable one odd leg walk with four legs
        elif num == 4:
            print("### Robot has Four legs ###")
            (boid1, boid2) = self.boid_count()
            if boid1 == boid2:
                
            elif boid1 > boid2:

            else:

            # reconfigure according to the position of functional legs
        elif num == 3:
            print("### Robot has Three legs ###")
            # disable one odd leg, crawl witb two legs
        elif num == 2:
            print("### Robot has Two legs ###")
            #   reconfigure according to the position of legs and then crawl
        else:
            print("### Robot has One leg ###")
            # crawl
        self.initialize()
        return
            
    def walk(self):
        return
    
    def crawl(self):
        return