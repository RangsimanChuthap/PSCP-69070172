"""SAFE PROBLEM"""
PASS = "H4567"
CHAR,NUM = input(),input()

if CHAR == PASS[0] and NUM == PASS[1:5]:
    print("safe unlocked")
elif CHAR != PASS[0] and NUM == PASS[1:5]:
    print("safe locked - change char")
elif CHAR == PASS[0] and NUM != PASS[1:5]:
    print("safe locked - change digit")
else:
    print("safe locked")
