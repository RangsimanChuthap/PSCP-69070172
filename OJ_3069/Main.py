"""ราศึ"""
date,month = map(int, (input() for _ in range(2)))

# Constellation lookup table (name: [(startMM, startDD),(endMM, endDD)]);
CONST_LOOKUP = {
    "aquarius":     [(1,20),(2,18)],
    "pisces":       [(2,19),(3,20)],
    "aries":        [(3,21),(4,19)],
    "taurus":       [(4,20),(5,20)],
    "gemini":       [(5,21),(6,21)],
    "cancer":       [(6,22),(7,22)],
    "leo":          [(7,23),(8,22)],
    "virgo":        [(8,23),(9,22)],
    "libra":        [(9,23),(10,23)],
    "scorpio":      [(10,24),(11,21)],
    "sagittarius":  [(11,22),(12,21)],
    "capricorn":    [(1,1),(12,22)]
}

absmonthdate = (month, date)

for item in CONST_LOOKUP.items():
    if item[1][0] <= absmonthdate <= item[1][1]:
        print(item[0])
        break
