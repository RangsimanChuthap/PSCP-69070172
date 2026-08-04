""" 3021 — OverlapCircle """
POSX1,POSY1,RAD1 = int(input()),int(input()),int(input())
POSX2,POSY2,RAD2 = int(input()), int(input()), int(input())

# IHATEMATHEMATICSIHATEMATHEMATICSIHATEMATHEMATICS
# A circle intersect if AB < R1 + R2

# A distance between each center point can be found using
# Formula: d^2 = ((x2 - x1)^2) + ((y2-y1)^2)
DIST = ((POSX2 - POSX1) ** 2) + ((POSY2 - POSY1) ** 2)
# Square the DIST to get d^1
DIST **= 0.5

# According to many website, a circle intersect if
# r2 - r1 < d =< r2 + r1 or r2 - r1 < d =< r2 + r1
if RAD2 - RAD1 < DIST <= RAD2 + RAD1 or RAD1 - RAD2 < DIST <= RAD2 + RAD1:
    print("overlapping")
else:
    print("no overlapping")
