# Enter your code here. Read input from STDIN. Print output to STDOUT
size_of_group = int(input())       #how many people are in per group
room_for_all = list(map(int, input().split()))      #room numbers but with only 1 numbr for captain's room
individual_room = list(set(room_for_all)) * size_of_group   #room numbers if captain's room also had "size_of_group" number of keys 
difference =  sum(individual_room) - sum(room_for_all)      #finding difference between sums of 2 lists
captains_room  = difference // (size_of_group - 1)     #dividing it by k-1 (in this case "size_of_group" - 1) 
print(captains_room)