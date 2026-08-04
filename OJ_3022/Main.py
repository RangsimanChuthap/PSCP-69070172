""" 3022 — [LEARNING LOGS] Temperature"""
TEMP,UNIT,TARGET = float(input()),input(),input()
TERM = False

# Bypass the calculation if current unit is same as target
if UNIT == TARGET:
    print(f"{TEMP:.2f}")
    TERM = True
# If the unit is not celsius, turn them into celsius for easier
# calculation
if UNIT != "C":
    match UNIT:
        case "K":
            TEMP -= 273.15
        case "F":
            TEMP = ((TEMP -32 ) / 9) * 5
        case "R":
            TEMP = ((TEMP / 9) * 5) -273.15

# Convert to the respective unit
match TARGET:
    case "C":
        pass
    case "K":
        TEMP += 273.15
    case "F":
        TEMP = ((TEMP * 9) / 5) + 32
    case "R":
        TEMP = ((TEMP + 273.15) * 9) / 5

if not TERM:
    print(f"{TEMP:.2f}")
