from itertools import product 

A = list(map(int,input().split()))  #gets space separated values
B = list(map(int,input().split())) #gets space separated values

lst = list(product(A,B))

for i in lst:
    print(i, end=' ')