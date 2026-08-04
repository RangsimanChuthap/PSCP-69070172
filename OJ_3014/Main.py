"""3014 - Milk"""
price,cap,free,budget = int(input()), int(input()), int(input()), int(input())
amount = 0

if not cap:
    # If cap is 0, skip free part entirely, you get budget // price bottles
    print(budget // price)
else:
    # We will define pattern by saperating each one at when accumulate cap reach exchangable amount
    # First, get the total possible full pattern repeat by dividing possible can that could be
    # afford with repeating amount of pattern
    afford = budget // price
    repeat = afford // cap

    if repeat > 0:
        # The first pattern is cap long
        amount += cap + free
        afford -= cap

        # Subsequence repeat is cap - 1 long because free bottle grant extra cap
        repeat = afford // (cap - free)
        amount += ((cap - free) * repeat) + (free * repeat)
        afford -= ((cap - free) * repeat)

        # For Remainders, use mudulo to find availble left. the leftover get no extra surplus
    amount += afford % cap

    print(amount)
