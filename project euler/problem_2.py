#euler project
#project N2 



list_fibonacci = [1 , 1] #creating list with first numbers of fibonacci to add nect numbers later
even_numbers = []  #creating an empty list to add even numbers and then sum all of it for last answer 

#logics for fibonacci sequence
#when the sum of last two numbers exceed the 4e6 the while loop stops 
while (list_fibonacci[-1] + list_fibonacci[-2]) < 4e6:
    new_num = list_fibonacci[-1] + list_fibonacci[-2]  #new number is new nuber for fibonacci sequene this means adding last two numbers of the list 
    list_fibonacci.append(new_num)  #adding new fibonacci numbers in list for fibonacci numbers    

#logics for even numbers in fibonacci sequence 
for i in list_fibonacci:
    if i % 2 == 1:
        even_numbers.append(i)  #adding even numbers to new list for even numbers that was created before 

print(sum(even_numbers))





