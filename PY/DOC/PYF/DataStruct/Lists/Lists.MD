
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [DS](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DataStruct/DS.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Data Structures - Lists</h3>

---

* <a href='#listtostr'>list to string</a><br>
* <a href='#listtotup'>list to tuple</a><br>
* <a href='#listtodict'>list to dictionary</a>
* <a href='#listtoset'>list to set</a>

---

<h4 id='listtostr'>list to string</h4>

```python
list1 = ['1', '2', '3']
str1 = ''.join(list1)
str2 = ' '.join(list1)
str3 = '-'.join(list1)
str4 = 'x'.join(list1)

print(str1)
print(str2)
print(str3)
print(str4)

>>>
123
1 2 3
1-2-3
1x2x3
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='listtotup'>list to tuple</h4>

```python
l = [4,5,6]
t = tuple(l)

print(l)
print(t)

>>>
[4, 5, 6]
(4, 5, 6)
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='listtodict'>list to dictionary</h4>

```python
l = ['bi','double','duo','two']

d = dict((k,2) for k in l)

print(d)

>>>
{'bi': 2, 'double': 2, 'duo': 2, 'two': 2}
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='listtoset'>list to set</h4>

```python
l1 = ['bi','double','duo','two']
l2 = [1, 2, 3, 4, 5]

s1 = set(l1)
s2 = set(l2)

print(s1)
print(s2)

>>>
{'two', 'bi', 'double', 'duo'}
{1, 2, 3, 4, 5}
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='uniqueel'>find a unique element</h4>

```python
def find_uniq(arr):
    if (arr[0] == arr[1]) or (arr[0] != arr[1] and arr[0] == arr[2]):
        repeatableNum = arr[0]
    else:
        repeatableNum = arr[1]
    for nums in arr:
        if nums != repeatableNum:
            return nums

print(find_uniq(arr = [ 3, 10, 3, 3, 3 ]))

>>>
10
>>>
```

<a href='#^'>^^^</a>

---

```python
a = [1,2,3]
print(a)

a[2]=4
print(a)

>>>
[1, 2, 3]
[1, 2, 4]
>>>
```

<a href='#^'>^^^</a>

---

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

<a href='#^'>^^^</a>

---

```python
# nested list
my_list = ["mouse", [8, 4, 6], ['a']]

print(my_list)

>>>
['mouse', [8, 4, 6], ['a']]
>>>
```

<a href='#^'>^^^</a>

---

```python
#min max
l1 = [1, 2, 3, 50, 60, 100]

print(min(l1))
print(max(l1))

>>>
1
100
>>>
```

---

```python
my_list = ['p','r','o','b','e']

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

>>>
p
r
o
b
e
>>>
```

<a href='#^'>^^^</a>

---

```python
n_list = ["Happy", [2,0,1,5]]

print(n_list[0][1])    
print(n_list[1][3])

>>>
a
5
>>>
```

<a href='#^'>^^^</a>

---

```python
my_list = ['p','r','o','b','e']

print(my_list[-1])
print(my_list[-5])

>>>
e
p
>>>
```

<a href='#^'>^^^</a>

---

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

<a href='#^'>^^^</a>

---

```python
lst = ["apple", "banana", "cherry"]

print(lst)

lst[1] = "blackcurrant"

print(lst)

>>>
['apple', 'banana', 'cherry']
['apple', 'blackcurrant', 'cherry']
>>>
```

<a href='#^'>^^^</a>

---

```python
lst = ["apple", "banana", "cherry"]
lst.append("damson")

print(lst)
print(lst * 2)

>>>
['apple', 'banana', 'cherry', 'damson']
['apple', 'banana', 'cherry', 'damson', 'apple', 'banana', 'cherry', 'damson']
>>>
```

<a href='#^'>^^^</a>

---

```python
lst = ["apple", "banana", "cherry"]

print(lst)

lst.remove("banana")

print(lst)
print(len(lst))

>>>
['apple', 'banana', 'cherry']
['apple', 'cherry']
2
>>>
```

<a href='#^'>^^^</a>

---

```python
print(range(10))
print(list(range(10)))
print(list(range(2, 8)))
print(list(range(2, 20, 3)))

>>>
range(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 3, 4, 5, 6, 7]
[2, 5, 8, 11, 14, 17]
>>>
```

<a href='#^'>^^^</a>

---

```python
>>> x = range(1,5)
>>> type (x)
<class 'range'>
>>> 
```

<a href='#^'>^^^</a>

---

```python
>>> list(range(0, 10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
```

<a href='#^'>^^^</a>

---

```python
>>> list(range(20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 
```

<a href='#^'>^^^</a>

---

```python
>>> x = list(range(0,10))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> type(x)
<class 'list'>
>>> 
```

<a href='#^'>^^^</a>

---

```python
>>> start = 5
>>> stop = 20
>>> list(range(start,stop))
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 
```

<a href='#^'>^^^</a>

---

```python
>>> start = 5
>>> stop = 20
>>> list(range(start,stop,2))
[5, 7, 9, 11, 13, 15, 17, 19]
>>>
```

---
