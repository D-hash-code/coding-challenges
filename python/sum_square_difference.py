https://projecteuler.net/problem=6

import numpy as np

square_then_sum = np.sum(np.square(np.arange(101)))

sum_then_square = np.sum(np.arange(101))

sum_then_square = sum_then_square * sum_then_square

print("answer: ", sum_then_square - square_then_sum)
