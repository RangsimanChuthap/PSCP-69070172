
# Problem Solving Submission


## 1. OJ Information

OJ problem number/title:

```text
3058 — [LEARNING LOGS] BrickBridge
```

OJ submission ID, if submitted:

```text
582095
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```
15-30 min
```

## 2. My Understanding

```
Take 3 input: the amount of available big brick, available small brick, and target length.

Calculate the minimum amount of small brick needed to built a bridge with target length,
assuming big brick count as 5 unit and small brick count as 1. If constructing a bridge with
desired length is not possible within the given amount of brick, return - 1 instead.
```

## 3. My First Plan

```
Step 1: Take 3 input

Step 2: Calculate whether a bridge can be build within the scope of given brick by
(5 * bigbrick) + smallbrick, if the condition is false. return -1

Step 3: Calculate brick required by first using maximum amount of big brick possible by
using using the amount of big brick available or the most big brick that can be used by
performing floor division on desired length.

Step 4: Now, the remainders is the amount of small bricks needed.
```


## 4. My Final Approach
```
Step 1: Take 3 input

Step 2: Calculate brick required by first using maximum amount of big brick possible by
using using the amount of big brick available or the most big brick that can be used by
performing floor division on desired length.

Step 3: Now, the remainders is the amount of small bricks needed.

Step 4: Compare the number of small brick used to number initially given. If number of small brick
used exceed initial given brick, return -1 since constructing the bridge within given amount is not
possible.
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
A bridge can be built using small and big brick comnbined.
```
Input:
```
4
1
9
```
Expected output:
```
4
```
Actual output:
```
4
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
A bridge can be fully built using entirely big brick.
```
Input:
```
5
5
20
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

### Test Case 3

Why I chose this case:
```
A bridge cannot be built using given amount of small and big brick
```
Input:
```
1
5
22
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
