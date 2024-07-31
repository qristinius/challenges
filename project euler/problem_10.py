# list where we save prime numbers
lstprimes = []

# first iterating over given value excluding 1 cause it isn't prime
for num in range(2_000_000, 1, -1):
    # variable that determines if we include number as prime or not
    include = True
    # iterating over divisor for each numebr
    for divisor in range(2, int(m.sqrt(num)) + 1):

        # if number is divided by any of divisor it gets excluded
        if num % divisor == 0:
            include = False
            break
    # if include is True then we append that number for which is include True in previusly made list
    if include:
        lstprimes.append(num)

# printing sum of list
print(sum(lstprimes))