
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD) - [Objects and Data Structures](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/OBJ_DS.MD)

---

### Set

---

Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }. Items in a set are not ordered.

---

* [Create a Set](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/SETS/01/CREATE.MD)
* [Change Set in Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/SETS/02/CHANGE.MD)
* [Remove Elements from a Set](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/SETS/03/REM_ELE.MD)
* [Set Union]()
* [Set Intesection]()
* [Set Difference]()
* [Set Simmetric Difference]()

---

SET UNION

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)

>>>
{1, 2, 3, 4, 5, 6, 7, 8}
>>>
```

---

SET INTERSECTION

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A & B)

>>>
{4, 5}
>>>
```

---

SET DIFFERENCE

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A - B)
print(B - A)

>>>
{1, 2, 3}
{8, 6, 7}
>>>
```

---

SET SIMMETRIC DIFFERENCE

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A ^ B)

>>>
{1, 2, 3, 6, 7, 8}
>>>
```

---

[src - programiz.com](https://www.programiz.com/python-programming/set)

---
