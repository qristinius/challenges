
elements_in_set = int(input())     #num of element in set
set_itself = set(map(int, input().split()))  #set of integers fro  1-9
number_of_commands = int(input())  #how many time should we do csome operations on set

#logics to discard, remove or pop itms from set
for i in range (number_of_commands):
    commands = input().split()  #picking command and splitting into listseach item has idex 0 and 1 
    
    if commands[0] == "remove":  #0 indexes are the ones that tells what operation we should do on our set
        set_itself.remove(int(commands[1]))  #index with 1 is the item that should be removed or discarded from set (depends on what item sits on the index 0)
    elif commands[0] == "discard":
        set_itself.discard(int(commands[1]))
    else:
        set_itself.pop()  #pop doesn't have exact item or index item cause it removes last item of the set and it always will be different since set changes order of it's own items
        

print(sum(set_itself))  #printing the sum of the set 