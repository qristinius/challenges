#euler project
#project N4

new_list = [] #list to add palindromes 

#those two for loops take one number from first loop and substitutes all the numbers of second for loop
for i in range (100,1000):  
    for k in range (100,1000):
        equation = str(i * k) #equation is the result of substitution from 1st and 2nd loop
        if equation[::-1] == equation:     #the reversed number in equation variable should be same as the equation number is 
            new_list.append(int(equation)) #appending equations in new list 

print(max(new_list)) #printing the max number from new list in which are presented the palindromes. 
    



