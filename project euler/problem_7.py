lst = []
num=1 

while len(lst)<1001:
    for i in range(2, int(num/2)+1):
        if not num % i == 0 :
            lst.append(num)
    num+=1


