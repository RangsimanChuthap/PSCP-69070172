""" 3021 — OverlapCircle """
# Better way to do ceiling division
from math import ceil

expand, people = map(int, input().split(" "))
i = 0
while i != people:
    # A circle intersect if AB < R1 + R2

    # Current radius travelled  A = 3.1416 * (radius ^ 2)
    # Radius ^ 2 = Area / 3.1416
    # Radius = sqrroot(Area / 3.1416)

    # Find a time until circle intersect a specific point using formula
    # t = pi(dist^2) / expand_rate where dist = sqr(x^2 + y^2)
    pos_x, pos_y = map(int, input().split(" "))
    dist = (pos_x ** 2) + (pos_y ** 2)
    dist *= 3.1416
    dist = ceil( dist / expand )
    print(dist)

    i += 1
