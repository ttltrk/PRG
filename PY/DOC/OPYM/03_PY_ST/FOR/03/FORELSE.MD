
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD) - [Python Statements](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/03_PY_ST/PY_ST.MD) - [for loops](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/03_PY_ST/FOR/FORLOOP.MD)

---

### for loop with else

---

A for loop can have an optional else block as well. The ```else``` part is executed if the items in the sequence used in for loop exhausts.

---

```python
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")
    
>>>
0
1
5
No items left.
>>>
```
---
