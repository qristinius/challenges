if __name__ == '__main__':
    n = int(input())
    lst = []
    while n !=0 :
        n=n-1
        lst.append(n)
    lst.reverse()
    
    for i in lst:
        print(i**2)
