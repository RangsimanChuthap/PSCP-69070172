"""COLORSMIX"""
FST,SEC = input(),input()
RES = ""

# Color lookup, 7 possible combination, 4 possible unique result (Orange,Violet,Green,Error)
# Using lookup table to yield 3 possible combination, Error as fallback value
prim = ["Red", "Blue", "Yellow"]
color_lookup = dict({
    "Yellow_Red": "Orange",
    "Blue_Red": "Violet",
    "Yellow_Blue": "Green"
})

# USE COLOR MATCHING PATTERN
if FST not in prim or SEC not in prim:
    RES = "Error"
elif FST == SEC:
    RES = FST
else:
    try:
        RES = color_lookup[f"{FST}_{SEC}"]
    except KeyError:
        try:
            RES = color_lookup[f"{SEC}_{FST}"]
        except KeyError:
            RES = "Error"

print(RES)
