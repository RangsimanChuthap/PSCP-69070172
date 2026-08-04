"""[LEARNING LOGS] BrickBridge"""
smol,big = int(input()), int(input())
target = int(input())

tempbig, tempsmol = 0, 0
subtotal = 0
# Find the max possible number of big brick to be used first.
tempbig = min(big, target // 5)
target -= (tempbig * 5)
subtotal += target
tempsmol = target

# Check if you could actually build by comparing brick used
if tempsmol > smol:
    print(-1)
else:
    print(subtotal)
