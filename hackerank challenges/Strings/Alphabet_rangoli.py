def print_rangoli(size):
    n = size
    list1 = list(map(chr, range(97,123))) #The lower case letters from a through z are represented by list of 97 to 122
    
    #middle
    middle = list1[n-1::-1] + list1[1:n]
    width = len("-".join(middle)) #width of rangoli
    middle = "-".join(middle)
    
    #upperpart
    for i in range (1,n):
        upper = "-".join( list1[n-1:n-i:-1]+list1[n-i:n])
        upper = upper.center(width,"-")
        print(upper)
    
    #lowerpart
    for i in range (n, 0, -1):
        lower = "-".join( list1[n-1:n-i:-1]+list1[n-i:n])
        lower = lower.center(width,"-")
        print(lower)
        
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

