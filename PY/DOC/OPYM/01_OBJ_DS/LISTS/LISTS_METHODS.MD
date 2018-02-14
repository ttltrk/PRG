
Python List Methods
======

[tutorialspoint.com](https://www.tutorialspoint.com/python) |
[programiz.com](https://www.programiz.com/python-programming/methods/list)

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/LISTS/LISTS.MD)

* Python has some list methods that you can use to perform frequency occurring task (related to list) with ease. 

---

* <a href="#3">append()</a>
* <a href="#6">copy()</a>
* <a href="#7">count()</a>
* <a href="#8">clear()</a>
* <a href="#10">extend()</a>
* <a href="#13">index()</a>
* <a href="#14">insert()</a>
* <a href="#12">pop</a>
* <a href="#21">remove</a>
* <a href="#22">reverse</a>
* <a href="#24">sort</a>

---

<h4 id="3">append</h4>

The append() method adds a single item to the existing list. It doesn't return a new list; rather it modifies the original list.

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

---

<h4 id="6">copy</h4>

The copy() method returns a shallow copy of the list.

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

---

<h4 id="7">count</h4>

The count() method returns the number of occurrences of an element in a list.

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

---

<h4 id="8">clear</h4>

The clear() method removes all items from the list.

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

---

<h4 id="10">extend()</h4>

The extend() extends the list by adding all items of a list (passed as an argument) to the end.

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

---

<h4 id="13">index</h4>

The index() method searches an element in the list and returns its index.

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

---

<h4 id="14">insert</h4>

The insert() method inserts the element to the list at the given index.

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

---

<h4 id="12">pop</h4>

The pop() method removes and returns the element at the given index (passed as an argument) from the list.

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

---

<h4 id="21">remove</h4>

The remove() method searches for the given element in the list and removes the first matching element.

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

---

<h4 id="22">reverse</h4>

The reverse() method reverses the elements of a given list.

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

---

<h4 id="24">sort</h4>

The sort() method sorts the elements of a given list.

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

---

