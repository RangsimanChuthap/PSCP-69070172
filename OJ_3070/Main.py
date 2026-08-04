"""3070-นับเลขคู่และเลขคี่"""
test = [int(input()) for _ in range(3)]
odd,evn = 0,0

for i in range(len(test)):
    if test[i - 1] % 2:
        odd += 1
    else:
        evn += 1

print(evn)
print(odd)
