if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()  
        score = float(input())
        lst.append([name, score])  #saxelebs da qulebs vamateb listebad listshi 
        
    score = [float(i[1]) for i in lst]    # qulebis lists vqmni (patara listebis indeqsit vigeb)
    second_low = []

    #meore yvelaze dabali qulis povna 
    for i in score:
        if i!= min(score):          
            second_low.append(i)
        
    second_low =  min(second_low)
    
    #saxelebis ppovna qulebis mixedvit 
    name = []
    for i in lst:
        if float(i[1]) == second_low:
            name.append(i[0])
    name.sort()
    print(*name, sep = "\n")  
