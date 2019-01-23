
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [DS](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DataStruct/DS.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Data Structures - Print Formatting</h3>

---

```python
'String here {} then here {}'.format('something1', 'something2')
```

<a href='#^'>^^^</a>

---

```python
print('this is a string {}'.format('INSERTED'))

>>>
this is a string INSERTED
>>>
```

<a href='#^'>^^^</a>

---

```python
print('the {} {} {}'.format('fox', 'brown', 'quick'))
print('the {2} {0} {1}'.format('fox', 'brown', 'quick'))
print('the {b} {q} {f}'.format(f='fox', b='brown', q='quick'))

>>>
the fox brown quick
the quick fox brown
the brown quick fox
>>>
```

<a href='#^'>^^^</a>

---

```python
def choose():
    a1, b1, c1 = 0, 0, 0
    inp = input('a, b, or c? \n')
    if inp == 'a':
        a1 = 1
    elif inp == 'b':
        b1 = 1
    elif inp == 'c':
        c1 = 1
    else:
        return err()
    print('the result is {aa} {bb} {cc}'.format(aa = a1, bb = b1, cc = c1))

def err():
    print('no or wrong pwd')
    
choose()

>>>
a, b, or c? 

a
the result is 1 0 0

b
the result is 0 1 0

c
the result is 0 0 1

xxx
no or wrong pwd
>>>
```

<a href='#^'>^^^</a>

---

```python
n = 'trk'
a = '35'

print('hi my name is {}'.format(n))
print(f'hi my name is {n} and Im {a}')

>>>
hi my name is trk
hi my name is trk and Im 35
>>>
```

<a href='#^'>^^^</a>

---
