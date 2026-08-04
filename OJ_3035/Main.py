""" 3021 — OverlapCircle """
rad, pos_x, pos_y = map(float, input().split(" "))

# A circle intersect if AB < R1 + R2

# A distance between each center point can be found using
# Formula: d^2 = ((x2 - x1)^2) + ((y2-y1)^2)
dist = (pos_x ** 2) + (pos_y ** 2)
dist **= 0.5

# According to many website, a circle intersect if
# r2 - r1 < d =< r2 + r1 or r2 - r1 < d =< r2 + r1
print(pos_x)
if dist < rad:
    print("IN")
elif dist == rad:
    print("ON")
else:
    print("OUT")
