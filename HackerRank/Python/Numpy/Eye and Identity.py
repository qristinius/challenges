import numpy as np

np.set_printoptions(legacy='1.13')

N,M = input().split()

ident = np.eye(int(N),int(M), k=0)
print(ident)
