
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3233 — [LEARNING LOGS] สลากกินแบ่ง
```

OJ submission ID, if submitted:

```text
630344
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```
0-15 min.
```

## 2. My Understanding

```
Take 2 different input in form of "{Char} {num1}{num2}{num3}{num4}{num5}{num6}"

if 2 different input is exact match: return 1000000
else if 2 different input is exact match except the char, return 100000
else if 2 different input has same num4,num5,num6 and char: return 3000
else if 2 different input has same num5,num6 and char: return 2000
else if 2 different input has same num4,num5,num6: return 200
else if 2 different input has same num5,num6: return 100
else if 2 different input has same char: return 20
return 0 if all of the above is not true.
```

## 3. My First Plan

```
Step 1: Take 2 input, remove whitespace saperator.
Step 2: Compare all indexes of the 2 input. jot down the digit indexes with same numerical
value representation in positiob of the current index of 2 different input.
Step 3: Compare the recurrance pattern to dictionary and get the associated value using
tuple type as a key.
Step 4: return associated value from dict, if value doesn't exist in dict, return 0.
```

## 4. My Final Approach
```
Step 1: Take 2 input, remove whitespace saperator.
Step 2: Compare all indexes of the 2 input. jot down the digit indexes with same numerical
value representation in positiob of the current index of 2 different input.
Step 3: Compare the recurrance pattern to dictionary and get the associated value using
tuple type as a key.
Step 4: remove position 2 and 3 from recurrance list and perform lookup again to check if last
3 position match in case of 1 same position value but not other in 1,2 position.
Step 4: return associated value from dict, if value doesn't exist in dict, return 0.
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
2 exact match
```
Input:
```
A 12345
A 12345
```
Expected output:
```
1000000
```
Actual output:
```
1000000
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
1,2,3,5,6 position match which satisfied position5,position6, and position1 match and 
yield 1000, also position 2 match could trip lookup system.
```
Input:
```
A 12345
A 12445
```
Expected output:
```
1000
```
Actual output:
```
1000
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
else case
```
Input:
```
A 11111
Z 45432
```
Expected output:
```
0
```
Actual output:
```
0
```
Result:
```
Pass
```

## 6. AI Use

Did you use AI for this problem?
```
No
```

## 7. Human Help / Collaboration

Did you ask a friend, TA, instructor, or another person for help on this problem?
```
No
```

Who helped you?
```
No one
```

What did they help with?
```text
None
```

What did you still do by yourself?
```text
Everything
```

Did you copy any code from another person?

```text
No
```

## 8. Student Declaration

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | YES |
| I understand my final code. | YES |
| I recorded the real OJ status. | YES |
| I did not copy AI-generated text directly into this file. | YES |
| I did not copy code from another person. | YES |
| If I received human help, I disclosed it in this file. | YES |
| I submitted the final code to the OJ by myself. | YES |
