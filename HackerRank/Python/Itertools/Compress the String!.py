from itertools import groupby

string = input()
list1 = []
for num, occurence in groupby(string):
    list1.append((len(list(occurence)), int(num)))

print(*list1)