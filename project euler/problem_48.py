import numpy as np

# creating array with numbers range from 1 to 1000
array_a = np.arange(1,1001, dtype=object)

# powering each item of array with the same item (self powers)
powered_values = np.power(array_a, array_a)

# last 10 digits from sum of self powers
print(str(sum(powered_values.tolist()))[-10:])