
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3381 — [LEARNING LOGS] Point Sorting
```

OJ submission ID, if submitted:

```text
684930
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```
20 min.
```

## 2. My Understanding

```
given n set of a pair of value: x and y, sort each pair using value of x + y as a key from
least to most. if there present multiple pairs with same x + y value, the pair with greater y
came first in order.
```

## 3. My First Plan

```
1. Take and iterate over number of dataset

2. In each iteration per dataset, take value n as number of pairs, for n input, take a data
as pair of x and y position saperated by whitespace, after finishing receiving input, sort
the dataset using .sort() with tuple and reversed = True, first value as primary sorting key which is x + y,
and second is y *-1 as fallback key, multiplied by -1 to reverse sorting direction as higher the
negative, lower the value hence make them came first.

3. Display sort result per dataset.
```

## 4. My Final Approach
```
1. Take and iterate over number of dataset

2. In each iteration per dataset, take value n as number of pairs, for n input, take a data
as pair of x and y position saperated by whitespace, after finishing receiving input, sort
the dataset using .sort() with tuple and reversed = True, first value as primary sorting key which is x + y,
and second is y *-1 as fallback key, multiplied by -1 to reverse sorting direction as higher the
negative, lower the value hence make them came first.

3. Display sort result per dataset.
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Sampled test case.
```
Input:
```
2
2
10 0
2 8
3
-5 20
1 1
10 3
```
Expected output:
```
2 8
10 0
1 1
10 3
-5 20
```
Actual output:
```
2 8
10 0
1 1
10 3
-5 20
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
All value can't be sorted by primary key.
```
Input:
```
2
2
6 5
5 6
2
-10 10
10 -10
```
Expected output:
```
5 6
6 5
-10 10
10 -10
```
Actual output:
```
5 6
6 5
-10 10
10 -10
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
์No fallback key needed.
```
Input:
```
1
4
1 2
3 1
2 2
0 5
```
Expected output:
```
1 2
2 2
3 1
0 5
```
Actual output:
```
1 2
2 2
3 1
0 5
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
