import numpy as np 


N,M = input().split()

arr = []
for i in range(int(N)):
    arr_item = arr.append(np.array(list(map(int,input().split()))))

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(round(np.std(arr),11))
