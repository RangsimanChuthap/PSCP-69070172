""" 3033 - กระดาษห่อของขวัญ"""
rad, height, offset = map(float, input().split(" "))

#Width = 2 * radius + height
area_w = 2 * rad + height
# Height = (2 * Pi * Radius) + Offset
area_h = 2 * rad * 3.14 + offset

print(f"{area_w:.2f} {area_h:.2f}")
