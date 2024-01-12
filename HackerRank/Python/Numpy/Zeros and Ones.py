import numpy as np 

size = list(map(int,input().split()))

zeros = np.zeros(size, dtype=int)
ones = np.ones(size, dtype=int)

print(zeros)
print(ones)