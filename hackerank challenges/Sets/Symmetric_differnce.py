# Enter your code here. Read input from STDIN. Print output to STDOUT
size1, firstnums = (int(input()), map(int, input().split())) #size of first set and set numbers (placed inside list)
size2, secnums = (int(input()), map(int, input().split()))  #size of second set and set numbers  (placed inside list)

#transfroming into set
Firstnums = set(firstnums)  
Secnums = set(secnums)

#finding only difference between two sets
differenciate = Firstnums.symmetric_difference(Secnums)

lst = list(differenciate) #making into list
lst.sort() #sorting

output = ("\n".join(map(str,lst)))  #joining srted list as their items are strings(making this thing with map()) and writing them in new line 

print(output)