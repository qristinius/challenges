# Enter your code here. Read input from STDIN. Print output to STDOUT

total_num_ofcountry = int(input())   #how many countries are there

countries = set()  #empty set to add non repeatable items later 

#adding items to set 
for i in range(total_num_ofcountry):
    country = input()
    countries.add(country)


print(len(countries))  #printing our how mant distinct countries were in the set