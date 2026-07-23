
# Problem Solving Submission


## 1. OJ Information

OJ problem number/title:
```
3036 — [LEARNING LOGS] ปราสาท
```

OJ submission ID, if submitted:
```
565750
```

OJ status:
```
Pass
```

Independent time spent on this problem:

```
1-3 hours
```

## 2. My Understanding

```
Take 1 integer that dictate the index of triangle that stacked up  to create triangular pyramid.

find the shortest available route from current triangle to the top of pyramid ( Index #1 triangle )
if you are only allowedto cross into adjacent triangle that has share a border.
```

## 3. My First Plan

```
Step 1: Take the input
Step 2: Use ceil(sqr(n+1)) to find how many floor pyramid had
Step 3: For every odd floor that is not 1, take + 3 extra step
for every even floor, take only + 1 extra step
Step 4: For an even numbered column relative to parent input, Take 1 less step
Step 5: return print
```


## 4. My Final Approach
```
Step 1: Take the input
Step 2: Use ceil(sqr(n)) to find how many floor pyramid had
Step 3: Calculate the step required by using (floor - 1) * 2
Step 4: For a even numbered triangle index inside an odd numbered row, or odd numbered triangle
index inside an even numbered row, take 1 less step
Step 5: return print
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Sampled Testcase where triangle index is odd-numbered inside an odd numbered row 
```
Input:
```
21
```
Expected output:
```
8
```
Actual output:
```
8
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
Made up Testcase where triangle index is odd-numbered inside an even numbered row 
```
Input:
```
31
```
Expected output:
```
9
```
Actual output:
```
9
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
Made up test case where index is already 1 which should take no step at all
```
Input:
```
1
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
| I did not copy code from another person. | |
| If I received human help, I disclosed it in this file. | YES |
| I submitted the final code to the OJ by myself. | YES |
