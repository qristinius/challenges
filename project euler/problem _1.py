import numpy as np
def SumOfMultiples(startingpoint = 1, endingpoint = 1000, multiplier1 = 3, multiplier2 = 5 ):
    """
    Finding sum of multiples of 3 or 5

    Args:
    startingpoint (int) : starting point of the range we are searching sum 
    endingpoint (int) : ending point of the range we are searching sum 
    multiplier1 (int) : first multiplier
    multiplier2 (int) : second multiplier
    
    """

    # creating matrix with numbers 
    matrix = np.arange(startingpoint, endingpoint)

    # filter
    mask = (matrix % multiplier1 == 0) | (matrix % multiplier2 == 0)

    # returning filtered matrix sum, firstly converting it in list to avoid overloading numpy
    return sum(matrix[mask].tolist())

SumOfMultiples(1,1000,3,5)