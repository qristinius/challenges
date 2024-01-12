import numpy as np 

N,M = input().split()

arr = np.array([list(map(int, input().split())) for i in range(int(N))])

sum_ax0 = np.sum(arr, axis=0)
print(np.prod(sum_ax0))


