"""Special Discount Exclusion??"""
IACTUAL,IPAYCOUNT,IPRICE,ITOTAL = int(input()), int(input()), int(input()), int(input())

# Firstly, Get how many deducted pay by counting how many time can
# total be floor divisible by criteria (How many time count deduction applies)
IDISCOUNT = ITOTAL // IACTUAL
# The remaining numbers get counted whole (Remainder after promotion deduction)
IFRACTURE = ITOTAL % IACTUAL

# The deducted * discounted amount + the whole remainders
IFULLPRICE = ((IDISCOUNT * IPAYCOUNT) + IFRACTURE) * IPRICE

print(IFULLPRICE)
