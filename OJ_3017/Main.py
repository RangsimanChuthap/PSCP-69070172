"""Bills"""
BASE = int(input())

# Labour cost is 10% of base price, max 1000, min 50
LABOUR = max(50, BASE * 0.1)
LABOUR = min(1000, LABOUR)

BASE = BASE + LABOUR
BASE = BASE + (BASE * 0.07)

print(f"{BASE:.2f}")
