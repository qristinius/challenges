import numpy as np

arr = input().strip().split(' ')
array  = np.array(arr, int)
print(np.reshape(array, (3,3)))