import math

class Utils:
    def __init__(self):
        #nothing
    
    @staticmethod
    def line(p1, p2):
        m = (p2[1]-p1[1])/(p2[0]-p1[0])
        c = 0
        return (m, c)

    @staticmethod
    def angle_between(m1, m2):
        return 90-abs(math.atan((m1-m2)/(1+m1*m2)))