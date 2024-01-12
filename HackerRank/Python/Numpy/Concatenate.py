import numpy as np 

N,M,P = input().split()

arr1 = np.array([list(map(int, input().split())) for i in range(int(N))])
arr2 = np.array([list(map(int, input().split())) for i in range(int(M))])

print(np.concatenate((arr1, arr2), axis=0))