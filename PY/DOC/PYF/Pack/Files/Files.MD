
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [PMF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/Pack/Pack.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Packages/Modules/Files - Files</h3>

---

```python
mf = open('C:\\path\\path\\path\\test.txt')

>>>
Process finished with exit code 0
>>>
```

<a href='#^'>^^^</a>

---

```python
mf = open('C:\\path\\path\\path\\test.txt')
print(mf.read())

>>>
hello world
new line
third line and hello 
>>>
```

<a href='#^'>^^^</a>

---

```python
mf = open('C:\\path\\path\\path\\test.txt')
print(mf.read())
#you can't use read() twice, use the seek as it is described below 
mf.seek(0)
print(mf.read())

>>>
hello world
new line
third line and hello 
hello world
new line
third line and hello 
>>>
```

<a href='#^'>^^^</a>

---

```python
mf = open('C:\\path\\path\\path\\test.txt')

print(mf.readlines())

>>>
['hello world\n', 'new line\n', 'third line and hello ']
>>>
```

<a href='#^'>^^^</a>

---

```python
with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\test.txt') as myfile:
    contents = myfile.read()

print(contents)

>>>
hello world
new line
third line and hello
>>>
```

<a href='#^'>^^^</a>

---

```python
with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\test.txt', mode='a') as myfile:
    contents = myfile.write('hey hey hey')

with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\test.txt', mode='r') as myfile:
    contents = myfile.read()

print(contents)
>>>
hey hey hey
>>>
```

<a href='#^'>^^^</a>

---

```python
with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\zzz.txt', mode='w') as zzz:
    zx = zzz.write('eyyo')

with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\zzz.txt', mode='r') as zzz:
    zx = zzz.read()

print(zx)

>>>
eyyo
>>>
```

<a href='#^'>^^^</a>

---
