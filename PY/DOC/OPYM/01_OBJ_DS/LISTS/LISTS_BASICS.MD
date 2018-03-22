
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD) - [Objects and Data Structures](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/OBJ_DS.MD) - [Lists](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/LISTS/LISTS.MD)

---

### Python List Basics

---

* [Create a List](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/LISTS/01_LB/CRE_LIS.MD)
* [Nested List]()
* [List Index]()
* [Nested Indexing]()
* [Negative Indexing]()
* [Slice Lists]()

---

[src - programiz](https://www.programiz.com/python-programming/list)

---

<h4 id="2">Nested list</h4>

```python
# nested list
my_list = ["mouse", [8, 4, 6], ['a']]

print(my_list)

>>>
['mouse', [8, 4, 6], ['a']]
>>>
```

---

<h4 id="3">List index</h4>

```python
my_list = ['p','r','o','b','e']

print(my_list[0])
print(my_list[2])
print(my_list[4])

>>>
p
o
e
>>>
```

<h4 id="4">Nested indexing</h4>

```python
n_list = ["Happy", [2,0,1,5]]

print(n_list[0][1])    
print(n_list[1][3])

>>>
a
5
>>>
```

<h4 id="5">Negative indexing</h4>

```python
my_list = ['p','r','o','b','e']

print(my_list[-1])
print(my_list[-5])

>>>
e
p
>>>
```
---

<h4 id="6">Slice lists</h4>

```python
my_list = [1, 2, 3, 4, 5, 6, 7]

print(my_list[2:5])
print(my_list[:-5])
print(my_list[5:])
print(my_list[:])

>>>
[3, 4, 5]
[1, 2]
[6, 7]
[1, 2, 3, 4, 5, 6, 7]
>>>
```

---

