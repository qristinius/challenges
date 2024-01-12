import numpy as np 

N,M =input().strip().split()


arr = np.array([list(map(int,input().split())) for i in range(int(N))])
print(np.transpose(arr))
print(arr.flatten())