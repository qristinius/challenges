# Enter your code here. Read input from STDIN. Print output to STDOUT

Test_case = int(input())   #number of test cases

for i in range (Test_case):   #in range of test cases you are bringing new inputs 
    A , set_A = int(input()) , set(map(int, input().split()))   #inputing the length of set_A and as "A" and set itself as "set_A" 
    B , set_B = int(input()) , set(map(int, input().split()))   #inputing the length of set_B and as "B" and set itself as "set_B"

    print(len(set_B.intersection(set_A)) == A)   #checking if the length of intersecion of set_A to set_B equals to
                                                 # the length of set_A (which is variable named "A" and printing result)

