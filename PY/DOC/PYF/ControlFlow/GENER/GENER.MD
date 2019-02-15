
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [CF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/ControlFlow/CF.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Control Flow - generators</h3>

---

```python
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(10))

>>>
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>>
```

```python
def gen_fibon(n):

    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for number in gen_fibon(10):
    print(number)
    
>>>
1
1
2
3
5
8
13
21
34
55
>>>
```

```python
def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)
    
>>>
0
1
2
>>>
```

```python
def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()

print(next(g))

>>>
0
1
2
0
>>>
```

```python
s = 'hello'

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))

>>>
h
e 
>>>
```

```python
def gensquares(N):
    for i in range(N):
        yield i**2

for x in gensquares(10):
    print(x)
    
>>>
0
1
4
9
16
25
36
49
64
81
>>>
```

```python
import random

random.randint(1,10)

def rand_num(low,high,n):

    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)
    
>>>
2
9
7
4
6
9
10
4
4
3
5
9
>>>
```

```python
s = 'hello'
s = iter(s)
print(next(s))

>>>
h
>>>
```

```python
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item>3)

for item in gencomp:
    print(item)

>>>
4
5
>>>
```

<a href='#^'>^^^</a>

---
