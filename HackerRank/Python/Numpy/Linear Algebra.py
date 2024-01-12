import numpy as np 

N = int(input())

A = np.array([list(map(float,input().split())) for i in range(N)])

print(np.linalg.det(A))