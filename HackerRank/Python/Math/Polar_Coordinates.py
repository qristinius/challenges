# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath as cm

z = complex(input())


for i in cm.polar(z):
    print(i)