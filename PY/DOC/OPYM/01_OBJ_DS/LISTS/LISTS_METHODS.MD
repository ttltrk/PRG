
Lists Methods
======

[tutorialspoint.com](https://www.tutorialspoint.com/python)

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/LISTS/LISTS.MD)

* <a href="#3">append</a>
* <a href="#6">copy()</a>
* <a href="#7">count</a>
* <a href="#8">clear()</a>
* <a href="#9">enumerate()</a>	
* <a href="#10">extend</a>
* <a href="#11">filter()</a>
* <a href="#13">index</a>
* <a href="#14">insert</a>
* <a href="#15">iter()</a>
* <a href="#16">len()</a>	
* <a href="#17">list()</a>
* <a href="#18">map()</a>
* <a href="#19">max()</a>	
* <a href="#20">min()</a>	
* <a href="#12">pop</a>
* <a href="#21">remove</a>
* <a href="#22">reverse</a>
* <a href="#222">reversed</a>
* <a href="#23">slice()</a>
* <a href="#24">sort</a>
* <a href="#244">sorted</a>
* <a href="#25">sum()</a>	
* <a href="#26">zip()</a>

<h4 id="3">append</h4>

Add Single Element to The List

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

<h4 id="6">copy</h4>

Returns Shallow Copy of a List

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

<h4 id="7">count</h4>

returns occurrences of element in a list

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

<h4 id="8">clear</h4>

Removes all Items from the List

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

<h4 id="9">enumerate</h4>

Returns an Enumerate Object

<h4 id="10">extend</h4>

Add Elements of a List to Another List

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

<h4 id="11">filter</h4>

constructs iterator from elements which are true

<h4 id="13">index</h4>

returns smallest index of element in list

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

<h4 id="14">insert</h4>

Inserts Element to The List

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

<h4 id="15">iter</h4>

returns iterator for an object

<h4 id="16">len</h4>

Returns Length of an Object

<h4 id="17">list</h4>

Function	creates list in Python

<h4 id="18">map</h4>

Applies Function and Returns a List

<h4 id="19">max</h4>

returns largest element

<h4 id="20">min</h4>

returns smallest element

<h4 id="12">pop</h4>

Removes Element at Given Index

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

<h4 id="21">remove</h4>

Removes Element from the List

```python
l = [1, 2, 3, 4, 5, 6]
print(l)
l.remove(3)
print(l)

>>>
[1, 2, 3, 4, 5, 6]
[1, 2, 4, 5, 6]
>>>
```

<h4 id="22">reverse</h4>

Reverses a List

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

<h4 id="222">reversed</h4>

returns reversed iterator of a sequence

<h4 id="23">slice</h4>

creates a slice object specified by range()

<h4 id="24">sort</h4>

sorts elements of a list

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

<h4 id="24">sorted</h4>

returns sorted list from a given iterable

<h4 id="25">sum</h4>

Add items of an Iterable

<h4 id="26">zip</h4>

Returns an Iterator of Tuples

