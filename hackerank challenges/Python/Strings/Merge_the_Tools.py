def merge_the_tools(string, k):
    # your code goes here
    substrings = int(len(string) / k)
    

    for i in range (substrings):
        Full_sub = string[(i * k) : (k * (i + 1))]   #picking substrings from full string as it is divided by k  
        no_repeating_sub  = ""
        
        for i in Full_sub:
            if i not in no_repeating_sub:
                no_repeating_sub += i
                
        print (no_repeating_sub)
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)