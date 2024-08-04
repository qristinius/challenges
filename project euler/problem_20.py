import math as m

def sum_of_factorial(num):
    """
    Finding sum of num's factorial's each numbers

    Args:
        num (int) : number which factorial's sum of numbers we are searching
    """
    fact = m.factorial(num)
    lstofnum = [int(i) for i in str(fact)]
    return sum(lstofnum)

sum_of_factorial(100)