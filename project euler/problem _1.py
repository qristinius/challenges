#euler project
#project N1

num =  0 #variable where I save the added numbers

#logics for adding specific numbers to variable 
for i in range(1000):
    if i % 3 == 0 or i % 5 ==0: 
        num += i   #adding and saving chosen numbers to variable 

print(num)






