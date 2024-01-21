from itertools import combinations

s, k = input().split()  #gets 2 space separated values 1 is saved in S other one is saved in k 
letters = sorted(s)  #sorts s alphabetically 

for i in range(1, int(k) + 1):
    for combination in combinations(letters, i):
        print("".join(combination))