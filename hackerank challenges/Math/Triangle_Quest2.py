#printing triangle of palindromic numbers
#input number must be less than 10 

for i in range(1,int(input())+1): 
    print(((10**i - 1)//9)**2)