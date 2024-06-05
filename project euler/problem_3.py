# the number that I want the prime factors of
num = 600851475143

# empty list that I want to add prime factors
factors_of_num = []

#logics for adding info in list
while True:
    # the action happens in range of 2 and the presented number
    for i in range (2,int(num)+1):
        if num % i == 0 :
            # appends the list the number that is factor of the presented number
            factors_of_num.append(i)
            # divide the previous number on it's factor and rewrite it in "num" variable
            num = num/i
            # breaks the for cycle and restarts for new divided number form first i to up
            break
    if num == 1:
        # when the lastly divided numbers is equal to 1 the while loop cycle breaks
        break

print(max(factors_of_num))