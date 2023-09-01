def minion_game(string):
    # your code goes here
    length = len(s)
    vowels = "AEIOU"
    kevin_vow = 0
    stuart_cons = 0

    for i in range(length):
        if s[i] in vowels:
            kevin_vow += length - i     #length - i because to check every new indexes possible numbers of words 
        else:
            stuart_cons += length - i

    if kevin_vow > stuart_cons:
        print("Kevin", kevin_vow)
    elif kevin_vow < stuart_cons:
        print("Stuart", stuart_cons)
    else : 
        print("Draw")

        
    print(kevin_vow)
    print(stuart_cons)
    
if __name__ == '__main__':
    s = input().upper()
    minion_game(s)