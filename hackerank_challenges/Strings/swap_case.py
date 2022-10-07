def swap_case(s):
    sentence = [] #cariei sia
    for letter in s:
        if letter == letter.upper():   #vamowmebt tu aris didi asoebi da tu aris vapataraveb da vamateb cariels sias
            sentence.append(letter.lower())  
        elif letter == letter.lower():  #igives vaketeb patara asoebistvis 
            sentence.append(letter.upper())
        else:
            sentence.append(letter)
    sentence = "".join(sentence)
    return sentence

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)