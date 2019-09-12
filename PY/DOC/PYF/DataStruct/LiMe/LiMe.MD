
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [DS](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DataStruct/DS.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Data Structures - List Methods</h3>

---

* <a href='#lstmappend'>append</a><br>
* <a href='#lstmclear'>clear</a><br>
* <a href='#lstmcopy'>copy</a><br>
* <a href='#lstmcount'>count</a><br>
* <a href='#lstmextend'>extend</a><br>
* <a href='#lstmindex'>index</a><br>
* <a href='#lstminsert'>insert</a><br>
* <a href='#lstmpop'>pop</a><br>
* <a href='#lstmremove'>remove</a><br>
* <a href='#lstmreverse'>reverse</a><br>
* <a href='#lstmsort'>sort</a>

---

<h4 id='lstmappend'>append</h4>

```python
l = [1, 2, 3, 4, 5, 6]
print(l)
l.append(7)
print(l)

>>>
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
>>>
```

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmclear'>clear</h4>

```python
l = [1, 2, 3, 4, 5, 6]
print(l)
l.clear()
print(l)

>>>
[1, 2, 3, 4, 5, 6]
[]
>>>
```

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmcopy'>copy</h4>

```python
l = [1, 2, 3, 4, 5, 6]
print(l)
l2 = l.copy()
l2.append(7)
print(l2)

>>>
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
>>>
```

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmcount'>count</h4>

```python
l = [1, 2, 3, 3, 4, 5, 6]
print(l)
print(l.count(1))
print(l.count(2))
print(l.count(3))

>>>
[1, 2, 3, 3, 4, 5, 6]
1
1
2
>>>
```

```python
def well(x):
    count = x.count('good')
    if count > 2:
        return 'I smell a series!'
    elif count >= 1 and count < 2:
        return 'Publish!'
    else:
        return 'Fail!'

print(well(['good','good','bad', 'bad', 'bad']))

>>>
Publish!
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='lstmextend'>extend</h4>

```python
l1 = [1, 2, 3, 4, 5, 6]
l2 = [11, 22, 33, 44, 55, 66]
print(l1)
print(l2)
l1.extend(l2)
print(l1)

>>>
[1, 2, 3, 4, 5, 6]
[11, 22, 33, 44, 55, 66]
[1, 2, 3, 4, 5, 6, 11, 22, 33, 44, 55, 66]
>>>
```

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmindex'>index</h4>

```python
l = [1, 2, 3, 4, 5, 6]
print(l)
print(l.index(1))
print(l.index(2))
print(l.index(3))

>>>
[1, 2, 3, 4, 5, 6]
0
1
2
>>>
```

find index with string/int

```python
def warn_the_sheep(queue):

    wolfIndex = queue.index('wolf')
    print(wolfIndex)

    listWolf = queue[wolfIndex:]
    print((listWolf))


warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep'])

>>>
0
['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='lstminsert'>insert</h4>

```python
l = [1, 2, 3, 4, 5, 6]
print(l)
l.insert(3, "X")
print(l)

>>>
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 'X', 4, 5, 6]
>>>
```

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmpop'>pop</h4>

```python
l = [1, 2, 3, 4, 5, 6]
print(l)
l.pop(3)
print(l)

>>>
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 5, 6]
>>>
```

remove first and last element from the list

```python
word = 'baabca'

#convert string to list
l = list(word)

#remove the first element 
l.pop(0)

#remove the last element
l.pop(-1)

#convert the list back to string
str1 = ''.join(l)

print(str1)
```

<a href='#^'>^^^</a>

---

<h4 id='lstmremove'>remove</h4>

```python
l = [1, 2, 3, 3, 3, 3, 4, 5, 6]
print(l)
l.remove(3)
print(l)
l.remove(4)
print(l)

>>>
[1, 2, 3, 3, 3, 3, 4, 5, 6]
[1, 2, 3, 3, 3, 4, 5, 6]
[1, 2, 3, 3, 3, 5, 6]
>>>
```

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmreverse'>reverse</h4>

```python
l = [1, 2, 3, 4, 5, 6]
print(l)
l.reverse()
print(l)

>>>
[1, 2, 3, 4, 5, 6]
[6, 5, 4, 3, 2, 1]
>>>
```

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmsort'>sort</h4>

```python
l1 = [1, 3, 6, 5, 2, 4]
l2 = ["c", "b", "g", "e", "f", "a", "d"]
print(l1)
print(l2)
l1.sort()
l2.sort()
print(l1)
print(l2)

>>>
[1, 3, 6, 5, 2, 4]
['c', 'b', 'g', 'e', 'f', 'a', 'd']
[1, 2, 3, 4, 5, 6]
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>>
```

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---
