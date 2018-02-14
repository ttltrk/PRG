
Python List Basics
======

[programiz.com](https://www.programiz.com/python-programming/list)

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/LISTS/LISTS.MD)

---

* <a href="#1">Create a list</a>
* <a href="#2">Nested list</a>
* <a href="#3">List index</a>
* <a href="#4">Nested indexing</a>
* <a href="#5">Negative indexing</a>
* <a href="#6">Slice lists</a>

---

<h4 id="1">Create a list</h4>

```python
# empty list
my_list = []
print(my_list)

# list of integers
my_list = [1, 2, 3]
print(my_list)

# list with mixed datatypes
my_list = [1, "Hello", 3.4]
print(my_list)

>>>
[]
[1, 2, 3]
[1, 'Hello', 3.4]
>>>
```

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

