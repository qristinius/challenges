
import numpy as np
num = np.array([i for i in range(1,101)])
sum_of_squares = sum(num**2)
square_of_sum = (sum(num))**2

print(square_of_sum-sum_of_squares)
