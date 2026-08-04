""" 3025 — [LEARNING LOGS] Season """
MTH, DAY = int(input()), int(input())
SEASON = ["winter", "spring", "summer", "fall", "winter"]

# Pep-8 analyser will complain that == 0 can be replaced by not
if MTH > 12:
    MTH %= 12

SEASON_INDEX = (MTH - 1) // 3
if not MTH % 3:
    if DAY >= 21:
        SEASON_INDEX += 1

print(SEASON[SEASON_INDEX])
