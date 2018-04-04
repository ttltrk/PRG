
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD) - [Python Statements](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/03_PY_ST/PY_ST.MD) - [for loops](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/03_PY_ST/FOR/FORLOOP.MD)

---

### for loops (other examples)

---

```python
l = [1, 2, 3, 4, 5]

for element in l:
    print (element)
	
>>>
1
2
3
4
5
>>>
```

---

```python
l = [1, 2, 3, 4, 5]

for element in l:
    print ("something")
	
>>>
something
something
something
something
something
>>> 
```

---

```python
l = [1, 2, 3, 4, 5]

for num in l:
    if num % 2 == 0:
        print (num)

>>>
2
4
>>> 
```

---

```python
l = [1, 2, 3, 4, 5]

for num in l:
    if num % 2 == 1:
        print (num)

>>>
1
3
5
>>> 
```

---

```python
l = [1, 2, 3, 4, 5]

for num in l:
    if num % 2 == 0:
        print ("here is an even")
    else:
        print ("Odd number!")
		
>>>
Odd number!
here is an even
Odd number!
here is an even
Odd number!
>>> 
```

---

```python
l = [1, 2, 3, 4, 5]
list_sum = 0

for num in l:
    list_sum = list_sum + num

print (list_sum)

>>>
15
>>>
```

---

```python
l = ("a", "b", "c")
lst = ""

for abc in l:
    lst = lst + abc

print (lst)

>>>
abc
>>>
```

---

```python
l = [1, 2, 3, 4, 5]
list_sum = 0

for num in l:
    list_sum += num

print (list_sum)

>>>
15
>>>
```

---

```python
s = "this is a string!"

for item in s:
    print (item)
	
>>>
t
h
i
s
 
i
s
 
a
 
s
t
r
i
n
g
!
>>> 
```

---

```python
tup = (1, 2, 3, 4, 5)

for t in tup:
    print (t)
	
>>>
1
2
3
4
5
>>> 
```

---

```python
l = [(2,4),(6,8),(10,12)]

for tup in l:
    print (tup)
	
>>>
(2, 4)
(6, 8)
(10, 12)
>>> 
```

---

```python
l = [(2,4),(6,8),(10,12)]

for (t1, t2) in l:
    print (t1)
	
>>>
2
6
10
>>> 
```

---

```python
l = [(2,4),(6,8),(10,12)]

for (t1, t2) in l:
    print (t2)
	
>>>
4
8
12
>>> 
```

---

```python
l = [(2,4),(6,8),(10,12)]

for (t1, t2) in l:
    print (t1 - t2)
	
>>>
-2
-2
-2
>>> 
```

---

```python
d = {"k1" : 1, "k2" : 2, "k3" : 3}

for item in d:
    print (item)
	
>>>
k3
k1
k2
>>>
```

---

```python
d = {"k1" : 1, "k2" : 2, "k3" : 3}

for k, v in d.items():
    print (k)
    print (v)
	
>>>
k2
2
k1
1
k3
3
>>> 
```

---
