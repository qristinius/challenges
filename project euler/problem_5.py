#euler project
#project N5
import random
from numpy import number
import numpy as np 

ganayofebi = []
while True:
    num = random.choice(range(1,100000))
    for i in range(1,21):
        a = num % i
        if a == 0:
            ganayofebi.append(num)
    else:
        break

print(ganayofebi)