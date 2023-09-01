def count_substring(string, sub_string):
    cnt = 0   #later we wll add it how many times substring occures in string 
    len_sbstr = len(sub_string)
    #checking all the indexs in string 
    for i in range(len(string)):
        if string[i: i + len_sbstr] == sub_string:  #checks if from i idex to i + 3(l3ngth of sbstring) index is equal to substring  
            cnt = cnt+1
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)