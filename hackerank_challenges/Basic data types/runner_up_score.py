
n = int(input())
arr = map(int, input().split()) #separate
arr = list(arr)  #make into list
filtered_winner = [] #later addign info

for i in arr:
    if i != max(arr):  #max point is cut from list
        filtered_winner.append(i)

print(f"{max(filtered_winner)}") #new max is gonna  actually be the second max score 