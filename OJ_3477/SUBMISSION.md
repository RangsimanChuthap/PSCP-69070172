
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3477 — [LEARNING LOGS] Pad Thai
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
15 min.
```

## 2. My Understanding

```
Given a set of ingredient and a taste, find chef reaction to your cooking of Pad Thai.
If you added any ingredient outside of specified ingredient in making of Pad Thai.
you get "This is not Pad Thai!!!" regardless of anything else. If you missing some ingredient 
you'll get "This is bad!" regardless of other factor excluding alien ingredient.
If your Pad Thai has all the specified ingredients but missing any 3 taste or have taste
not listed, you'll get "Not Bad...". If you nailed all the recipe and taste you'll receive
"Delicious!". "Cook" specified end of receiving ingredient list and move to taste,
"End" specified end of tasting phase and entire function.
```

## 3. My First Plan

```
1. Map each ingredient and taste into a list with corresponding value of 0; Saperate
each 3 mistake into saperate flag.

2. Begin receiving the ingredient list, if an ingredient is in dict, flip the corresponding
value inside dict to 1, else: trip the alien ingredient flag.

3. When "Cook" was inputted, begin receiving the taste, if taste is in taste dict, set
corresponding value to 1. else: trip the incorrect taste flag.

4. Sweep through ingredient list, if any value is 0: trip the incomplete recipe flag.

5. Sweep through taste list, if any value is 0: trip incorrect taste flag.

6. Display corresponding message based of flag: alien ingredient first, if not then missing ingredient, and if not both then incorrect taste. if no flag are flagged return "Delicious!"
```

## 4. My Final Approach
```
1. Map each ingredient and taste into a list with corresponding value of 0; Saperate
each 3 mistake into saperate flag.

2. Begin receiving the ingredient list, if an ingredient is in dict, flip the corresponding
value inside dict to 1, else: trip the alien ingredient flag.

3. When "Cook" was inputted, begin receiving the taste, if taste is in taste dict, set
corresponding value to 1. else: trip the incorrect taste flag.

4. Sweep through ingredient list, if any value is 0: trip the incomplete recipe flag.

5. Sweep through taste list, if any value is 0: trip incorrect taste flag.

6. Display corresponding message based of flag: alien ingredient first, if not then missing ingredient, and if not both then incorrect taste. if no flag are flagged return "Delicious!"
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Delicious!
```
Input:
```
Pad Thai Sauce
Tofu
Tofu
Pickle Turnip
Shrimp
Bean Sprouts
Noodle
Chives
Lime
Egg
Oil
Egg
Peanuts
Cook
Sweet
Sour
Salty
Sweet
End
```
Expected output:
```
Delicious!
```
Actual output:
```
Delicious!
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
Not bad...
```
Input:
```
Pad Thai Sauce
Tofu
Pickle Turnip
Shrimp
Bean Sprouts
Noodle
Chives
Lime
Egg
Oil
Peanuts
Cook
Sweet
Sour
Salty
Bitter
End
```
Expected output:
```
Not Bad...
```
Actual output:
```
Not Bad...
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
Jamie Oliver making pad thai
```
Input:
```
Pad Thai Sauce
Tofu
Pickle Turnip
Shrimp
Bean Sprouts
Baby Carrot
Broccoli
Mint
Holy Basil
Chives
Lime
Egg
Oil
Peanuts
Cook
Bitter
Sweet
Salty
Sour
Umami
Spicy
Whacky
End 
```
Expected output:
```
This is not Pad Thai!!!
```
Actual output:
```
This is not Pad Thai!!!
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
