
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [CF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/ControlFlow/CF.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Control Flow - for</h3>

---

---
<h4 id='^^for'></h4>
<a href ='#basscr'>Basic script</a><br>
<a href ='#odevnu'>Odd and Even numbers</a><br>
<a href ='#sumlis'>Sum of the list</a><br>
<a href ='#mullis'>Multiply two lists
<a href ='#itestr'>Iterate a string</a><br>
<a href ='#itetup'>Iterate tuples</a><br>
<a href ='#itedic'>Iterate dictionary</a><br>
<a href ='#forran'>for with range()</a><br><br>
<a href ='#passfor'>pass for</a>
<a href ='#confor'>continue for</a>
<a href ='#brkfor'>break for</a>
<a href ='#enufor'>enumerate for</a>
<a href='#^'>^^^</a>

---

<h4 id='basscr'>Basic script</h4>

```python
#python for
l = [1,2,3]

for n in l:
    print(l)

>>>
1
2
3
>>>
```

<a href='#^^for'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='odevnu'>Odd and Even numbers</h4>

```python
#python for
l = [1,2,3, 4, 5, 6, 7, 8, 9, 10]
for num in l:
    if num % 2 == 0:
        print(num)
    else:
        print(f'odd number:{num}')
	
>>>
odd number:1
2
odd number:3
4
odd number:5
6
odd number:7
8
odd number:9
10
>>>
```

<a href='#^^for'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='sumlis'>Sum of the list</h4>

```python
#python for
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

sum = 0

for val in numbers:
	sum = sum+val

print("The sum is", sum)

>>>
The sum is 48
>>>
```

<a href='#^^for'>^^</a><br>
<a href='#^'>^^^</a>

```python
#python for
#how to count the sum of the list = final number
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ls = 0

for num in l:
    ls = ls + num

print(ls)

>>>
55
>>>
```

<a href='#^^for'>^^</a><br>
<a href='#^'>^^^</a>

```python
#python for
#how to count the sum of the list = the whole chain
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ls = 0

for num in l:
    ls = ls + num

    print(ls)
    
>>>
1
3
6
10
15
21
28
36
45
55
>>>
```

<a href='#^^for'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='mullis'>Multiply two lists</h4>

```python
# elements by elements
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']

for item in zip(l1, l2):
    print(item)
    
>>>
(1, 'a')
(2, 'b')
(3, 'c')
>>>
```

```python
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
l3 = [100, 200, 300]

for item in zip(l1, l2, l3):
    print(item)
    
>>>
(1, 'a', 100)
(2, 'b', 200)
(3, 'c', 300)
>>>
```

---

<h4 id='itestr'>Iterate a string</h4>

```python
#python for
s = 'trk'

for letters in s:
    print(letters)
    
>>>
t
r
k
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

```python
#python for
for letters in 'trk':
    print(letters)
    
>>>
t
r
k
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

```python
#python for
for _ in 'trk':
    print('hey')
    
>>>
trk
trk
trk
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

---

<h4 id='itetup'>Iterate tuples</h4>

```python
#python for
l = [(1,2),(3,4),(5,6),(7,8)]
print(len(l))

for n in l:
    print(n)
    
>>>
4
(1, 2)
(3, 4)
(5, 6)
(7, 8)
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

```python
#python for
l = [(1,2),(3,4),(5,6),(7,8)]

for (a,b) in l:
    print(a)
    print(b)
    
>>>
1
2
3
4
5
6
7
8
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

```python
#python for
l = [(1,2),(3,4),(5,6),(7,8)]

for a,b in l:
    print(a)
    
>>>
1
3
5
7
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

```python
#python for
l = [(1, 2, 3),(4, 5, 6),(7, 8, 9)]

for a, b, c in l:
    print(b)
    
>>>
2
5
8
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

---

<h4 id='itedic'>Iterate dictionary</h4>

```python
#python for
d = {'k1':1, 'k2':2, 'k3':3}

for k,v in d.items():
    print(k)
 
>>>
k1
k2
k3
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>


```python
#python for
d = {'k1':1, 'k2':2, 'k3':3}

for k,v in d.items:
    print(v)
    
>>>
1
2
3
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

```python
#python for
d = {'k1':1, 'k2':2, 'k3':3}

for item in d.items():
    print(item)
    
>>>
('k1', 1)
('k2', 2)
('k3', 3)
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

---

<h4 id='forran'>for with range()</h4>

```python
#python for
genre = ['pop', 'rock', 'jazz']

for i in range(len(genre)):
	print("I like", genre[i])

>>>
I like pop
I like rock
I like jazz
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

```python
#python for
l = [1, 2, 3, 4, 5]

for num in range(1,11):
    print (num)
	
>>>
1
2
3
4
5
6
7
8
9
10
>>> 
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

```python
#python for
for element in range(5):
    print ("hello world")

>>>
hello world
hello world
hello world
hello world
hello world
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

---

<h4 id='passfor'>pass for</h4>

```python
x = [1, 2, 3]

for nums in x:
    pass

print('how to use pass')

>>>
how to use pass
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

---

<h4 id='confor'>continue for</h4>

```print
x = 'sammy'

for letter in x:
    if letter == 'a':
        continue
    print(letter)
    
>>>
s
m
m
y
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

---

<h4 id='brkfor'>break for</h4>

```python
x = 'sammy'

for letter in x:
    if letter == 'a':
        break
    print(letter)

>>>
s
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

---

<h4 id='enufor'>enumerate for</h4>

```python
index_count = 0

for letter in 'abc':
    print('at index {} the letter is {}'.format(index_count, letter))
    index_count += 1
    
>>>
at index 0 the letter is a
at index 1 the letter is b
at index 2 the letter is c
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

---

```python
word = 'abc'

for item in enumerate(word):
    print(item)
    
>>>
(0, 'a')
(1, 'b')
(2, 'c')
>>>
```

---

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

```python
word = 'abc'

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')
    
>>>
0
a


1
b


2
c
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

---

