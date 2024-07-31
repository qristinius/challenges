def nthprime(nthnum):
    # list made from only 1st prime number later will get added
    primelist = [2]

    # first prime number
    prime = 2

    # ensuring that we get that number of answers as we want
    while len(primelist) < nthnum:

        # increasing value of prime by one for each loop
        prime+=1

        # number that will help us find primes
        num = 0

        # iterating over integered square roots of primes + 1 to include last number too.
        # that is because when factorising after we cross square root number we get same multiples of numbers
        # like 2*12,12*2
        for i in range(2, int(m.sqrt(prime)+1)):

            # if value of prime variable is divided by any of those numbers then it isn't prime number
            # so we just increase num value by 1
            if prime%i == 0:
                num +=1
        # if previous if logic wasn't satisfied it means num value stays 0
        # and it is prime number so we add that number in our very first list
        if num == 0:
            primelist.append(prime)
    # print lastest item from list
    print(primelist[-1])

nthprime(10001)
