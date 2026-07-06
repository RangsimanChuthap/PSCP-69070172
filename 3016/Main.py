"""Find the last digit of 7 power user input"""
POWR = int(input())

# Calculating result individually would not be productive
# Using the trick that 7 power to anything will always yield
# 7,9,3,1 repeatedly

# First, Find what sequence is the number currently in
SUBCOUNT = POWR % 4

match SUBCOUNT:
    case 0:
        print("1")
    case 1:
        print("7")
    case 2:
        print("9")
    case 3:
        print("3")
