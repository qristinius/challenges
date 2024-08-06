import math as m

def d(n):
    """
    Finding sum of proper divisors

    Args:
        n (int) : number of which divisors we are searching
    """
    num = 1
    # iterating over sqrt and then adding the other part of multiple it gives us (shortening for loop)
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            num+=i
            j = n//i
            if j > i:
                num +=j
    return num

# this takes much more time
# amicable_nums  = set()
# for i in range(1,10000):
#     for j in range(i+1,10000):
#         if d(i) == j and d(j) == i:
#             amicable_nums.update([i, j])

# sum(amicable_nums)


# optimal version
answer = []

# iterating over numbers to find sum of amicable numbers
for i in range (1,10_000):
    # denoting sum of proper divisors for each number
    amicable1  = d(i)

    # denoting sum of proper divisors for amicable1
    amicable2 = d(amicable1)

    # logical boundaries:
    if i == amicable2 and amicable2 != amicable1:
        answer.append(i)

sum(answer)