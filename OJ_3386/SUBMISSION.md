
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3386 — [LEARNING LOGS] Duplicate I
```

OJ submission ID, if submitted:

```text
685026
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
Given 2 dataset, return the value occurance that is presence in both dataset sort by value descending. return "Nope" if none presence.
```

## 3. My First Plan

```
1. Take dataset a and b size.

2. Receive all data in dataset a and b and store the data in each dataset list.

3. Find the intersection by iterate over dataset A member and check whether does it exist
in dataset B. if true, add to intersection table. we dont need to iterate over dataset B
member as if it exist in BOTH A and B then it is impossible for a value to be missed when
scanning for intersection using dataset A.

4. Sort all value inside intersection list using reversed = True to sort from highest to lowest, print.
if no value in intersection list, print "Nope" instead.
```

## 4. My Final Approach
```
1. Take dataset a and b size.

2. Receive all data in dataset a and b and store the data in each dataset list.

3. Find the intersection by iterate over dataset A member and check whether does it exist
in dataset B. if true, add to intersection table. we dont need to iterate over dataset B
member as if it exist in BOTH A and B then it is impossible for a value to be missed when
scanning for intersection using dataset A.

4. Sort all value inside intersection list using reversed = True to sort from highest to lowest, print.
if no value in intersection list, print "Nope" instead.
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Sampled test case, No intersection.
```
Input:
```
10
10
56070147
59070002
58070161
59070044
59070019
59070116
58070040
59070032
58070009
59070048
59070135
59070063
59070146
59070149
59070141
59070103
59070110
59070008
59070158
59070188
```
Expected output:
```
Nope
```
Actual output:
```
Nope
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
Sampled test case.
```
Input:
```
15
12
59070158
59070074
59070173
59070012
59070191
59070078
59070167
59070127
59070116
59070105
59070155
58070153
59070182
59070047
59070061
59070185
59070148
59070065
58070015
59070173
59070070
59070012
58070161
59070116
59070170
58070108
59070049
```
Expected output:
```
59070173
59070116
59070012
```
Actual output:
```
59070173
59070116
59070012
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
Everything in A is presence in B aswell so A is subset of B
```
Input:
```
4
6
69070172
69070173
69070174
69070175
69070176
69070175
69070174
69070173
69070172
69070171
```
Expected output:
```
69070175
69070174
69070173
69070172
```
Actual output:
```
69070175
69070174
69070173
69070172
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
