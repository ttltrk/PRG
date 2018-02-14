
Lists Methods
======

[tutorialspoint.com](https://www.tutorialspoint.com/python)

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/LISTS/LISTS.MD)

* <a href="#1">all()</a>
* <a href="#2">any()</a>
* <a href="#3">append</a>
* <a href="#4">ascii()</a>
* <a href="#5">bool()</a>
* <a href="#6">copy()</a>
* <a href="#7">count</a>
* <a href="#8">clear()</a>
* <a href="#9">enumerate()</a>	
* <a href="#10">extend</a>
* <a href="#11">filter()</a>
* <a href="#12">pop</a>
* <a href="#13">index</a>
* <a href="#14">insert</a>
* <a href="#15">iter()</a>
* <a href="#16">len()</a>	
* <a href="#17">list()</a>
* <a href="#18">map()</a>
* <a href="#19">max()</a>	
* <a href="#20">min()</a>	
* <a href="#21">remove</a>
* <a href="#22">reverse</a>
* <a href="#222">reversed</a>
* <a href="#23">slice()</a>
* <a href="#24">sort</a>
* <a href="#244">sorted</a>
* <a href="#25">sum()</a>	
* <a href="#26">zip()</a>

<h4 id="1">all</h4>

returns true when all elements in iterable is true

<h4 id="2">any</h4>

Checks if any Element of an Iterable is True

<h4 id="3">append</h4>

Add Single Element to The List

<h4 id="4">ascii</h4>

Returns String Containing Printable Representation

<h4 id="5">bool</h4>

Coverts a Value to Boolean

<h4 id="6">copy</h4>

Returns Shallow Copy of a List

<h4 id="7">count</h4>

returns occurrences of element in a list

<h4 id="8">clear</h4>

Removes all Items from the List

<h4 id="9">enumerate</h4>

Returns an Enumerate Object

<h4 id="10">extend</h4>

Add Elements of a List to Another List

<h4 id="11">filter</h4>

constructs iterator from elements which are true

<h4 id="12">pop</h4>

Removes Element at Given Index

<h4 id="13">index</h4>

returns smallest index of element in list

<h4 id="14">insert</h4>

Inserts Element to The List

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

<h4 id="21">remove</h4>

Removes Element from the List

<h4 id="22">reverse</h4>

Reverses a List

<h4 id="222">reversed</h4>

returns reversed iterator of a sequence

<h4 id="23">slice</h4>

creates a slice object specified by range()

<h4 id="24">sort</h4>

sorts elements of a list

<h4 id="24">sorted</h4>

returns sorted list from a given iterable

<h4 id="25">sum</h4>

Add items of an Iterable

<h4 id="26">zip</h4>

Returns an Iterator of Tuples

<h4 id="1">Append</h4>

In order append() an element onto an array, call the method with the element in the parenthesis.

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

<h4 id="2">Pop</h4>

The pop() method can work in two different ways. If you leave the parenthesis empty, it works as the opposite of append().

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.pop()
print(linux_distros)

>>>
['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch']
>>>

linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch']
linux_distros.pop()
print(linux_distros)

>>>
['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE']
>>>

linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch']
linux_distros.pop(1)
print(linux_distros)

>>>
['Debian', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch']
>>>
```

<h4 id="3">Insert</h4>

In order to use insert() to place a new element into a list, you have to specify the index where you want to insert your new element and the element that you want to insert.

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.insert(2, "Mint")
print(linux_distros)

>>>
['Debian', 'Ubuntu', 'Mint', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
>>>

print(linux_distros[4])

>>>
CentOS
>>>
```

<h4 id="4">Remove</h4>

remove() works sort of like giving pop an index to remove, but instead of giving remove() an index you give it the actual value of the element. It will find and remove the first occurrence of that value in the list. So, be sure that the first occurrence is the one that you want to remove. Otherwise, it's probably best to figure out the index of the element that you do want to remove and use pop().

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.remove("Arch")
print(linux_distros)

>>>
['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Gentoo']
>>>
```

<h4 id="5">Extend</h4>

extend() adds two lists together. It adds the list in parenthesis to the list that it is being called on.

```python
linux_distros = ['Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
debian_distros = ['Debian', 'Ubuntu', 'Mint']
linux_distros.extend(debian_distros)
print(linux_distros)

>>>
['Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo', 'Debian', 'Ubuntu', 'Mint']
>>>
```

<h4 id="6">Index</h4>

There is a way to find out the index of an element, and that's the index() method. Like with the others, index() finds the first occurrence of an element, not every occurrence.

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
print(linux_distros.index("Arch"))

>>>
5
>>>
```

<h4 id="7">Sort</h4>

If you need to sort a list, either alphabetically or numerically, Python has you covered there as well. Just call the sort() method on the list, and it will be saved in the new order. This will overwrite the previous list, so create a copy to sort, if you need to preserve the original.

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.sort()
print(linux_distros)

>>>
['Arch', 'CentOS', 'Debian', 'Fedora', 'Gentoo', 'OpenSUSE', 'Ubuntu']
>>>
```

```python
numbers_to_sort = [1, 5, 8, 16, 3, 75, 4, 23, 9, 15, 8, 32]
numbers_to_sort.sort()
print(numbers_to_sort)

>>>
[1, 3, 4, 5, 8, 8, 9, 15, 16, 23, 32, 75]
>>>
```

<h4 id="8">Reverse</h4>

reverse() is a bit of an odd method. It reverses the order of elements in a list in place and saves it. It doesn't put them in any kind of special order, it just flips the list around.

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.reverse()
print(linux_distros)

>>>
['Gentoo', 'Arch', 'OpenSUSE', 'CentOS', 'Fedora', 'Ubuntu', 'Debian']
>>>
```

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.sort()
linux_distros.reverse()
print(linux_distros)

>>>
['Ubuntu', 'OpenSUSE', 'Gentoo', 'Fedora', 'Debian', 'CentOS', 'Arch']
>>>
```

<h4 id="9">Count</h4>

You can count the number of element of a kind:

[01](https://repl.it/repls/TragicUnsightlyMarabou)

```python
ln = [1, 2, 3, 4, 5, 1, 1, 2, 3, 1]
lw = ['a', 'a', 'b', 'c', 'a', 'd']

print(ln.count(1))
print(ln.count(4))
print(lw.count('a'))
print(lw.count('b'))

>>>
4
1
3
1
>>>
```
