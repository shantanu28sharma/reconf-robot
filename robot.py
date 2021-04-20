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
        rotate = (move)*(direc)
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
        rotate = (move)*(direc)
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

    def simulate_quadruped(self, legs, inc, time, move = 1, direc = 1):
        print("#### Walking with four legs ####")

    def simulate_bipod(self, legs, inc, time, move = 1, direc = 1):
        print("#### Walking with two legs ####")
        
    def boid_count(self):
        boid1 = 0
        boid2 = 0
        for leg in self.legs:
            if leg.boid == 1:
                boid1+=1
            else:
                boid2+=1
        return (boid1, boid2)

    def fault(self, arr):
        for leg in arr:
            self.functional[leg] = False
            self.legs[leg]._disable()
        self.reconfigure()

    def recover(self, arr):
        for leg in arr:
            self.functional[leg] = True
            self.legs[leg]._enable()
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
            # self.simulate_tripod(40, 30, 3, 1, 1)
            # self.simulate_ripple(50, 30, 10, 1, 1)
            # do nothing
        elif num == 5:
            print("### Robot has Five legs ###")
            for (index, leg) in enumerate(self.functional):
                if leg == False:
                    remove = (index+3)%6
                    self.fault([remove])
                    break
            #disable one odd leg walk with four legs
        elif num == 4:
            print("### Robot has Four legs ###")
            (boid1, boid2) = self.boid_count()
            if boid1 == boid2:
                print()
                #find symmetry line and arrange the legs accordingly
            elif boid1 > boid2:
                print("inequal boid")
                found = False
                ind = 0
                while True:
                    leg = self.legs[ind]
                    if ind == 6:
                        ind = 0
                    if leg.disable == False and leg.boid == 2:
                        found = True
                    elif found and leg.disable == False and leg.boid == 1:
                        leg.change_boid(2)
                        break
                    ind+=1
                #move one leg from one boid to another
            else:
                print("inequal boid")
                found = False
                ind = 0
                while True:
                    leg = self.legs[ind]
                    if ind == 6:
                        ind = 0
                    if leg.disable == False and leg.boid == 1:
                        found = True
                    elif found and leg.disable == False and leg.boid == 2:
                        leg.change_boid(1)
                        break
                    ind+=1
                #move one bod to another
            # reconfigure according to the position of functional legs
        elif num == 3:
            print("### Robot has Three legs ###")
            # disable one odd leg, crawl with two legs
            dis = 10000
            ind1 = -1
            ind2 = -1
            functional = self.functional + self.functional
            prev = -1
            for (ind, state) in enumerate(functional):
                if state and prev==-1:
                    prev = ind
                elif state:
                    if abs(prev-ind%6) < dis:
                        ind1 = ind
                        ind2 = prev
                        dis = abs(prev-ind%6)
                    prev = ind
            for (ind, leg) in enumerate(self.legs):
                if ind == ind1:
                    leg.change_boid(1)
                elif ind == ind2:
                    leg.change_boid(2)
                elif leg.disable == False:
                    self.fault([ind])
            self.reconfigure()
        elif num == 2:
            functional_legs = []
            for leg in self.legs:
                if leg.disable == False:
                    functional_legs.append(leg)
            print("### Robot has Two legs ###")
            # reconfigure according to the position of legs and then crawl
        else:
            print("### Robot has One leg ###")
            # crawl
        self.initialize()
        return