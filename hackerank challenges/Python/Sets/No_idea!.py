# Enter your code here. Read input from STDIN. Print output to STDOUT
whole_array , items_in_set = map(int, input().split())   

arr = list(map(int, input().split())) #list of arr

#checking point items
Adding_happiness = map(int, input().split())
Minus_happiness = map(int, input().split())

#creating sets to add and take happiness
Adding_happines  = set(Adding_happiness)
Minus_happiness = set(Minus_happiness)

Happiness = 0

#is there is an item in arr (list) and also in Adding_happines(set) adds 1point to happiness
#if there's an item in arr(list) and also in Minus_happiness(set) takes 1 point from happiness
for i in arr:
    if i in Adding_happines:
        Happiness += 1
    elif i in Minus_happiness:
        Happiness -= 1
        
print(Happiness)


#wanna discus why dis code doesn't work for all cases
""" 
# Enter your code here. Read input from STDIN. Print output to STDOUT
whole_array , items_in_set = map(int, input().split())

arr = list(map(int, input().split()))

Adding_happiness = map(int, input().split())
Minus_happiness = map(int, input().split())

Adding_happines  = set(Adding_happiness)
Minus_happiness = set(Minus_happiness)

add = Adding_happines.intersection(arr)
minus = Minus_happiness.intersection(arr)

result = len(add) - len(minus)

print(result) """