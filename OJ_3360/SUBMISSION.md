
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3360 — [LEARNING LOGS] หั่นขนมปัง
```

OJ submission ID, if submitted:

```text
684728
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```
around 45 min.
```

## 2. My Understanding

```
divide an square of an size into uneven grid using given horizonal and vertical cut position. find the size of largest and second-largest piece of children square after division.
```

## 3. My First Plan

```
1. Take the basic input: Size and number of cut.

2. Iterate and store all cut position in horizontal and vertical direction.

3. Add 0 and final width/height to both cut position as start-stop to define boundaries of 
each children after cut.

4. Iterate over all cut position which now define boundaries of each children of a grid;

4.1. Iterating horizonally first using current and next cut position (index + 1) as boundaries;
calculate the horizonal area by subtracting next horizonal boundaries with current boundaries.

4.2. From each iteration inside horizonal axis, Iterate over all vertical boundaries again
to get 2-dimention cut, get current vertical area by subtracting next vertical boundaries with
current boundaries.

4.3. multiply horizonal area with vertical area and store them inside the list. iterate until all
horizonal cut and vertical cut are iterated.

5. Sort the area list, print the first and second member from last.
```

## 4. My Final Approach
```
1. Take the basic input: Size and number of cut.

2. Iterate and store all cut position in horizontal and vertical direction.

3. Add 0 and final width/height to both cut position as start-stop to define boundaries of 
each children after cut.

4. Iterate over all cut position which now define boundaries of each children of a grid;

4.1. Iterating horizonally first using current and next cut position (index + 1) as boundaries;
calculate the horizonal area by subtracting next horizonal boundaries with current boundaries.

4.2. From each iteration inside horizonal axis, Iterate over all vertical boundaries again
to get 2-dimention cut, get current vertical area by subtracting next vertical boundaries with
current boundaries.

4.3. multiply horizonal area with vertical area and store them inside the list. iterate until all
horizonal cut and vertical cut are iterated.

5. Sort the area list, print the first and second member from last.
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Sampled test case.
```
Input:
```
20 12 3 4
2 10 14
1 6 8 10
```
Expected output:
```
40 30
```
Actual output:
```
40 30
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
4 5 3 4
1 2 3
1 2 3 4
```
Expected output:
```
1 1
```
Actual output:
```
1 1
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
Test for one cut.
```
Input:
```
10 10 1 1
5
5
```
Expected output:
```
25 25
```
Actual output:
```
25 25
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
| I wrote this submission in my own words. | YES |
| I understand my final code. | YES |
| I recorded the real OJ status. | YES |
| I did not copy AI-generated text directly into this file. | YES |
| I did not copy code from another person. | YES |
| If I received human help, I disclosed it in this file. | YES |
| I submitted the final code to the OJ by myself. | YES |
