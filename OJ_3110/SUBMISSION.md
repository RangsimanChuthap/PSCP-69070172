
# Problem Solving Submission


## 1. OJ Information

OJ problem number/title:

```text
3110 — [LEARNING LOGS] สงคราม...ส่งด่วน
```

OJ submission ID, if submitted:

```text
587544
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
Create a program that take 2 input: first is string that is starting route and destination route saperated
by a whitespace, second is total weight (Real number)

given a preset that contained starting and ending route present and their prices per cargo kilo and fixed 
service fee. Calculate the total cost to deliver the payload.

If given starting route to the destination is not defined in preset table - return "Error".
```

## 3. My First Plan

```
Step 1: Take first input, saperate the input into starting and destination by using .split()

Step 2: Take second input as payload weight (as real number)

Step 3: Define the lookup that contain the route info structured as follow:
    -----------------------------------------------------------------------
    StartRoute:{
                DestinationRoute: [FixedFee,PricePerKilo]
            }
    -----------------------------------------------------------------------

Step 4: Use Trycatch to fetch route data from lookup table with following relation:
    -----------------------------------------------------------------------
    get(key = startroute) -> get(key = destinationroute)
    -----------------------------------------------------------------------
if data exist and fetched successfully, we will get an array of[FixedFee, PricePerKilo] as 
RefTable
if data DOESN'T exist in any of the getter, we will get NoneType object as RefTable

Step 5: Let TotalCost = RefTable[0] + (RefTable[1] * PayloadWeight); If fetch fails, RefTable will be 
NoneType Object, meaning it element is non-subscriptable(doesn't have iterable structure) or in
simple term: cannot be indexed. Which will trigger a TypeError, and a except bracket will catch it,
printing "Error"

Step 6: If trycatch did not catch any exception and TotalCost is valid, return TotalCost. with .2f
format
```

## 4. My Final Approach
```
Step 1: Take first input, saperate the input into starting and destination by using .split()

Step 2: Take second input as payload weight (as real number)

Step 3: Define the lookup that contain the route info structured as follow:
    -----------------------------------------------------------------------
    StartRoute:{
                DestinationRoute: [FixedFee,PricePerKilo]
            }
    -----------------------------------------------------------------------

Step 4: Use Trycatch to fetch route data from lookup table with following relation:
    -----------------------------------------------------------------------
    get(key = startroute) -> get(key = destinationroute)
    -----------------------------------------------------------------------
if data exist and fetched successfully, we will get an array of[FixedFee, PricePerKilo] as 
RefTable
if data DOESN'T exist in any of the getter, we will get NoneType object as RefTable

Step 5: Let TotalCost = RefTable[0] + (RefTable[1] * PayloadWeight); If fetch fails, RefTable will be 
NoneType Object, meaning it element is non-subscriptable(doesn't have iterable structure) or in
simple term: cannot be indexed. Which will trigger a TypeError, and a except bracket will catch it,
printing "Error"

Step 6: If trycatch did not catch any exception and TotalCost is valid, return TotalCost. with .2f
format
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Sampled Testcase
```
Input:
```
BKK CNX
2
```
Expected output:
```
70.00
```
Actual output:
```
70.00
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
Route relation doesn't exist in preset for the destination route.
```
Input:
```
BKK UBP
10
```
Expected output:
```
Error
```
Actual output:
```
Error
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
Route relation doesn't exist in preset for both starting and destination route.
```
Input:
```
FNJ
LAX
```
Expected output:
```
Error
```
Actual output:
```
Error
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
