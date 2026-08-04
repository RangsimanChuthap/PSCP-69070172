"""3072 — A-E-I-O-U"""
# Convert the string into list first, then we use .Count method
strng = list(input().lower())

# Yeah, just count the amount of vowels that appears in word using .count() method
recurse = {
    "a": strng.count("a"),
    "e": strng.count("e"),
    "i": strng.count("i"),
    "o": strng.count("o"),
    "u": strng.count("u")
}

# Now, iterate over all item in recurse dictionary, if the count is atleast 1, display
# the total occurance of that vowels
for item in recurse.items():
    if item[1]:
        print(f"{item[0]} : {item[1]}")
