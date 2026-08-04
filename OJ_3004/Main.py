"""3004 — หาระยะทางระหว่างจุด 3D"""
X1,Y1,Z1 = map(int, input().split(" "))
X2,Y2,Z2 = map(int, input().split(" "))

# Formula
CALC = ((X1 - X2)** 2) + ((Y1 - Y2) ** 2) + ((Z1 - Z2) ** 2)
CALC = CALC ** 0.5

print(f"{CALC:.2f}")
