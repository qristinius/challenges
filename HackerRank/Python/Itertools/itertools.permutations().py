from itertools import permutations

S,k = input().split()  #gets 2 space separated values 1 is saved in S other one is saved in k 

permutation_lst = sorted(list(permutations(S,int(k))))

items = [''.join(i) for i in permutation_lst]
for i in items:
    print(i)