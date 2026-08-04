"""DATETIME"""
from datetime import date

D1 = [int(input()) for _ in range(3)]
D2 = [int(input()) for _ in range(3)]

# Use Built in library to convert to date
DATE1 = date(
    year=D1[0],
    month=D1[1],
    day=D1[2]
)

DATE2 = date(
    year=D2[0],
    month=D2[1],
    day=D2[2]
)

# Subtract first person birth date with second person
DELTA = DATE1 - DATE2

# If birth date range differ for no more than 7 days, return 0
if 0 <= abs(DELTA.days) <= 7:
    print("0")
# Else if delta is less than 0, it meant second person birth date
# Is higher than first person (hence, they are born later)
elif DELTA.days > 0:
    print("2")
# Otherwise, if it is positive number, the first person were born later
else:
    print("1")
