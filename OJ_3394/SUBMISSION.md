
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3394 — [LEARNING LOGS] ส่งต่อ
```

OJ submission ID, if submitted:

```text
685471
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
Given a reference table of a number where it will point toward different number and starting number.
find how many unique number are inside that closed cycle exluding starting number, 
each number can only reference 1 others number. and refering to number already refered will not continue the loop nor a number with reference number of 0.
(100 prisoner box problem thing).
```

## 3. My First Plan

```
1. Take amount of member and starting number.

2. Map each starting number to a value inside a list, each starting at 0, for a number already
reached.

3.Initialize the cycle by starting at starting number, and cycle through reference number of current number.
flip the corresponding representation inside a list to 1 for every visited number. if the cycle
reach a number that already had value representation inside a list with a value of 1 —
we have came full cycle. Or we reached number whose reference to 0 which meant self, 
meaning dead end. 
stop the loop and return how many unique number reached inside the cycle.
in this case we use the sum of all 1 inside a list as it represent all number we reached 
inside a cycle deducted by 1 to exclude starting number.
```

## 4. My Final Approach
```
1. Take amount of member and starting number.

2. Map each starting number to a value inside a list, each starting at 0, for a number already
reached.

3.Initialize the cycle by starting at starting number, and cycle through reference number of current number.
flip the corresponding representation inside a list to 1 for every visited number. if the cycle
reach a number that already had value representation inside a list with a value of 1 —
we have came full cycle. Or we reached number whose reference to 0 which meant self, 
meaning dead end. 
stop the loop and return how many unique number reached inside the cycle.
in this case we use the sum of all 1 inside a list as it represent all number we reached 
inside a cycle deducted by 1 to exclude starting number.
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Sampled test case.
```
Input:
```
3 1
2
3
0
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

### Test Case 2

Why I chose this case:
```
Cycle end instantly as we point to number who refered to self.
```
Input:
```
5 4
2
3
1
0
3
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
Closed loop contained all possible member.
```
Input:
```
5 3
3
5
2
4
1
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
