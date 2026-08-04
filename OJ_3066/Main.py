"""3066—เหมือนกันหมด"""
first,sec,third = map(int, [input() for _ in range(3)])

if first == sec == third:
    print("all the same")
elif first != sec and sec != third and first != third:
    print("all different")
else:
    print("neither")
