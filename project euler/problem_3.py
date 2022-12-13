#euler project
#project N3 

num = 600851475143  #the number that i want the prime factors of 
factors_of_num = [] #empty list that i want to add prime factors 

#logics for adding info in lits
while True:
    for i in range (2,int(num)+1):  #the action happens in range of 2 and the presented number 
        if num % i == 0 :
            factors_of_num.append(i) #appends the list the number that is factor of the presented number
            num = num/i              #divide the previous number on it's factor and rewrite it in "num" variable   
            break #breaks the for cycle and restarts for new divided number form first i to up 
    if num == 1: 
        break    #when the lastly divided numbers is equal to 1 the while loop cycle breaks 

print(max(factors_of_num))