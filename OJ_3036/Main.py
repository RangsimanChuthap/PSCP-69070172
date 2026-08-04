""" 3036 - [LEARNING LOGS] ปราสาท """
from math import ceil
index = int(input())

# Using the formula foundation = (floor)^2, we can reverse engineering to find how many floor
# pyramid could have, We reverse engineered the formula to be ceil(sqr(n)), which gave us how
# many total floor a pyramid had.
floor = ceil(index ** 0.5)
# Amount of step required is just 2 * (row - 1)
step = 0

# Take 2 more every floor 1 extra, for even numbered column relative to current row index,
# take 1 less step
step = (floor - 1) * 2
if (floor % 2 and not index % 2) or (not floor % 2 and index %2):
    step -= 1

print(step)
