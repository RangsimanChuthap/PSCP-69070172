"""Finding euclidian position using 4 positional argument"""
Q1,Q2,P1,P2 = float(input()), float(input()), float(input()), float(input())

DIF = (((Q1 - P1) ** 2) + ((Q2 - P2) ** 2)) ** 0.5

print(DIF)
