from itertools import permutations

S,k = input().split()

permutation_lst = sorted(list(permutations(S,int(k))))

items = [''.join(i) for i in permutation_lst]
for i in items:
    print(i)