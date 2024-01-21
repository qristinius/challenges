from itertools import combinations_with_replacement

S,k = input().split()

sort = sorted(S)

for comb in combinations_with_replacement(sort, int(k)):
    print(''.join(comb))