# Enter your code here. Read input from STDIN. Print output to STDOUT
english_subs = int(input())                              #how many students subscribe english
english_sub_students = set(map(int, input().split()))    #1 item is 1 student here 

french_subs = int(input())                                 #how many students subscribe french
french_sub_students = set(map(int, input().split()))       #1 item is 1 student here 

inter = english_sub_students.symmetric_difference(french_sub_students)  #interectioning 2 sets 

print(len(inter))  #printing how many of them have only one magazine subscribed 