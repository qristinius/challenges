def Divisible(num):        #checks if it is divisible or not and reutrs bool
    for i in range(1,21):
        if num%i != 0:
            return False
    return True

num = 1 
while True:
    if Divisible(num):  #it stops when 1st division occurs so it's gonna be the smallest
        break
    num+=1   #or it colntinues looping

print(num)
