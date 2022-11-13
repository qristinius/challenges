# Enter your code here. Read input from STDIN. Print output to STDOUT 
length_of_set1 = int(input())

set1 = set(map(int, input().split()))

num_of_other_sets = int(input())

for i in range (num_of_other_sets):
    command = input().split()
    if command[0] == "intersection_update":
        temp_set1 = set(map(int, input().split()))
        set1.intersection_update(temp_set1)
    elif command[0] == 'update':
        temp_set2 = set(map(int, input().split()))
        set1.update(temp_set2)
    elif command[0] == 'symmetric_difference_update':
        temp_set3 = set(map(int, input().split()))
        set1.symmetric_difference_update(temp_set3)
    elif command[0] == 'difference_update':
        temp_set4 = set(map(int, input().split()))
        set1.difference_update(temp_set4)
        
print(sum(set1))
