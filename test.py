import time
import math
from kit import Kit

i = 0
pin1 = 15 
pin2 = 12
i = 0
kit = Kit()
while i<1:
    j = 1
    while j<12:
        kit.set_angle(j, 90)
        j+=2
    i=i+1