# Enter your code here. Read input from STDIN. Print output to STDOUT
engl_subscribers = int(input())             #how many students subscribe english
roll_num1 = set(map(int, input().split()))  #1 item is 1 student here 

french_subscribers = int(input())  #how many students subscribe french
roll_num2 = set(map(int, input().split())) #1 item is 1 student here 

unite = roll_num1.union(roll_num2)   #uniting 2 sets 
print(len(unite))  #prints how many of students have subscribed at least one 
