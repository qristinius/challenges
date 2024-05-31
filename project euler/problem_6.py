import numpy as np
def SumSquareDiff(range_arr=[1,101]):
    """
    Finding Substraction of sum of squared array items and square of summed items
    
    Args:
    range_arr (list) : list containging 2 items firts is lower boundary of range and second is upper boundary on range

    """
    # arranging array
    arr = np.arange(range_arr[0], range_arr[1])

    # returning the value
    return (sum(arr.tolist())**2) - sum((arr**2).tolist())

SumSquareDiff()