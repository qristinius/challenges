fib = [1,1]

# while the length of the last number of fibonacci sequence is 1000 the loop continues and we find the index of it
while len(str(fib[-1]))!=1000:
    fib.append(fib[-1] + fib[-2])

print(f'Length of sequence:{len(fib)}, Index of 1000 digits number:{fib.index(max(fib))}')