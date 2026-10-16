
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3296 — [LEARNING LOGS] แปลงดอกไม้
```

OJ submission ID, if submitted:

```text
656678
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```
30-60 min.
```

## 2. My Understanding

```
Take 2 argument in the same string, the N and L

Calculate how many staircase shaped fill can be done if give
```

## 3. My First Plan

```
Step 1: Take 2 input and saperate each with split() and parse using int, store the data
as individual hue inside list.

Step 2: Add 2 hue together and return the average value rounded down.

Step 3: print the resulting gamut.
```

## 4. My Final Approach
```
Step 1: Take 2 input and saperate each with split() and parse using int, store the data
as individual hue inside list.

Step 2: Add 2 hue together and return the average value rounded down.

Step 3: print the resulting gamut.
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
PURE WHITE + PURE DARK ( for testing averaging )
```
Input:
```
0 0 0
255 255 255
```
Expected output:
```
127 127 127
```
Actual output:
```
127 127 127
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
MIXING THE SAME COLOR WHICH SHOULD YIELD SAME COLOR
```
Input:
```
127 127 127
127 127 127
```
Expected output:
```
127 127 127
```
Actual output:
```
127 127 127
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
Mixing 2 different color together
```
Input:
```
43 42 51
66 65 77
```
Expected output:
```
54 53 64
```
Actual output:
```
54 53 64
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
