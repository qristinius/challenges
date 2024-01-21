from itertools import combinations

N = int(input()) #how many letters does string contain
string = input().split()  #N ცალი space separated values 
k = int(input()) #how many of letters should get combined 

combination = list(combinations(string,k))  #all combinations 
wanted = [tup for tup in combination if 'a' in tup]  #combinations with 'a' in it 
print(len(wanted)/len(combination)) #solving for probability 