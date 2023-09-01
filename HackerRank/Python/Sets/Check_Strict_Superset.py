# Enter your code here. Read input from STDIN. Print output to STDOUT
main_set = set(map(int, input().split()))     
num_of_othersets = int(input())               
union_of_other_sets = set()    #set that we will add all other sets later
for i in range (num_of_othersets):
    new_sets = set(map(int, input().split()))  
    union_of_other_sets = union_of_other_sets.union(new_sets)  #unioning new sets as 1 set

intersection  = main_set.intersection(union_of_other_sets)  

print(len(union_of_other_sets) == len(intersection))   #checking if there's at least one element in union of new sets that does not exist in main set







#code that didn't work for all cases
""" # Enter your code here. Read input from STDIN. Print output to STDOUT
main_set = set(map(int, input().split()))
num_of_othersets = int(input())

finish_result = 0
for i in range (num_of_othersets):
    checkset = set(map(int, input().split()))
    
    checker = (checkset.difference(main_set))
    
    if checker == True:
        finish_result += 1
    else:
        a = 5
    
if finish_result == num_of_othersets:
    print("True")
else:
    print(False) """
        