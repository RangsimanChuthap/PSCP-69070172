"""3066—เหมือนกันหมด"""
first,sec,third = map(float, [input() for _ in range(3)])

if first < sec < third:
    print("increasing")
elif first > sec > third:
    print("decreasing")
else:
    print("neither")
