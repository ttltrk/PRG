
Lists
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD)

* [[python.org](https://docs.python.org/3/tutorial/introduction.html#lists)]
* [[linuxconfig](https://linuxconfig.org/python-list-methods)]
* [[dev.google](https://developers.google.com/edu/python/lists)]
* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Lists.ipynb)]
* [[digitalocean](https://www.digitalocean.com/community/tutorials/understanding-lists-in-python-3)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/lists.html)]

```python
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
>>> squares[:]
[1, 4, 9, 16, 25]
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

```python
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```

```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```

```python
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```

List methods

Append

In order append() an element onto an array, call the method with the element in the parenthesis.

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.append("Mint")
print(linux_distros)

>>>
['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo', 'Mint']
>>>
```

Pop

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

Insert

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

Remove

remove() works sort of like giving pop an index to remove, but instead of giving remove() an index you give it the actual value of the element. It will find and remove the first occurrence of that value in the list. So, be sure that the first occurrence is the one that you want to remove. Otherwise, it's probably best to figure out the index of the element that you do want to remove and use pop().

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.remove("Arch")
print(linux_distros)

>>>
['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Gentoo']
>>>
```

Extend

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

Index

There is a way to find out the index of an element, and that's the index() method. Like with the others, index() finds the first occurrence of an element, not every occurrence.

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
print(linux_distros.index("Arch"))

>>>
5
>>>
```

Sort

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

Reverse

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

```
list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
list.sort() -- sorts the list in place (does not return it). (The sorted() function shown below is preferred.)
list.reverse() -- reverses the list in place (does not return it)
list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
```
