
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3227 — [LEARNING LOGS] ไพ่ 44 ใบ
```

OJ submission ID, if submitted:

```text
630210
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
Take card abbreviated face value and suits as input.

return the full card name.
```

## 3. My First Plan

```
Step 1: Take input and .upper().
Step 2: lookup all digit except the last in an dictionary for full form of abbreviation.
if not exist, then add the plain value to the fullname string, then add " of " as saperator.
Step 3: lookup the final digit(card suits) on dictionary as it garanteed to exist and in
dictionary, add the full abbreviated form into display string.
Step 4: print full card name.
```

## 4. My Final Approach
```
Step 1: Take input and .upper().
Step 2: lookup all digit except the last in an dictionary for full form of abbreviation.
if not exist, then add the plain value to the fullname string, then add " of " as saperator.
Step 3: lookup the final digit(card suits) on dictionary as it garanteed to exist and in
dictionary, add the full abbreviated form into display string.
Step 4: print full card name.
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
2 abbreviation of face value and suits
```
Input:
```
AS
```
Expected output:
```
ace of spades
```
Actual output:
```
ace of spades
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
2 digit face value
```
Input:
```
10H
```
Expected output:
```
10 of hearts
```
Actual output:
```
10 of hearts
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
lowercase edge case
```
Input:
```
kc
```
Expected output:
```
king of clubs
```
Actual output:
```
king of clubs
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
