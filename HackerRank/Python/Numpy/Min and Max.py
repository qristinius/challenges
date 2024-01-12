import numpy as np

N,M = input().split()


mins_list = []
for i in range(int(N)):
    arr = np.array(list(map(int,input().split())))
    mins = mins_list.append(np.min(arr))
    
print(max(mins_list))
