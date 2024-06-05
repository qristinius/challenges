import numpy as np
def Distinctpowers(start_a, finish_a, start_b, finish_b):
    """
    Finding Distinct powers of given numbers at a given range of powers

    Args:
    start_a (int) : starting numbers of array a
    finish_a (int) : ending numbers of array a
    start_b (int) : starting numbers of array b
    finish_b (int) : ending numbers of array b
    """

    # creating empty list
    empty_list = []

    # creating arrays with given parameters
    array_a = np.arange(start_a,finish_a+1, dtype=object)
    array_b = np.arange(start_b,finish_b+1, dtype=object)

    # iterating over second array taking its values and powering first array with this number and extending the empty list we previously made, aftr that we save it as a set to remove duplicates.
    for i in array_b:
        empty_list.extend(array_a**i)
    return len(set(empty_list))


Distinctpowers(start_a=2,finish_a=100,start_b=2,finish_b=100)

#%%
