import numpy as np
def EvenFibonacci(n=4_000_000):
    """
    Finding sum of even fibonacci numbers with upper boundary
    
    Args:
    n (int) : upper boundary

    """


    # list with first two items of fibonacci numbers
    fib = [0,1]


    # while the last number is less than the upper boundary it will continue adding to list
    while fib[-1] +fib[-2] < n:
        fib.append(fib[-1] + fib[-2])

    # transforming it into array
    fibonaccy_array = np.array(fib)

    # create filter to get even numbers
    mask = (fibonaccy_array % 2 == 0)

    # returning sum of even fibonacci numbers 
    return sum(fibonaccy_array[mask].tolist())

EvenFibonacci()