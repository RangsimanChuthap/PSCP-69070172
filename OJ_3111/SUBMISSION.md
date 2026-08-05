
# Problem Solving Submission


## 1. OJ Information

OJ problem number/title:

```text
3111 — [LEARNING LOGS] สหกรณ์โรงเรียน
```

OJ submission ID, if submitted:

```text
587882
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```
0-15 min
```

## 2. My Understanding

```
First, Take 2 input, A string that is either "Y" or "N" that dictate membership status,
and n number which determine purchase amount

For n number: take an input (Real positive number) and store the value into total cost.

If the string is "Y": grant -5% to total cost; If string is "N" and total >= 500: grant -3% to
total cost.

Return the final total cost in 2 decimal places, rounded up if 3rd decimal >= 5, rounded down
otherwise.
```

## 3. My First Plan

```
Step 1: Take first input as m(string) and second input as n(integer).

Step 2: Let total = 0. Iterate for loop n time; For each iteration, take the user input
(real number), and the add the number into total.

Step 3: Check if discount condition applies: -5% from total if m = "Y", -3% from total if M = "N"
and total >= 500

Step 4: Round the number by first multiplying total with 1000, then find the 3rd decimal by
performing floor division on total with 10.

Step 5: Strip fraction off the total by subtracting fraction amount from total. Then, check if
fraction is equal or greater than 5: if true, add 10 into the value (0.01 in respective decimal term)

Step 6: Divide total back by 1000 to get original value in term of decimal place back.

Step 7: Return the value as output.
```

## 4. My Final Approach
```
Step 1: Take first input as m(string) and second input as n(integer).

Step 2: Let total = 0. Iterate for loop n time; For each iteration, take the user input
(real number), and the add the number into total.

Step 3: Check if discount condition applies: -5% from total if m = "Y", -3% from total if M = "N"
and total >= 500

Step 4: Round the number by first multiplying total with 1000, then find the 3rd decimal by
performing floor division on total with 10.

Step 5: Strip fraction off the total by subtracting fraction amount from total. Then, check if
fraction is equal or greater than 5: if true, add 10 into the value (0.01 in respective decimal term)

Step 6: Divide total back by 1000 to get original value in term of decimal place back.

Step 7: Return the value as output with :.2f format.
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
A standard .round() with yield 71.72 where the intended result is 71.73 (actual value is 71.725)
```
Input:
```
Y
3
20
45.5
10
```
Expected output:
```
71.73
```
Actual output:
```
71.73
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
Case where using 0.95 * total won't work and will need to be converted to whole number
to perform operation (IEEE 754 floating point arithmetic flaw).

The valid result should yield actual value of 0.67 where IEEE 754 yield 0.66 
(from 0.7 /0.95 = 0.6649999999999999  resulted in rounding down)
```
Input:
```
Y
1
0.7
```
Expected output:
```
0.67
```
Actual output:
```
0.67
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
A normal test case where IEEE 754 flaoting point arirthmetic flawed code, .round() code,
and actual working code should yield same result.
```
Input:
```
N
3
200
200
100
```
Expected output:
```
500
```
Actual output:
```
500
```
Result:
```
Pass
```

## 6. AI Use

Did you use AI for this problem?
```
YES
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
