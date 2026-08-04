""" 3024 — [LEARNING LOGS] SurprisingVote """
SUBTOTAL, HIGHEST = float(input()), float(input())

# Calculate the possible rating pools of 2 non-top raters
# the pool is (MIDDLE RATING + LOWEST RATING)
POOL = SUBTOTAL - HIGHEST

# Find the maximum score range between middle and lowest voter.
# Lowest possible rating can be found by subtracting a pool with
# higest possible rating. This is due to the fact that we knew that
# pool are result of middle + lowest rating, the greater the middle
# rating are, the lower the lowest rating it can be.

# Start by determining maximum rating of middle vote, we will
# start with by defining that the highest rating is the total amount
# in the pool that doesn't exceeds highest rating.
MAX_DELTA = min(POOL,HIGHEST)

# we will then subtract the pool with highest possible middle rating
# to obtain lowest possible rating.
MAX_DELTA = [MAX_DELTA, (POOL - MAX_DELTA)]

# Then, we will compare a highest rating with lowest possible rating.
if HIGHEST - MAX_DELTA[1] > 2:
    print("Surprising")
else:
    print("Not surprising")
