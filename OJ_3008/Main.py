"""Calculate area of triangle using Hedron's Formula"""
A , B, C = float(input()), float(input()),float(input())

S = (A + B + C) / 2

RESULT = (S * (S - A) * (S - B) * (S - C)) ** 0.5

print(f"{RESULT:.3f}")
