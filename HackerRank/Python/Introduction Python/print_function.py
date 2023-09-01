n = int(input())

lst = []

for i in range(1, n+1) :
    lst.append(i)
new = "".join(map(str,lst))
print(new)