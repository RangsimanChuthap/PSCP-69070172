
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
1-2 hours.
```

## 2. My Understanding

```
Take input X, Y

Starting from 0, add X and then subtract X by 2 until X is greater than or equal to Y or X
is equal 0 or less. count how many time X need to be added until it reach Y. If can't reach
Y with given X number. return -1
```

## 3. My First Plan

```
Step 1: Take input X, Y as int
Step 2: Initialize number store variable = 0
Step 3: Check if X =< Y: if so, return 1 early.
Step 4: Iterate while X is greater than 2, add X to number store and subtract X by 2.
if X is greater than or equal to Y, set X = -1 to end loop. If entire iteration has been exhausted
and X is not greater than or equal to Y, return -1
```

## 4. My Final Approach
```
Step 1: Take input X, Y as int
Step 2: Initialize number store variable = 0
Step 3: Iterate while X is greater than 0, add X to number store and subtract X by 2.
if X is greater than or equal to Y, set X = -1 to end loop. If entire iteration has been exhausted
and X is not greater than or equal to Y, return -1
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
sample non edge case
```
Input:
```
6 10
```
Expected output:
```
2
```
Actual output:
```
2
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
edge case of starting jump is greater than end
```
Input:
```
9 7
```
Expected output:
```
1
```
Actual output:
```
1
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
can't reach end with given X
```
Input:
```
5 12
```
Expected output:
```
-1
```
Actual output:
```
-1
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
