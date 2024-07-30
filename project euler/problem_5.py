# checks if passed number is divisble by all the numbers in given problem 
def Divisible(num, start=1, end=20):
    for i in range(start,end+1):
        if num%i != 0:
            return False
    return True

num = 1
# if Divisible function returns true it will break and we will get the number else it adds num 1 till we get the
# value we want
while True:
    if Divisible(num):
        break
    num+=1
print(num)