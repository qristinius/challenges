# Enter your code here. Read input from STDIN. Print output to STDOUT
import math as m

AB = int(input())  #one leg of triangle
BC = int(input())  #second leg of triangle
AC = m.sqrt(AB**2 + BC**2) #hypotenuse
MC = AC / 2  #half of hypotenuse
BCA = m.atan(AB / BC)  #BCA angle 
MB = m.sqrt( (BC**2 + MC**2) - 2 * BC * MC * m.cos(BCA) )  #MB side from cosine theory 

theta_rad = m.acos( (BC**2 + MC**2 - MC**2) / (2*BC*MC) )  #counting theta by using cosine theory 

theta_degree =int(round(m.degrees(theta_rad),0))  #theta in degrees 
degree_sign = u'\N{DEGREE SIGN}' 

print(theta_degree,degree_sign, sep="")
