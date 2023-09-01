
N,M = map(int, input().split())#this should be an odd number 

wlcm = "WELCOME"
point = ".|."

#top part 
for i in range(N//2):
    print(( point * ((i *2)+1)).center(M, "-"))
    
#mid part 
print((wlcm.center(M, "-")))

#last part
for i in range(N//2-1, -1, -1):
    print(( point * ((i *2)+1)).center(M, "-"))
    
