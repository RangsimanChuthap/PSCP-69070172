"""Please stop with MATH already, programming isn't all about solving math."""
# Just perform a floor division by 10 and multiplies them back with 10
# to get highest number that is divisible by 10
no = (int(input()) // 10) * 10

txt = ""
# Iterate from highest number to 0 that is divisible by 10, reducing by 10 per step
for i in range(no, -1, -10):
    txt += str(i)
    if i != -1:
        txt += " "

print(txt)
