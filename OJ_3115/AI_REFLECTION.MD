# AI Reflection

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

---

## 2. AI Tool Used

```text
Chatgpt
```

---

## 3. What I Asked AI to Help With

```text
Optimizing the algorithm for amount of store that is open in given timestamp. And PEP-8 
assistance for "R: ln, cr: Unnecessary dictionary index lookup, use 'item[1]' instead"
```

---

## 4. What AI Helped Me Notice

```text
The initial algorithm before AI help was to use bracket lookup by storing the closing and opening
time into lookup table, initially the key would be crude lookup first, then accurate lookup
start with {openingtime // 60}:{openingtime:closingtime}, by first searching the crude 
opening hour. which will yield the range of all possible opening hour for individual store 
but not the exact minute. Initially, AI were asked to find big O notation and iteration 
per input and to suggest a way to improve algorithm. the AI pointed out about "sweep timeline"
approach and summarize how it works.  AI also helped explaining new linter warning of
"R: ln, cr: Unnecessary dictionary index lookup, use 'item[1]' instead"— which, in short,
caused by using .item() to get the key value base pairs and then attempt to get the value
again by indexing the table with key. 
```

---

## 5. What I Checked or Changed by Myself

```text
All code implementation were done with self. I only read AI description on how to optimize
the algorithm. Other logics such as caching were all done without AI suggestion.
```

---

## 6. What I Learned

```text
I learned about "sweeping line" approach and the "R: ln, cr: Unnecessary dictionary index lookup, use 'item[1]' instead"
```

---

## 7. Student Declaration

| Statement | Yes/No |
|---|---|
| I wrote this reflection in my own words. | Yes |
| This reflection describes my real AI use. | Yes |
| I checked AI's suggestions before using them. | Yes |
| I can explain my final code. | Yes |
