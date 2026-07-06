"""Special Discount Exclusion??"""
IACTUAL,IPAYCOUNT,IPRICE,ITOTAL = int(input()), int(input()), int(input()), int(input())

# Get Total Discounted pay by finding how many time the total satisfied criteria
IDISCOUNT = ITOTAL // IACTUAL
# The remaining numbers get counted whole (Remainder after promotion deduction)
IFRACTURE = ITOTAL % IACTUAL

# The deducted * discounted amount + the whole remainders
IFULLPRICE = ((IDISCOUNT * IPAYCOUNT) + IFRACTURE) * IPRICE

print(IFULLPRICE)
