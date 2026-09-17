
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3293 — BigFrame
```

OJ submission ID, if submitted:

```text
634356
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```
15-30 min.
```

## 2. My Understanding

```
Take 5 string as input.

Encase the input plaintext into "*" as frame with horizontal padding of 1 char
```

## 3. My First Plan

```
Step 1: Take 5 input, store the input in list.

Step 2: find the longest text using len(max(list, key = len())) and add + 4
2 for 2 horizontal padding and 2 for border.

Step 3: print "*" * longest text length.

Step 4: print ("* ") then individual input in list. add filler whitespace after text
by subtracting the longest text len with (current text length + 2), then add " *" as border

Step 4: print "*" * longest text length.
```

## 4. My Final Approach
```
Step 1: Take 5 input, store the input in list. use trycatch so if input gave EOF error
treat them as empty string.

Step 2: find the longest text using len(max(list, key = len())) and add + 4
2 for 2 horizontal padding and 2 for border.

Step 3: print "*" * longest text length.

Step 4: print ("* ") then individual input in list. add filler whitespace after text
by subtracting the longest text len with (current text length + 2), then add " *" as border

Step 4: print "*" * longest text length.
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Sampled
```
Input:
```
Hello World       
in 
a 
big
frame
```
Expected output:
```
***************
* Hello World *
* in          *
* a           *
* big         *
* frame       *
***************
```
Actual output:
```
***************
* Hello World *
* in          *
* a           *
* big         *
* frame       *
***************
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
Empty input string
```
Input:
```
CAN YOU HEAR THE SIENCE
CAN YOU SEE THE DARK
CAN YOU FIX THE BROKEN

CAN YOU FEEL MY HEART
```
Expected output:
```
***************************
* CAN YOU HEAR THE SIENCE *
* CAN YOU SEE THE DARK    *
* CAN YOU FIX THE BROKEN  *
*                         *
* CAN YOU FEEL MY HEART   *
***************************
```
Actual output:
```
***************************
* CAN YOU HEAR THE SIENCE *
* CAN YOU SEE THE DARK    *
* CAN YOU FIX THE BROKEN  *
*                         *
* CAN YOU FEEL MY HEART   *
***************************
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
Non empty whitespace case
```
Input:
```
Sure, it's a calming notion
Propetual in motion
But i don't need the comfort
In any lies
    
```
Expected output:
```
********************************
* Sure, it's a calming notion  *
* Propetual in motion          *
* But i don't need the comfort *
* In any lies                  *
*                              *
********************************
```
Actual output:
```
********************************
* Sure, it's a calming notion  *
* Propetual in motion          *
* But i don't need the comfort *
* In any lies                  *
*                              *
********************************
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
