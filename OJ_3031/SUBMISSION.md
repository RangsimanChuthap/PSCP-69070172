
# Problem Solving Submission


## 1. OJ Information

OJ problem number/title:

```
3031 — [LEARNING LOGS] Ink
```

OJ submission ID, if submitted:

```
565316
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
Take first 2 input, A circle area growth rate, and a total
number of coordinate input.

for every coordinate input given, return how many times a
circle need to grow until the coordinate get overlapped by
circle. Assuming circle initial position is [0,0] and
initial radius is 0.
```

## 3. My First Plan

```
Step 1: Receive initial input and parse them into
area expansion rate and coordinate pairs respectively.

Step 2: Iterate the loop by n amount according to given
number of coordinate pairs.
	Step 2.1: Receive the coordinate input (position x and
	position y)
	Step 2.2: Compute them into relative distance from origin
	(0,0) using applied pythagorus theorem:
		d = sqr((X ^ 2) + (Y ^ 2))
	Step 2.3: Use a circle expansion formula that could explain
	an Area growth rate relation to a radius to find the time
	it take for a radius to become greater than the point 
	distance
```


## 4. My Final Approach
```
Step 1: Receive initial input and parse them into
area expansion rate and coordinate pairs respectively.

Step 2: Iterate the loop by n amount according to given
number of coordinate pairs.
	Step 2.1: Receive the coordinate input (position x and
	position y)
	Step 2.2: Compute them into relative distance from origin
	(0,0) using applied pythagorus theorem:
		d = sqr((X ^ 2) + (Y ^ 2))
	Step 2.3: Use the formula t = 3.1416(d ^ 2) / expansion_rate
	to determinte how many time it took for a point to be
	overlapped by a circle, use ceiling operator to round them
	to upper integer.
```

## 5. My Tests


### Test Case 1

  

Why I chose this case:

  

```
Sampled Testcase.
```
Input:
```
50 4
0 0
0 1
30 30
0 60
```

Expected output:
```
0
1
114
227
```

Actual output:
```
0
1
114
227
```

Result:

```
Pass
```

### Test Case 2

Why I chose this case:
```
Self test case with one coordinate but absurdly large distance
```
Input:
```
12 1
125 152
```

Expected output:
```
9982
```

Actual output:
```
9982
```

Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
Large amount of coordinate with absurd amount of position value (Test code performance)
```

Input:
```
50 10
1750 1337
555 250
999 999
1423 1234
1 2456
-5 69
-1111 -191
2500 2500
-9999 9999
69072 3031
```

Expected output:
```
304740
23281
125413
222909
378999
301
79848
785400
6344650
12563887
300345012
```

Actual output:
```
304740
23281
125413
222909
378999
301
79848
785400
6344650
12563887
300345012
```

Result:
```
Pass
```

## 6. AI Use

Did you use AI for this problem?
```
Yes
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

| I wrote this submission in my own words. |YES|

| I understand my final code. |YES|

| I recorded the real OJ status. |YES|

| I did not copy AI-generated text directly into this file. |YES|

| I did not copy code from another person. |YES|

| If I received human help, I disclosed it in this file. |YES|

| I submitted the final code to the OJ by myself. |YES|
