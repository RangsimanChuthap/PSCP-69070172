"""DOC"""
RA = int(input())
RB = int(input())
S = input()

EA = 1/(1+(10**((RB-RA)/400)))
EB = 1/(1+(10**((RA-RB)/400)))
if S == "A":
    print(f"{EA:.2f}")
else:
    print(f"{EB:.2f}")
