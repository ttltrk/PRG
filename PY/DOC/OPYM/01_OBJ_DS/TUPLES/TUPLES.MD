
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD) - [Objects and Data Structures](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/OBJ_DS.MD)

---

### Tuples

---

Tuple is an ordered sequence of items same as list.The only difference is that tuples are immutable. Tuples once created cannot be modified.

---

* [Creating a Tuple](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/TUPLES/01/CREATE.MD)
* [Creating Tuple with one element](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/TUPLES/02/CRE_ONE.MD)
* [Indexing](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/TUPLES/03/INDEXING.MD)
* [Negative Indexing](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/TUPLES/04/NEG_IND.MD)
* [Slicing](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/TUPLES/05/SLICING.MD)
* [Changing a Tuple](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/TUPLES/06/CHANGE.MD)
* [Deleting a Tuple]()
* [Tuple Methods]()

---

<h4 id="7">DELETING A TUPLE</h4>

```python
t = ('p','r','o','g','r','a','m','i','z')
print(t)

del t
print(t)

>>>
('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
Traceback (most recent call last):
  File "python", line 5, in <module>
NameError: name 't' is not defined
>>>
```

---

<h4 id="8">TUPLE METHODS</h4>

* count(x)
* index(x)

```python
t = ('a','p','p','l','e',)

print(t.count('p'))
print(t.index('l'))

>>>
2
3
>>>
```

---

[src - programiz](https://www.programiz.com/python-programming/tuple)

---
