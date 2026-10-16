
# Problem Solving Submission

## 1. OJ Information

OJ problem number/title:

```text
3355 — [LEARNING LOGS] Shorten
```

OJ submission ID, if submitted:

```text
684575
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
ให้ค่าตัวเลขจำนวนเต็มบวกที่นับเพิ่มขึ้นไปเรื่อย ๆ แล้วให้ย่นช่วงจำนวนที่ติดกันโดยไม่ขาดโดยใช้ตัว "-" เป็นตัวเชื่อม หากช่วงไม่มีตอน
ให้แสดงเป็นตัวเลขโดดตัวเดียว
```

## 3. My First Plan

```
รับข้อมูลตัวเลขมาเรื่อย ๆ จนกว่าจะได้ค่า -1 คือสั่งหยุด จากนั้นก็เก็บข้อมูลตัวเลขทั้งหมดไว้ใน list แล้วจัดการรันตัวเลขทุกตัวภายใน list
เพื่อหาความต่อเนื่อง โดยเช็กจากตัวตัวก่อน + 1 เทียบกับตัวเลขปัจจุบัน หากใช่ให้จัดข้อมูลนั้นเป็นช่วง ๆ หนึ่งจนกว่าจะขาดสาย แล้ว
ทำการ print ตัวเลขตัวเริ่มไปจนถึงเลขสุดท้ายก่อนขาดสาย สำหรับตัวเลขโดดที่มีช่วงโดดเดี่ยวให้ปริ้นเป็นตัวเลขโดดธรรมดาไม่ต้องมีขีดช่วงคั่น
```

## 4. My Final Approach
```
รับข้อมูลตัวเลขมาเรื่อย ๆ จนกว่าจะได้ค่า -1 คือสั่งหยุด จากนั้นก็เก็บข้อมูลตัวเลขทั้งหมดไว้ใน list แล้วจัดการรันตัวเลขทุกตัวภายใน list
เพื่อหาความต่อเนื่อง โดยเช็กจากตัวตัวก่อน + 1 เทียบกับตัวเลขปัจจุบัน หากใช่ให้จัดข้อมูลนั้นเป็นช่วง ๆ หนึ่งจนกว่าจะขาดสาย แล้ว
ทำการ print ตัวเลขตัวเริ่มไปจนถึงเลขสุดท้ายก่อนขาดสาย สำหรับตัวเลขโดดที่มีช่วงโดดเดี่ยวให้ปริ้นเป็นตัวเลขโดดธรรมดาไม่ต้องมีขีดช่วงคั่น
```

## 5. My Tests


### Test Case 1

Why I chose this case:
```
Sample
```
Input:
```
1
2
3
5
7
9
10
-1
```
Expected output:
```
1-3, 5, 7, 9-10
```
Actual output:
```
1-3, 5, 7, 9-10
```
Result:
```
Pass
```

### Test Case 2

Why I chose this case:
```
Sample
```
Input:
```
1
2
3
4
5
-1
```
Expected output:
```
1-5
```
Actual output:
```
1-5
```
Result:
```
Pass
```

### Test Case 3

Why I chose this case:
```
เหลี่ยมอาจารย์โช ไม่มีตัวเลขอะไรเลย
```
Input:
```
-1
```
Expected output:
```

```
Actual output:
```

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
