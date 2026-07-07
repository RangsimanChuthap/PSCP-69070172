"""Embed the received user input into the frame"""
INPUT = input()

#Calculate the frame padding
FRAMELEN = len(INPUT) + 2

print("*" * FRAMELEN)
print("*" + INPUT + "*")
print("*" * FRAMELEN)
