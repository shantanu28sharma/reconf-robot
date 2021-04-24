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
        self.f1 = Leg(12, 1, "f1", self.kit, 60, [-25, 30], [20, 20], (f, s, 0), 1)
        self.f2 = Leg(4, 5, "f2", self.kit, 120, [25, 30], [20, 20], (f, -s, 0), 2)
        self.m1 = Leg(0, 3, "m1", self.kit, 60, [0, 30], [20, 20], (f, s, 0), 1)
        self.m2 = Leg(6, 7, "m2", self.kit, 60, [0, 30], [20, 20], (f, s, 0), 2)
        self.b1 = Leg(8, 9, "b1", self.kit, 60, [25, 30], [20, 20], (f, s, 0), 1)
        self.b2 = Leg(10, 11, "b2", self.kit, 60, [-25, 30], [20, 20], (f, s, 0), 2)
        self.legs = [self.f1, self.f2, self.m2, self.b2, self.b1, self.m1]
        self.frames = []
        self.delay = 0.4
        # self.initialize()

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
        input()
    
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

    def post_process(self, info, safe = False):
        self.frames.append(self.get_cords())
        print(info)
        time.sleep(self.delay)    
        # if safe:
        # input()
    
    def simulate_tripod(self, inc, inc_down, _time, move = 1, direc = 1):
        print("##### Tripod Gait #####")
        rotate = (move)*(direc)
        self.f1.inc_up_angle(inc/2)
        self.m2.inc_up_angle(-inc/2*(rotate))
        self.b1.inc_up_angle(inc/2)
        self.m1.inc_up_angle(-inc/2)
        self.b2.inc_up_angle(inc/2*(rotate))
        self.f2.inc_up_angle(inc/2*(rotate))
        self.post_process(0)
        for _ in range(_time):
            self.f1.inc_up_angle(-inc/2)
            self.m2.inc_up_angle(inc/2*(rotate))
            self.b1.inc_up_angle(-inc/2)
            self.m1.inc_up_angle(inc/2)
            self.b2.inc_up_angle(-inc/2*(rotate))
            self.f2.inc_up_angle(-inc/2*(rotate))
            self.f2.inc_below_angle(inc_down/2)
            self.m1.inc_below_angle(inc_down/2)
            self.b2.inc_below_angle(inc_down/2)
            self.post_process(1)
            self.f1.inc_up_angle(-inc/2)
            self.m2.inc_up_angle(inc/2*(rotate))
            self.b1.inc_up_angle(-inc/2)
            self.m1.inc_up_angle(inc/2)
            self.b2.inc_up_angle(-inc/2*(rotate))
            self.f2.inc_up_angle(-inc/2*(rotate))
            self.f2.inc_below_angle(-inc_down/2)
            self.m1.inc_below_angle(-inc_down/2)
            self.b2.inc_below_angle(-inc_down/2)
            self.post_process(2)
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
            self.f1.inc_up_angle(inc/2*(rotate))
            self.m2.inc_up_angle(-inc/2)
            self.b1.inc_up_angle(inc/2*(rotate))
            self.m1.inc_up_angle(-inc/2*(rotate))
            self.b2.inc_up_angle(inc/2)
            self.f2.inc_up_angle(inc/2)
            self.f1.inc_below_angle(inc_down/2)
            self.m2.inc_below_angle(inc_down/2)
            self.b1.inc_below_angle(inc_down/2)
            self.post_process(3)
            self.f1.inc_up_angle(inc/2*(rotate))
            self.m2.inc_up_angle(-inc/2)
            self.b1.inc_up_angle(inc/2*(rotate))
            self.m1.inc_up_angle(-inc/2*(rotate))
            self.b2.inc_up_angle(inc/2)
            self.f2.inc_up_angle(inc/2)
            self.f1.inc_below_angle(-inc_down/2)
            self.m2.inc_below_angle(-inc_down/2)
            self.b1.inc_below_angle(-inc_down/2)
            self.post_process(4)
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
    
    def simulate_ripple(self, inc, inc_down, _time, move = 1, direc = 1):
        print("###### Ripple Gait #######")
        rotate = (move)*(direc)
        self.f1.inc_up_angle(inc/2)
        self.m1.inc_up_angle(-inc/2)
        self.m2.inc_up_angle(-inc/2*(rotate))
        self.b2.inc_up_angle(inc/2*(rotate))
        self.post_process(0)
        for _ in range(_time):
            self.f1.inc_up_angle(-inc/4)
            self.f2.inc_up_angle(inc/4*(rotate))
            self.m1.inc_up_angle(inc/2)
            self.m2.inc_up_angle(inc/4*(rotate))
            self.b1.inc_up_angle(-inc/4)
            self.b2.inc_up_angle(-inc/2*(rotate))
            self.m1.inc_below_angle(inc_down)
            self.b2.inc_below_angle(inc_down)
            self.post_process(1)
            self.f1.inc_up_angle(-inc/4)
            self.f2.inc_up_angle(inc/4*(rotate))
            self.m1.inc_up_angle(inc/2)
            self.m2.inc_up_angle(inc/4*(rotate))
            self.b1.inc_up_angle(-inc/4)
            self.b2.inc_up_angle(-inc/2*(rotate))
            self.m1.inc_below_angle(-inc_down)
            self.b2.inc_below_angle(-inc_down)
            self.post_process(2)
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
            self.f1.inc_up_angle(-inc/4)
            self.f2.inc_up_angle(-inc/2*(rotate))
            self.m1.inc_up_angle(-inc/4)
            self.m2.inc_up_angle(inc/4*(rotate))
            self.b1.inc_up_angle(inc/2)
            self.b2.inc_up_angle(inc/4*(rotate))
            self.b1.inc_below_angle(inc_down)
            self.f2.inc_below_angle(inc_down)
            self.post_process(3)
            self.f1.inc_up_angle(-inc/4)
            self.f2.inc_up_angle(-inc/2*(rotate))
            self.m1.inc_up_angle(-inc/4)
            self.m2.inc_up_angle(inc/4*(rotate))
            self.b1.inc_up_angle(inc/2)
            self.b2.inc_up_angle(inc/4*(rotate))
            self.b1.inc_below_angle(-inc_down)
            self.f2.inc_below_angle(-inc_down)
            self.post_process(4)
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
            self.f1.inc_up_angle(inc/2)
            self.f2.inc_up_angle(inc/4*(rotate))
            self.m1.inc_up_angle(-inc/4)
            self.m2.inc_up_angle(-inc/2*(rotate))
            self.b1.inc_up_angle(-inc/4)
            self.b2.inc_up_angle(inc/4*(rotate))
            self.f1.inc_below_angle(inc_down)
            self.m2.inc_below_angle(inc_down)
            self.post_process(5)
            self.f1.inc_up_angle(inc/2)
            self.f2.inc_up_angle(inc/4*(rotate))
            self.m1.inc_up_angle(-inc/4)
            self.m2.inc_up_angle(-inc/2*(rotate))
            self.b1.inc_up_angle(-inc/4)
            self.b2.inc_up_angle(inc/4*(rotate))
            self.f1.inc_below_angle(-inc_down)
            self.m2.inc_below_angle(-inc_down)
            self.post_process(6)
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])

    def simulate_quadruped(self, legs, inc, inc2, time, move = 1, direc = 1):
        print("#### Walking with four legs ####")
        f1 = legs[0]
        f2 = legs[1]
        b1 = legs[2]
        b2 = legs[3]
        f1.inc_up_angle(inc/2)
        f2.inc_up_angle(inc/2)
        b1.inc_up_angle(-inc/6)
        b2.inc_up_angle(inc/6)
        self.post_process(0, True)
        for _ in range(time):
            f1.inc_up_angle(-inc/6)
            f2.inc_up_angle(-inc/2)
            b1.inc_up_angle(-inc/6)
            b2.inc_up_angle(inc/6)
            f2.inc_below_angle(inc2)
            self.post_process(1, True)
            f1.inc_up_angle(-inc/6)
            f2.inc_up_angle(-inc/2)
            b1.inc_up_angle(-inc/6)
            b2.inc_up_angle(inc/6)
            f2.inc_below_angle(-inc2)
            self.post_process(2, True)
            f1.inc_up_angle(-inc/6)
            f2.inc_up_angle(inc/6)
            b1.inc_up_angle(inc/2)
            b2.inc_up_angle(inc/6)
            b1.inc_below_angle(inc2)
            self.post_process(3, True)
            f1.inc_up_angle(-inc/6)
            f2.inc_up_angle(inc/6)
            b1.inc_up_angle(inc/2)
            b2.inc_up_angle(inc/6)
            b1.inc_below_angle(-inc2)
            self.post_process(4, True)
            f1.inc_up_angle(-inc/6)
            f2.inc_up_angle(inc/6)
            b1.inc_up_angle(-inc/6)
            b2.inc_up_angle(-inc/2)
            b2.inc_below_angle(inc2)
            self.post_process(5, True)
            f1.inc_up_angle(-inc/6)
            f2.inc_up_angle(inc/6)
            b1.inc_up_angle(-inc/6)
            b2.inc_up_angle(-inc/2)
            b2.inc_below_angle(-inc2)
            self.post_process(6, True)
            f1.inc_up_angle(inc/2)
            f2.inc_up_angle(inc/6)
            b1.inc_up_angle(-inc/6)
            b2.inc_up_angle(inc/6)
            f1.inc_below_angle(inc2)
            self.post_process(7, True)
            f1.inc_up_angle(inc/2)
            f2.inc_up_angle(inc/6)
            b1.inc_up_angle(-inc/6)
            b2.inc_up_angle(inc/6)
            f1.inc_below_angle(-inc2)
            self.post_process(8, True)



    def simulate_bipod(self, legs, inc, inc2, time, move = 1, direc = 1):
        print("#### Walking with two legs ####")
        rotate = move
        f1 = legs[0]
        f2 = legs[1]
        f1.inc_up_angle(inc/2)
        f2.inc_up_angle(-inc/2*rotate)
        self.post_process(0)
        input()
        for _ in range(time):
            f1.inc_up_angle(-inc)
            f2.inc_up_angle(inc*rotate)
            self.post_process(0)
            f1.inc_below_angle(inc2)
            f2.inc_below_angle(inc2)
            self.post_process(0)
            f1.inc_up_angle(inc/2)
            f2.inc_up_angle(-inc/2*rotate)
            self.post_process(1)
            f1.inc_up_angle(inc/2)
            f2.inc_up_angle(-inc/2*rotate)
            self.post_process(0)
            f1.inc_below_angle(-inc2)
            f2.inc_below_angle(-inc2)
            self.post_process(2)

    def simulate_single(self, leg, inc, inc2, time, move = 1, direc = 1):
        print("#### Walking with one leg ####")
        rotate = move
        f1 = leg
        flag = 1
        for _ in range(time):
            f1.inc_up_angle(-inc*flag)
            self.post_process(0)
            f1.inc_below_angle(inc2)
            self.post_process(0)
            f1.inc_up_angle(inc/2*flag)
            self.post_process(1)
            f1.inc_up_angle(inc/2*flag)
            self.post_process(0)
            f1.inc_below_angle(-inc2)
            self.post_process(2)
            flag*=(-1*rotate)

    def boid_count(self):
        boid1 = 0
        boid2 = 0
        for leg in self.legs:
            if leg.disable == False:
                if leg.boid == 1:
                    boid1+=1
                else:
                    boid2+=1
        return (boid1, boid2)

    def fault(self, arr):
        for leg in arr:
            self.legs[leg]._disable()
            
    def fault_recon(self, arr):
        for leg in arr:
            self.legs[leg]._disable()
        self.reconfigure()

    def recover(self, arr):
        for leg in arr:
            self.legs[leg]._enable()

    def recover_recon(self, arr):
        for leg in arr:
            self.legs[leg]._enable()
        self.reconfigure()
    
    def get_number_legs(self):
        num = 0
        for leg in self.legs:
            if leg.disable == False:
                num = num+1
        return num

    def info(self):
        for (ind, leg) in enumerate(self.legs):
            print(ind, leg.disable, leg.boid)

    def reconfigure(self):
        num = self.get_number_legs()
        if num == 6:
            print("### Robot has Six legs ###")
            # self.simulate_tripod(40, 50, 10, 1, 1)
            self.simulate_ripple(50, 30, 10, -1, 1)
            # do nothing
            # self.initialize()
        elif num == 5:
            print("### Robot has Five legs ###")
            for (index, leg) in enumerate(self.legs):
                if leg.disable == True:
                    remove = (index+3)%6
                    self.fault_recon([remove])
                    return
            #disable one odd leg walk with four legs
        elif num == 4:
                ind1 = -1
                ind2 = -1
                for (index,leg) in enumerate(self.legs):
                    if leg.disable and ind1==-1:
                        ind1 = index
                    elif leg.disable and ind2==-1:
                        ind2 = index
                diff = abs(ind1-ind2)
                print(diff)
                functional = []
                if diff == 3:
                    num = 0
                    while num <= 5:
                        if len(functional) == 0 and self.legs[num].disable == False and self.legs[(num+1)%6].disable == False:
                            print(num)
                            f1 = self.legs[num]
                            f2 = self.legs[(num+1)%6]
                            f1.initialize()
                            f2.initialize()
                            f1.inc_up_angle(-30)
                            f2.inc_up_angle(30)
                            functional.append(f1)
                            functional.append(f2)
                        elif len(functional) > 0 and self.legs[num].disable == False and self.legs[(num+1)%6].disable == False:
                            print(num)
                            b1 = self.legs[(num+1)%6]
                            b2 = self.legs[num]
                            b1.initialize()
                            b2.initialize()
                            b1.inc_up_angle(30)
                            b2.inc_up_angle(-30)
                            functional.append(b1)
                            functional.append(b2)
                            break;
                        num+=1
                    self.post_process(-1, True)
                    input()
                    self.simulate_quadruped(functional, 30, 30, 10)
                elif diff == 2:
                    num = 0
                    while num < 5:
                        if len(functional) == 0 and self.legs[num].disable == False and self.legs[(num+1)%6].disable == False:
                            f1 = self.legs[num]
                            f2 = self.legs[(num+1)%6]
                            f1.inc_up_angle(-10)
                            f2.inc_up_angle(10)
                            functional.append(f1)
                            functional.append(f2)
                        elif self.legs[num].disable == False and self.legs[(num+1)%6].disable == False:
                            b1 = self.legs[(num+1)%6]
                            b2 = self.legs[num]
                            b1.inc_up_angle(10)
                            b2.inc_up_angle(-10)
                            functional.append(b1)
                            functional.append(b2)
                            break;
                        num+=1
                    self.simulate_quadruped(functional, 30, 30, 3)
                elif diff == 1:
                    _ind1 = min(ind1, ind2)
                    _ind2 = max(ind1, ind2)
                    ind1 = _ind1
                    ind2 = _ind2
                    f1 = self.legs[(ind1-2+6)%6]
                    f2 = self.legs[(ind2+2)%6]
                    b1 = self.legs[(ind1-1+6)%6]
                    b2 = self.legs[(ind2+1)%6]
                    b1.set_up_angle(0)
                    b2.set_up_angle(0)
                    f1.set_up_angle(0)
                    f2.set_up_angle(0)
                    b1.inc_up_angle(60)
                    b2.inc_up_angle(-60)
                    input()
                    self.simulate_quadruped([f1, f2, b1, b2], 30, 30, 10)
                #move one bod to another
            # reconfigure according to the position of functional legs
            # self.info()
        elif num == 3:
            print("### Robot has Three legs ###")
            # disable one odd leg, crawl with two legs
            dis = 10000
            ind1 = -1
            ind2 = -1
            functional = self.legs*2
            prev = -1
            for (ind, leg) in enumerate(functional):
                if leg.disable == False and prev==-1:
                    prev = ind
                elif leg.disable == False:
                    if abs(prev-ind%6) < dis:
                        ind1 = prev
                        ind2 = ind%6
                        dis = abs(prev-ind%6)
                    prev = ind%6
            for (ind, leg) in enumerate(self.legs):
                if ind == ind1:
                    leg.change_boid(1)
                elif ind == ind2:
                    leg.change_boid(2)
                elif leg.disable == False:
                    self.fault([ind])
            print("Debug:", ind1, ind2)
            self.reconfigure()
        elif num == 2:
            print("### Robot has Two legs ###")
            functional_legs = []
            for leg in self.legs:
                if leg.disable == False:
                    functional_legs.append(leg)
            functional_legs[0].set_up_angle(0)
            functional_legs[1].set_up_angle(0)
            self.simulate_bipod(functional_legs, 30, 60, 10, -1, 1)   
            # reconfigure according to the position of legs and then crawl
        else:
            print("### Robot has One leg ###")
            # crawl
            for leg in self.legs:
                if leg.disable == False:
                    self.simulate_single(leg, 60, 60, 20, -1)
                    break
        return

    def run(self):
        self.fault([0, 1, 3, 4, 5])
        self.reconfigure()