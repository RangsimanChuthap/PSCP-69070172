
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3135 — [LEARNING LOGS] ของขวัญและขโมย
```

OJ submission ID, if submitted:

```text
598918
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```
1-2 hours.
```

## 2. My Understanding

```
Take input N, K, T where (N is positive int, K is positive int that is N - 1 at max, T is 
positive int that is N at max)

Perform a loop by initially starting at 1, Incrementing at the rate of K, if number exceeded N,
loop back to 1 again as if a clock cycle. If a number reach exactly 1 or T. end the iteration
and return how many unique number have been reached in an iteration as an output.
```

## 3. My First Plan

```
Step 1: Take N,K,T as an string, use map(int, "N K T".split())

Step 2: Initialize a variable: current_position = 0, iteration_cycle = 1, count = 0,
initialized = False

Step 3: Perform iteration loop.
    Step 3.1: Set current position = ((iteration_cycle * K) % N) + 1
    Step 3.2A: If current position value is not 1 or T: continue the iteration and add 1 to
    count.
    Step 3.2B: If current position value is 1 or T (WITH THE EXCEPTION OF FIRST ITERATION):
    terminate the iteration loop, if current position value is T: also add 1 to count.
    Step 3.3: Set flag initialized to True
    Step 3.4: Increment the iteration_cycle by 1
```

## 4. My Final Approach
```
Step 1: Take N,K,T as an string, use map(int, "N K T".split())

Step 2: Initialize a variable: current_position = 0, iteration_cycle = 1, count = 0,
initialized = False

Step 3: Perform iteration loop.
    Step 3.1: Set current position = ((iteration_cycle * K) % N) + 1
    Step 3.2A: If current position value is not 1 or T: continue the iteration and add 1 to
    count.
    Step 3.2B: If current position value is 1 or T (WITH THE EXCEPTION OF FIRST ITERATION):
    terminate the iteration loop, if current position value is T: also add 1 to count.
    Step 3.3: Set flag initialized to True
    Step 3.4: Increment the iteration_cycle by 1
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Ordinary test case where no edge case were found
```
Input:
```
6 4 2
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
Edge case where iteration reached every possible unique number (the output should never
exceed N)
```
Input:
```
9 7 3
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
Edge case where 1 is also a breakpoint number.
```
Input:
```
5 3 1
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
