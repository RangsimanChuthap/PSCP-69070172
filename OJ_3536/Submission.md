
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3536 — [LEARNING LOGS] isPrime_large
```

OJ submission ID, if submitted:

```text
693641
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```
about 45 min-1 hour.
```

## 2. My Understanding

```
Given number n, determine whether if n is prime.
```

## 3. My First Plan

```
1. Take n input.

2. Iterate in range of 2 to square root of n(rounded down) + 1 as square root is the number that can be 
multiplied together with itself to get n, any factor greater than square root will have
matching factor that if multiplied, yielding n, already existed before square root.
hence searching for factor beyond square root became redundant. if any number inside the range satisfied
condition of n modulus number equal to 0, break and determine that n is not prime. 
otherwise if no number in range satisfied the condition, n is prime number.

3. If n is 1 or 0 (using if n > 1): also determine that n is not prime aswell.

4. Print "YES" if n is prime otherwise "NO"
```

## 4. My Final Approach
```
1. Take n input.

2. Iterate in range of 2 to square root of n(rounded down) + 1 as square root is the number that can be 
multiplied together with itself to get n, any factor greater than square root will have
matching factor that if multiplied, yielding n, already existed before square root.
hence searching for factor beyond square root became redundant. if any number inside the range satisfied
condition of n modulus number equal to 0, break and determine that n is not prime. 
otherwise if no number in range satisfied the condition, n is prime number.

3. If n is 1 or 0 (using if n > 1): also determine that n is not prime aswell.

4. Print "YES" if n is prime otherwise "NO"
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Only factor is 1 which satisfies the factor logic, but is not prime number since
prime number must have 2 factor: 1 and itself.
```
Input:
```
1
```
Expected output:
```
NO
```
Actual output:
```
NO
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
Will yield wrong result if we did not add + 1 to range.
```
Input:
```
4
```
Expected output:
```
NO
```
Actual output:
```
NO
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
Very large and would likely be timed out if we did not stop iterating at square root.
```
Input:
```
125863
```
Expected output:
```
YES
```
Actual output:
```
NO
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
