
# Problem Solving Submission


## 1. OJ Information

OJ problem number/title:

```text
3072 — [LEARNING LOGS] A-E-I-O-U
```

OJ submission ID, if submitted:

```text
584187
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
Take 1 string as an input.

Return the number of times a each vowel appeared in the given text. (case insensitive)
```

## 3. My First Plan

```
Step 1: Receive single string as an input, then run .lower() through it.

Step 2: Convert string into list that contained all the characters that made up the string

Step 3: Make a dictionary with vowel being the key and occuring number being the value

Step 4: Set the occuring number of each vowel by using built in .count(c) function, where c is
representative of individual vowel.

Step 5: Now, iterate through every item in dictionary. If value of a key is not 0, then
print ("{vowels}: {occurancenumber}").
```

## 4. My Final Approach
```
Step 1: Receive single string as an input, then run .lower() through it.

Step 2: Convert string into list that contained all the characters that made up the string

Step 3: Make a dictionary with vowel being the key and occuring number being the value

Step 4: Set the occuring number of each vowel by using built in .count(c) function, where c is
representative of individual vowel.

Step 5: Now, iterate through every item in dictionary. If value of a key is not 0, then
print ("{vowels}: {occurancenumber}").
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
The input string contained multiple vowels, all in same case.
```
Input:
```
racecar
```
Expected output:
```
a : 2
e : 1
```
Actual output:
```
a : 2
e : 1
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
The input string contained single vowel, but in different case.
```
Input:
```
aAa
```
Expected output:
```
a : 3
```
Actual output:
```
a : 3
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
Input string contained no vowels at all.
```
Input:
```
Cysts
```
Expected output:
```
{Void}
```
Actual output:
```
{Void}
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
