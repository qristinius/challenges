if __name__ == '__main__':
    N = int(input())
    newlst = []
    
    for i in range(N):
        x = input().split()   #splitting to get info with using of indexes (eg.insert 0 5 --> [insert, 0 , 5])
        if x[0] == "insert":
            newlst.insert(int(x[1]), int(x[2]))
        elif x[0] == "print":
            print(newlst)
        elif x[0] == "remove":
            newlst.remove(int(x[1]))
        elif x[0] == "append":
            newlst.append(int(x[1]))
        elif x[0] == "sort":
            newlst.sort()
        elif x[0] == "pop":
            newlst.pop()
        elif x[0] == "reverse":
            newlst.reverse()