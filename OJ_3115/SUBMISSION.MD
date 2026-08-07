
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3115 — [LEARNING LOGS] Arcade of Time: Store Check
```

OJ submission ID, if submitted:

```text
593849
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```
About 1 day.
```

## 2. My Understanding

```
give n,m as the amount of store and amount of timestamp to be checked.
all times used in this problem are in minute representation.

for n amount of time: take 1 input(string), which is in "{opentime} {closetime}" format.

take final input as string, each contained timestamp saperated by whitespace.

iterate through individual timestamp in final input string and return the amount of store
that is open in the exact tiem frame.
```

## 3. My First Plan

```
Step 1: Take n and m as single input string, use.split().

Step 2: For n time: take single input: a string containing opening and closing hour saperated
by single whitespace, use.split()

Step 3: Store the opening and closing time in bucket approach, where the table of opening
and closing time in another table as key with value is the amount, which, this table, 
is stored as value in table with crude opening hour as main key, the exact time is stored
into all main key opening hour where opening hour // 60 is not greater thanmain hour value. 
Let the table be timetable.

Step 4: Initialize a empty string to be a display string.

Step 5: Take timestamp check, use .split() to get individual timestamp to be checked.

Step 6: Iterate m time, accessing timestamp through m as index. let crudetime = timestamp 
floor divided by 60 and store = 0. iterate through all timetable, if hour <= crudetime: continue
the search by comparing the timestamp with opening and closing hour where
openinghour <= timestamp < closinghour, If true: add the count to the store. Finally, append 
the stringnified store into display string

Step 7: print the displaystring.strip()
```

## 4. My Final Approach
```
Step 1: Take n and m as single input string, use.split().

Step 2: For n time: take single input: a string containing opening and closing hour saperated
by single whitespace, use.split()

Step 3: Create timeline for every change in currently opening amount, for opening time,
add 1 to the change; for closing time, subtract 1; Store the keyframe into timeline table.


Step 5: Initialize a empty string to be a display string.

Step 6: Take timestamp check, use .split() to get individual timestamp to be checked.

Step 6: Iterate m time, accessing timestamp through m as index. each iteration iterate over all 
keyframe in timeline table, let ccu = 0, if keyframe is lesser than current timestamp, 
add the value of current keyframe into ccu. add stringnified ccu + " " into the display value.

Step 7: print the displaystring.strip()
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Sampled testcase
```
Input:
```
3 5
540 1020
600 660
1080 1200
600 659 660 900 1300
```
Expected output:
```
2 2 1 1 0
```
Actual output:
```
2 2 1 1 0
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
Sampled testcase
```
Input:
```
2 3
0 720
500 1000
100 700 800
```
Expected output:
```
1 2 1
```
Actual output:
```
1 2 1
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
Testing duplicatant + caching.
```
Input:
```
6 5
300 900
420 840
999 1440
300 900
450 1280
730 990
696 420 1080 420 860
```
Expected output:
```
4 3 2 3 4
```
Actual output:
```
4 3 2 3 4
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
Code implementation + initial algorithm.
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
