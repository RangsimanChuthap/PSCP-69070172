"""RECTANGLE"""
posx1,posy1,wdt1,hgt1 = map(int, input().split(" "))
posx2,posy2,wdt2,hgt2 = map(int, input().split(" "))

# Position composition [pointx1,pointy1, pointx2, pointy2]
# A rectangle can be constructed easily by knowing 2 point.
constructor_sq1 = [posx1, posy1, posx1 + wdt1, posy1 + hgt1]
constructor_sq2 = [posx2, posy2, posx2 + wdt2, posy2 + hgt2]

# Safeguarding first. if neither constructor satisfies that start position (in any one dimention)
# Is lesser than a end position then it didn't intersect at all

# This for if square 2 is more right than a square 1
if ((constructor_sq1[2] < constructor_sq2[0] and \
constructor_sq1[0] < constructor_sq2[2]) or \
(constructor_sq1[1] < constructor_sq2[3] and \
constructor_sq1[3] < constructor_sq2[1])):
    INTERSECT_AREA = 0

# This is for square 1 more right than square 2
elif (((constructor_sq2[2] < constructor_sq1[0] and \
constructor_sq2[0] < constructor_sq1[2]) or \
(constructor_sq2[1] < constructor_sq1[3] and \
constructor_sq2[3] < constructor_sq1[1]))) :
    INTERSECT_AREA = 0

# If we are certain that this do intersect. calculate how much intersection
# Finding intersection is min(Position_finale) - max(Position_beginning)
else:
    INTERSECT = []
    INTERSECT.append(min(constructor_sq1[2], constructor_sq2[2]) -
        max(constructor_sq1[0], constructor_sq2[0]))

    INTERSECT.append(min(constructor_sq1[3], constructor_sq2[3]) -
        max(constructor_sq1[1], constructor_sq2[1]))

    INTERSECT_AREA = INTERSECT[0] * INTERSECT[1]

if not INTERSECT_AREA:
    print("no overlapping")
else:
    print(INTERSECT_AREA)
