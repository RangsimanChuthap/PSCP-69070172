"""3065 — ตัวเลขโรมันแบบง่าย"""
num = int(input())
temp = ""

if num < 0:
    print("Error : Please input positive number")
elif not num or num > 9:
    print("Error : Out of range")
else:
    # Check if it could be replaced by I(Notation) by finding remainder of num + 1 / 5
    if not (num + 1) % 5:
        temp += "I"
        if num + 1 == 5:
            temp += "V"
        elif num + 1 == 10:
            temp += "X"
    # If not replacle by I(Notation)
    else:
        if num // 5:
            temp += "V"
            num -= 5
        temp += ("I" * num)

print(temp)
