"""Pod"""
passenger,line = map(int, input().split(" "))

# Create a reference table on all available lines to store data
lookup = [0] * line

while passenger > 0:
    # Add a data to table according to new arrival line
    new_arrival = int(input())
    lookup[new_arrival - 1] += 1

    passenger -= 1

# Checking everytime a pod could depart is highly demanding
# We will only check how many time a pod could depart after all input

# A port could depart if all line has a member in it, line with lowest amount
# dictate how many depature

depart = min(lookup)
remain = 0
for index in range(len(lookup)):
    lookup[index - 1] -= depart
    remain += lookup[index - 1]

print(remain)
