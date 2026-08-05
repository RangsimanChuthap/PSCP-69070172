# AI Reflection

## 1. OJ Information

OJ problem number/title:

```text
3111 — [LEARNING LOGS] สหกรณ์โรงเรียน
```

OJ submission ID, if submitted:

```text
587882
```

OJ status:

```text
Pass
```

---

## 2. AI Tool Used

```text
Claude Sonnet 5.5
```

---

## 3. What I Asked AI to Help With

```text
Used AI to help debugging the code to check for possible flaw in code logic. that caused
testcase #1 to kept on failing after multiple self assesment attempts.
```

---

## 4. What AI Helped Me Notice

```text
AI pointed out a flaw in discount logic caused by IEEE 754 floating point arithmetic flaw.
```

---

## 5. What I Checked or Changed by Myself

```text
Changed discount logic to use whole number instead of floating point arithmetic in calculation.
verified and confirmed with addition IEEE-754-prone test case.
```

---

## 6. What I Learned

```text
I was looking for the wrong place the whole time, the decimal rounder was not the problem.
my own code was equipped for IEEE-754 floating point arithmatic problem. I also learned
that using decimal multiplication for percentage directly into my code is not a good idea -
since it is IEEE 754 arithmetic floating point error prone.
```

---

## 7. Student Declaration

| Statement | Yes/No |
|---|---|
| I wrote this reflection in my own words. | Yes |
| This reflection describes my real AI use. | Yes |
| I checked AI's suggestions before using them. | Yes |
| I can explain my final code. | Yes |
