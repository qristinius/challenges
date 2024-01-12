import numpy as np

N,M = input().split()

A = np.array([list(map(int, input().split())) for i in range(int(N))])
B = np.array([list(map(int, input().split())) for i in range(int(N))])

print(f'{A+B}\n{A-B}\n{A*B}\n{A//B}\n{A%B}\n{A**B}')
