
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3299 — [LEARNING LOGS] แปลงดอกไม้
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
30 min.
```

## 2. My Understanding

```
Take 2 argument in single string: n and l.

find how many staircase layer of the width and height n can filled in given l unit
when moving from staircase to the next you don't need to refill all previous staircase. 
```

## 3. My First Plan

```
Step 1: Take 2 input and saperate each with split() and parse using int, store the data.

Step 2: Find how many unit does stair occupy using (n+1 * n)/2 as variable m

Step 3: Define the count as 0 

Step 4: Iterate while l is not equal or lesser than 0:

Step 4.1: Subtract l with m

Step 4.2: Add n*2 to m as this is the change in row size per staircase.

Step 4.3: If l is 0 or less. meant the unit has been depleted, break. if not add 1 to the count

Step 5: print(count)
```

## 4. My Final Approach
```
Step 1: Take 2 input and saperate each with split() and parse using int, store the data.

Step 2: Find how many unit does stair occupy using (n+1 * n)/2 as variable m

Step 3: Define the count as 0 

Step 4: Iterate while l is not equal or lesser than 0:

Step 4.1: Subtract l with m

Step 4.2: Add n*2 to m as this is the change in row size per staircase.

Step 4.3: If l is 0 or less. meant the unit has been depleted, break. if not add 1 to the count

Step 5: print(count)
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Sample
```
Input:
```
1 17
```
Expected output:
```
6
```
Actual output:
```
6
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
Sample
```
Input:
```
3 29
```
Expected output:
```
3
```
Actual output:
```
3
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
1 1 edge case
```
Input:
```
1 1
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
