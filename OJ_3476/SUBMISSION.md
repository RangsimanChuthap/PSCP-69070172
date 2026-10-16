
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3476 — [LEARNING LOGS] CuteCat CuteFox
```

OJ submission ID, if submitted:

```text
685945
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```
30-45 min.
```

## 2. My Understanding

```
Given a list of key-value pair of cat and fox with corresponding unique identifier.
return total amount of cat, fox. and a list of cat and fox sorted by their unique 
identifier number from lowest to highest; cat first then fox. also, if cat named
"Garfield" did not exist and no cat has unique identifier of "Cat01". Add cat named
"Garfield" with unique identifier "Cat01" into the list, same with the fox for fox named
"Fubuki" with unique identifier of "Fox01".
```

## 3. My First Plan

```
1. Receive amount of animals input and take the input of All animals with their name and
unique identifier, store them inside dict using name as key and identifier as value.

2. Scan the dict to see whether cat named "Garfield" and cat with identifier of "Cat01" 
exist, if both are false: Add cat named "Garfield" with unique identifier of "Cat01" into
the dict.

3. Scan the dict to see whether fox named "Fubuki" and fox with identifier of "Fox01" 
exist, if both are false: Add fox named "Fubuki" with unique identifier of "Fox01" into
the dict.

4. Sort the list using species identifier first, then identifier number. We use custom
function to handle sorting key where it will return a tuple with 2 value, a species identifier
and identifier number; for a specicies identifier we set them to be 0 for cat and 1 for dog
as sort compare key first before comparing anything, the cats will always get priority
in sort and came before all foxes.

5. Count amount of cats and foxes inside the dict by scanning for species identifier.

6. Print count for each species, cat and foxes.

7. display sorted list.
```

## 4. My Final Approach
```
1. Receive amount of animals input and take the input of All animals with their name and
unique identifier, store them inside dict using name as key and identifier as value.

2. Scan the dict to see whether cat named "Garfield" and cat with identifier of "Cat01" 
exist, if both are false: Add cat named "Garfield" with unique identifier of "Cat01" into
the dict.

3. Scan the dict to see whether fox named "Fubuki" and fox with identifier of "Fox01" 
exist, if both are false: Add fox named "Fubuki" with unique identifier of "Fox01" into
the dict.

4. Sort the list using species identifier first, then identifier number. We use custom
function to handle sorting key where it will return a tuple with 2 value, a species identifier
and identifier number; for a specicies identifier we set them to be 0 for cat and 1 for dog
as sort compare key first before comparing anything, the cats will always get priority
in sort and came before all foxes.

5. Count amount of cats and foxes inside the dict by scanning for species identifier.

6. Print count for each species, cat and foxes.

7. display sorted list.
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Sampled test case where garfield and fubuki get appended.
```
Input:
```
5
{"Chi" : "Cat06"}
{"Tom" : "Cat05"}
{"Shiro" : "Fox02"}
{"Senko" : "Fox10"}
{"Chocola" : "Cat03"}
```
Expected output:
```
Cat : 4
Fox : 3
Garfield : Cat01
Chocola : Cat03
Tom : Cat05
Chi : Cat06
Fubuki : Fox01
Shiro : Fox02
Senko : Fox10
```
Actual output:
```
Cat : 4
Fox : 3
Garfield : Cat01
Chocola : Cat03
Tom : Cat05
Chi : Cat06
Fubuki : Fox01
Shiro : Fox02
Senko : Fox10
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
Sampled test case where garfield and fubuki did NOT get appended.
```
Input:
```
7
{"Fubuki" : "Fox05"}
{"Shiro" : "Fox01"}
{"Garfield" : "Fox06"}
{"Kin" : "Cat05"}
{"Okayu" : "Cat03"}
{"Kuro" : "Fox02"}
{"Tom" : "Cat07"}
```
Expected output:
```
Cat : 3
Fox : 4
Okayu : Cat03
Kin : Cat05
Tom : Cat07
Shiro : Fox01
Kuro : Fox02
Fubuki : Fox05
Garfield : Fox06
```
Actual output:
```
Cat : 3
Fox : 4
Okayu : Cat03
Kin : Cat05
Tom : Cat07
Shiro : Fox01
Kuro : Fox02
Fubuki : Fox05
Garfield : Fox06
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
The astronomical high number beyond 2 digit. reason for 2 problematic test case i struggled
```
Input:
```
3
{"Redd" : "Fox694201337421984"}
{"Raymond" : "Cat99999999"}
{"Ankha" : "Cat10000"}
```
Expected output:
```
Cat : 3
Fox : 2
Garfield : Cat01
Ankha : Cat10000
Raymond : Cat99999999
Fubuki : Fox01
Redd : Fox694201337421984
```
Actual output:
```
Cat : 3
Fox : 2
Garfield : Cat01
Ankha : Cat10000
Raymond : Cat99999999
Fubuki : Fox01
Redd : Fox694201337421984
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
