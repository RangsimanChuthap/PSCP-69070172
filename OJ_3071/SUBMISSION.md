
# Problem Solving Submission


## 1. OJ Information

OJ problem number/title:

```text
3071 — [LEARNING LOGS] จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r
```

OJ submission ID, if submitted:

```text
585047
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```
1-3 hours.
```

## 2. My Understanding

```
Find a total amount of number in given range[A,B] where dividing with variable d result in
remainder of r, assuming B < A and d < r.
```

## 3. My First Plan

```
Step 1: Take 4 input: starting range, ending range, divider, and targeted fraction.

Step 2: Get range of given number by subtracting ending range with starting range.

Step 3: Find out how many time complete dividing pattern occur on targeted range by dividing
targeted range with divider. For every occuring pattern, one number will always be number that 
yield targeted fraction

Step 4: Find the remainder of unclosed pattern. If the remainder is greater than target
remainder, add 1 to the count.
```

## 4. My Final Approach
```
Step 1: Take 4 input: starting range, ending range, divider, and targeted fraction.

Step 2: Find first number from starting range that is divisible by divider by performing
floor division on starting range with divider, add target remainder to find first number
after starting range that yield targeted fraction when divided.

Step 3: Check if first divisible number that yield targeted fraction exceed ending range
or targeted remainder is greater than or equal to divider — In both cases, meant no valid
number exist in range that yield targeted fraction; therefore, return 0 early

Step 4: Get range from first divisible number to ending range by subtracting divisible 
number from ending range.

Step 5: Perform floor division on range to get how many time a complete pattern has occured,
disregard the leftover remainder where a pattern is not closed since we only count the instance
of perfect closed pattern, a closed pattern represent 1 number that is yield targeted fraction,
we knew this work because we already offsetted the starting number so every n divider
will give us 1 additional number that divided yield a target fraction.
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Sampled Testcase
```
Input:
```
2026
2569
25
23
```
Expected output:
```
21
```
Actual output:
```
21
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
The starting range when floor-divisioned and multiplied back will yield 15, less than
initial starting range, so the lesser than starting range need to kick in and add divider worth
amount of number
```
Input:
```
16
21
5
0
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
0 is a special case, it always yield 0 when divided by any number.
```
Input:
```
0
5
1
0
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
