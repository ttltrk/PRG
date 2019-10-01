
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [DS](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DataStruct/DS.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Data Structures - Enumerate</h3>

---

* <a href='#enubasics'>Basics</a><br>

---

<h4 id='enubasics'>Basics</h4>

```python
grocery = ['bread', 'milk', 'butter']

enumerateGrocery = enumerate(grocery)
enumerateGrocery10 = enumerate(grocery, 10)

le=list(enumerateGrocery)
le10=list(enumerateGrocery10)

print(le)
print(le10)

>>>
[(0, 'bread'), (1, 'milk'), (2, 'butter')]
[(10, 'bread'), (11, 'milk'), (12, 'butter')]
>>>
```

```python
for item in enumerate(grocery):
  print(item)

for count, item in enumerate(grocery):
  print(count, item)
  
for count, item in enumerate(grocery, 100):
  print(count, item)
  
>>>
(0, 'bread')
(1, 'milk')
(2, 'butter')

0 bread
1 milk
2 butter

100 bread
101 milk
102 butter
>>>
```

```python
x=[2, 7, 9, 'alfa']
xx=list(enumerate(x))

print(xx)

>>>
[(0, 2), (1, 7), (2, 9), (3, 'alfa')]
>>>
```

---
