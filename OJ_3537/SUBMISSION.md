
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3538 — [LEARNING LOGS] Impostor
```

OJ submission ID, if submitted:

```text
693619
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```
20 mins.
```

## 2. My Understanding

```
Given a list of a pair of player data: name and roles, saperated by each line until "Start" has been
inputted. after start, an inputted player will be marked as dead. after "End" has been inputted.
Display the amount of player with role "Impostor" left alive. and name list of alive and dead player 
by player name (default sort seem to works fine so probably sorted by ascii representation).
```

## 3. My First Plan

```
1. Take input and map each player data into dictionaru. using player name as key and having
associated value be [role, status]. 0 for dead, 1 for alive player. each player start with
status of alive. add 1 to impostor count if role is "Impostor"

2. When "Start" was inputted. set the player status inside the dictionary using input as key
index and change player status to 0 which meant dead. If player role is impostor, Subtract
1 from impostor count.

3. When "End" was inputted. stop receiving input. print the impostor count. iterate over
all player data in dictionary. if player status is 0: add player data into temporary
dead dict, if is 1: add data into temporary survivor dict. sort both dict by player name.
print "***Alive*** then the list of all player in survivor dict with associated role. 
then print "***Dead*** then the list of all player in dead dict.
```

## 4. My Final Approach
```
1. Take input and map each player data into dictionaru. using player name as key and having
associated value be [role, status]. 0 for dead, 1 for alive player. each player start with
status of alive. add 1 to impostor count if role is "Impostor"

2. When "Start" was inputted. set the player status inside the dictionary using input as key
index and change player status to 0 which meant dead. If player role is impostor, Subtract
1 from impostor count.

3. When "End" was inputted. stop receiving input. print the impostor count. iterate over
all player data in dictionary. if player status is 0: add player data into temporary
dead dict, if is 1: add data into temporary survivor dict. sort both dict by player name.
print "***Alive*** then the list of all player in survivor dict with associated role. 
then print "***Dead*** then the list of all player in dead dict.
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Impostor remaining
```
Input:
```
{"Green" : "Crewmate"}
{"Cyan" : "Crewmate"}
{"Red" : "Crewmate"}
{"Pink" : "Crewmate"}
{"Lime" : "Impostor"}
{"Blue" : "Impostor"}
{"White" : "Crewmate"}
{"Orange" : "Crewmate"}
Start
Green
Cyan
White
End
```
Expected output:
```
2 Impostor Remains
***Alive***
Blue : Impostor
Lime : Impostor
Orange : Crewmate
Pink : Crewmate
Red : Crewmate
***Dead***
Cyan : Crewmate
Green : Crewmate
White : Crewmate
```
Actual output:
```
2 Impostor Remains
***Alive***
Blue : Impostor
Lime : Impostor
Orange : Crewmate
Pink : Crewmate
Red : Crewmate
***Dead***
Cyan : Crewmate
Green : Crewmate
White : Crewmate
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
No impostor remaining + name sort
```
Input:
```
{"Aqua" : "Crewmate"}
{"Suisei" : "Impostor"}
{"Fubuki" : "Crewmate"}
{"Matsuri" : "Impostor"}
{"Impostor" : "Crewmate"}
{"Pekora" : "Impostor"}
{"Korone" : "Crewmate"}
{"Rushia" : "Crewmate"}
{"Kusa" : "Crewmate"}
{"Yagoo" : "Crewmate"}
{"Marine" : "Crewmate"}
{"Pinkguy" : "Crewmate"}
{"Crewmate" : "Impostor"}
{"Watame" : "Crewmate"}
Start
Aqua
Suisei
Fubuki
Matsuri
Crewmate
Pekora
End
```
Expected output:
```
0 Impostor Remains
***Alive***
Impostor : Crewmate
Korone : Crewmate
Kusa : Crewmate
Marine : Crewmate
Pinkguy : Crewmate
Rushia : Crewmate
Watame : Crewmate
Yagoo : Crewmate
***Dead***
Aqua : Crewmate
Crewmate : Impostor
Fubuki : Crewmate
Matsuri : Impostor
Pekora : Impostor
Suisei : Impostor
```
Actual output:
```
0 Impostor Remains
***Alive***
Impostor : Crewmate
Korone : Crewmate
Kusa : Crewmate
Marine : Crewmate
Pinkguy : Crewmate
Rushia : Crewmate
Watame : Crewmate
Yagoo : Crewmate
***Dead***
Aqua : Crewmate
Crewmate : Impostor
Fubuki : Crewmate
Matsuri : Impostor
Pekora : Impostor
Suisei : Impostor
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
No death + No impostor + Sort stress testing
```
Input:
```
{Zuzu : Crewmate}
{Yota : Crewmate}
{Xylem : Crewmate}
{Wukong : Crewmate}
{Uttah : Crewmate}
{Toto : Crewmate}
{SuperMum : Crewmate}
{Robo : Crewmate}
{Quackity : Crewmate}
{PPAP : Crewmate}
{Pqack : Crewmate}
{Pigsy : Crewmate}
{Otter : Crewmate}
{OUTER : Crewmate}
{Niceguy : Crewmate}
{NOlAN : Crewmate}
{MickeyMouse : CrewMate}
{Lol : Crewmate}
{Lovity : Crewmate}
{KingofClubs : Crewmate}
{KingofDiamonds : Crewmate}
{KingofSpades : Crewmate}
{KingofHeart: Crewmate}
{ISpyWithMyLittleEyes: Crewmate}
{IshowSpeed: Crewmate}
{HomerSimpson: Crewmate}
{Hunsen : Crewmate}
{Guilliver : Crewmate}
{Guy : Crewmate}
{Gawinthep: Crewmate}
{Forklift : Crewmate}
{FizzBuzz : Crewmate}
{FalloutNewVegas : Crewmate}
{FrintStone : Crewmate}
{E : Crewmate}
{EE : Crewmate}
{Eyjafjallajokull : Crewmate}
{DoctorHouse : Crewmate}
{Daew : Crewmate}
{Chotipat : Crewmate}
{Baowee : Crewmate}
{AmongUs : Crewmate}
{AAABattery : Crewmate}
Start
End
```
Expected output:
```
0 Impostor Remains
***Alive***
AAABattery : Crewmate
AmongUs : Crewmate
Baowee : Crewmate
Chotipat : Crewmate
Daew : Crewmate
DoctorHouse : Crewmate
E : Crewmate
EE : Crewmate
Eyjafjallajokull : Crewmate
FalloutNewVegas : Crewmate
FizzBuzz : Crewmate
Forklift : Crewmate
FrintStone : Crewmate
Gawinthep : Crewmate
Guilliver : Crewmate
Guy : Crewmate
HomerSimpson : Crewmate
Hunsen : Crewmate
ISpyWithMyLittleEyes : Crewmate
IshowSpeed : Crewmate
KingofClubs : Crewmate
KingofDiamonds : Crewmate
KingofHeart : Crewmate
KingofSpades : Crewmate
Lol : Crewmate
Lovity : Crewmate
MickeyMouse : CrewMate
NOlAN : Crewmate
Niceguy : Crewmate
OUTER : Crewmate
Otter : Crewmate
PPAP : Crewmate
Pigsy : Crewmate
Pqack : Crewmate
Quackity : Crewmate
Robo : Crewmate
SuperMum : Crewmate
Toto : Crewmate
Uttah : Crewmate
Wukong : Crewmate
Xylem : Crewmate
Yota : Crewmate
Zuzu : Crewmate
***Dead***
```
Actual output:
```
0 Impostor Remains
***Alive***
AAABattery : Crewmate
AmongUs : Crewmate
Baowee : Crewmate
Chotipat : Crewmate
Daew : Crewmate
DoctorHouse : Crewmate
E : Crewmate
EE : Crewmate
Eyjafjallajokull : Crewmate
FalloutNewVegas : Crewmate
FizzBuzz : Crewmate
Forklift : Crewmate
FrintStone : Crewmate
Gawinthep : Crewmate
Guilliver : Crewmate
Guy : Crewmate
HomerSimpson : Crewmate
Hunsen : Crewmate
ISpyWithMyLittleEyes : Crewmate
IshowSpeed : Crewmate
KingofClubs : Crewmate
KingofDiamonds : Crewmate
KingofHeart : Crewmate
KingofSpades : Crewmate
Lol : Crewmate
Lovity : Crewmate
MickeyMouse : CrewMate
NOlAN : Crewmate
Niceguy : Crewmate
OUTER : Crewmate
Otter : Crewmate
PPAP : Crewmate
Pigsy : Crewmate
Pqack : Crewmate
Quackity : Crewmate
Robo : Crewmate
SuperMum : Crewmate
Toto : Crewmate
Uttah : Crewmate
Wukong : Crewmate
Xylem : Crewmate
Yota : Crewmate
Zuzu : Crewmate
***Dead***
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
