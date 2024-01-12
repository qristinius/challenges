import numpy as np 
np.set_printoptions(legacy='1.13')

element = list(map(float, input().split()))
A = np.array(element)
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))