
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3484 — [LEARNING LOGS] หุ่นยนต์เคาะเสียงกระเบื้อง
```

OJ submission ID, if submitted:

```text
686056
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
Given a uniform size constant m and number n and a heatmap of fault in a grid heatmap
of a size m by m, calculate total fault occurance inside a grid, total grid with fault.
and total fault occurance * n. Also find fault occurance and total grid with fault per
column and row and append them to axis correspondingly.
```

## 3. My First Plan

```
1. Take input specified above.

2. Iterate over the heatmap in a row first, per row: find total fault and total grid with
fault in that row. store the data within a saperate layer for vertical side. 
total fault get to be left side of the pair while total grid with fault get to be right side 
in format of "[totalfault, totalgridwithfault]"

3. Iterate over the heatmap in a column next, per column: find total fault and total grid with
fault in that row. store the data within a saperate layer for horizonal side. We access
each column by accessing element with i index coresponding to number in range of dimention.

4. Append vertical overlay to the left of heatmap as a return by first using normal print
of sidemap but appending each corresponding element inside a vertical overlay after the
heatmap to the right. a first member in pair get to appear next to
heatmap while the other get to appear next to edge. each pair corresponse to 1 row
so no need to use column hack as overlay is structed to use horizonal-axis base.

5. Print the horizonal overlay but we need to use column hack to make each pair print as
column instead of row as the list are horizonal-axis based. We use indexing like in column
trick used before where first value get to be on first underlying row while second in pair
get to be on lower underlying row.

6. print final footer row: total fault in map, grid with fault in map, and total fault * n.
we get total fault and total grid with fault in map from horizonal row as both axis refer to
the same fault in a map in the end. refering from both will be a duplicate.
```

## 4. My Final Approach
```
1. Take input specified above.

2. Iterate over the heatmap in a row first, per row: find total fault and total grid with
fault in that row. store the data within a saperate layer for vertical side. 
total fault get to be left side of the pair while total grid with fault get to be right side 
in format of "[totalfault, totalgridwithfault]"

3. Iterate over the heatmap in a column next, per column: find total fault and total grid with
fault in that row. store the data within a saperate layer for horizonal side. We access
each column by accessing element with i index coresponding to number in range of dimention.

4. Append vertical overlay to the left of heatmap as a return by first using normal print
of sidemap but appending each corresponding element inside a vertical overlay after the
heatmap to the right. a first member in pair get to appear next to
heatmap while the other get to appear next to edge. each pair corresponse to 1 row
so no need to use column hack as overlay is structed to use horizonal-axis base.

5. Print the horizonal overlay but we need to use column hack to make each pair print as
column instead of row as the list are horizonal-axis based. We use indexing like in column
trick used before where first value get to be on first underlying row while second in pair
get to be on lower underlying row.

6. print final footer row: total fault in map, grid with fault in map, and total fault * n.
we get total fault and total grid with fault in map from horizonal row as both axis refer to
the same fault in a map in the end. refering from both will be a duplicate.
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Sample.
```
Input:
```
6 500
0 4 3 0 1 0
0 5 2 0 1 0
0 1 0 0 0 0
4 0 0 0 0 0
5 1 0 1 0 0
0 0 0 2 0 0
```
Expected output:
```
0 4 3 0 1 0 3 8
0 5 2 0 1 0 3 8
0 1 0 0 0 0 1 1
4 0 0 0 0 0 1 4
5 1 0 1 0 0 3 7
0 0 0 2 0 0 1 2
2 4 2 2 2 0
9 11 5 3 2 0
12 30 15000.00
```
Actual output:
```
0 4 3 0 1 0 3 8
0 5 2 0 1 0 3 8
0 1 0 0 0 0 1 1
4 0 0 0 0 0 1 4
5 1 0 1 0 0 3 7
0 0 0 2 0 0 1 2
2 4 2 2 2 0
9 11 5 3 2 0
12 30 15000.00
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
No Repair
```
Input:
```
3 100
0 0 0
0 0 0
0 0 0
```
Expected output:
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0
0 0 0
0 0 0.00
```
Actual output:
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0
0 0 0
0 0 0.00
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
Edge case where dimention is 1x1
```
Input:
```
1 999.99      
5
```
Expected output:
```
5 1 5
1
5
1 5 4999.95
```
Actual output:
```
5 1 5
1
5
1 5 4999.95
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
