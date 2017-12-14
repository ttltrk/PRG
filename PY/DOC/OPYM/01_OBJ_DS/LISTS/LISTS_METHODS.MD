
Lists Methods
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/LISTS/LISTS.MD)

* <a href="#1">Append</a>
* <a href="#2">Pop</a>
* <a href="#3">Insert</a>
* <a href="#4">Remove</a>
* <a href="#5">Extend</a>
* <a href="#6">Index</a>
* <a href="#7">Sort</a>
* <a href="#8">Reverse</a>
* <a href="#9">Count</a>

<h4 id="1">Append</h4>

In order append() an element onto an array, call the method with the element in the parenthesis.

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.append("Mint")
print(linux_distros)

>>>
['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo', 'Mint']
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
