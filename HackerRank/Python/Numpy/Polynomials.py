import numpy as np 

P = np.array(list(map(float,input().split())))
x = int(input())

print(np.polyval(P,x))

