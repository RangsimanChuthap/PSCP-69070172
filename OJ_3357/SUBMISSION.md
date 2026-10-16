
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3357 — [LEARNING LOGS] Giraffe
```

OJ submission ID, if submitted:

```text
684593
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
Find the amount of number where adjacent value did not exceed current value
in a dataset.
```

## 3. My First Plan

```
1. Take the amount of number input.

2. Iterate over amount of number of input, store the value inside a list by order.

3. Check first and last number in a list for it's only adjacent value which is to the left and
right respectively, if true add them to the counter

4. Sweep across all number in list that is not first and final number using index, compare
current number to next and previous number using indexing (-1 for prev and +1 for next), if
both number did not exceed current value, add them to count.

5. print count
```

## 4. My Final Approach
```
1. Take the amount of number input.

2. Iterate over amount of number of input, store the value inside a list by order.

3. Check first and last number in a list for it's only adjacent value which is to the left and
right respectively, if true add them to the counter

4. Sweep across all number in list that is not first and final number using index, compare
current number to next and previous number using indexing (-1 for prev and +1 for next), if
both number did not exceed current value, add them to count.

5. print count
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Sampled test case
```
Input:
```
6
5
4
6
9
7
3
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
Test case where there are no number between first and final number.
```
Input:
```
2
1
2
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
All number are equal so value should be 5.
```
Input:
```
5
1
1
1
1
1
```
Expected output:
```
5
```
Actual output:
```
5
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
