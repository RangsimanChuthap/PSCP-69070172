"""Generate a password using provided critera"""
NAME,SUR,AGE = input(),input(),input()

if len(NAME) >= 5 and len (SUR) >= 5:
    # Ef name AND surname has atleast 5 characters, use first 2 letters + final letters of surname
    # + final digit of age
    print(NAME[:2] + SUR[-1] + AGE[-1])
else:
    # Else, use first letter of the name + actual age + final letter of surname
    print(NAME[0] + AGE + SUR[-1])
