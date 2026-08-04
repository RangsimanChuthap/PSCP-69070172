"""COKE"""
PRC,CAP,DSC,AMT = int(input()),int(input()),int(input()),int(input())
LOW = 0
# If doesn't accept cap or amount less than discount cap, return full price.
if AMT < CAP or not CAP:
    LOW = PRC * AMT
else:
    # The first iteration of bottle cap require 3 full price bottles before obtaining discount
    AVAILABLE = AMT - CAP - 1
    LOW += CAP * PRC + DSC

    # Then, for every subsequence loop will require 1 cap bottle to
    # iterate a discount.

    # First We calculate how many discount cycle that can be triggered by
    # diving purchase amount(calculated after first discount cycle )
    # with [ cap required - 1 ]
    CYCLE = AVAILABLE // (CAP)

    # The total cycle dictate how many discount that is redeemable
    # For every x cycle, 1 discount is applied.
    LOW += (CYCLE * DSC)

    # A remainders will have to be paid in full price.
    REMAIN = AVAILABLE - CYCLE
    LOW += (REMAIN * PRC)

print(LOW)
