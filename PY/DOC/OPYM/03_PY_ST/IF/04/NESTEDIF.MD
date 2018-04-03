
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD) - [Python Statements](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/03_PY_ST/PY_ST.MD) - [if...elif](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/03_PY_ST/IF/IF_ELIF_ELSE.MD)

---

### Nested if Statements

---

```python
num = float(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
    
>>>
Enter a number:  10
Positive number
>>>

>>>
Enter a number:  0
Zero
>>>

>>>
Enter a number:  -2
Negative number
>>>

```

---
