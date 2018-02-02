
Generators
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD)

[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Iterators%20and%20Generators.ipynb)

```python
def gencubes(n):
  for num in range(n):
    yield num**3
    
for x in gencubes(10):
  print(x)
  
>>>
0
1
8
27
64
125
216
343
512
729
>>>
```

```python
def genfibon(n):
  a = 1
  b = 1
  
  for i in range(n):
    yield a
    t = a
    a = b
    b = t+b 

for num in genfibon(10):
  print(num)
  
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
def fibon(n):
  a = 1
  b = 1
  
  output = []
  
  for i in range(n):
    output.append(a)
    a,b = b, a+b 
    
  return output
  
print(fibon(10))

>>>
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>>
```

```python
def simple_gen():
  for x in range(3):
    yield x
    
g = simple_gen()

print(next(g))
print(next(g))
print(next(g))

>>>
0
1
2
>>>
```

```python
s = 'hello'

for let in s:
  print(let)
  
>>>
h
e
l
l
o
>>>
```

```python
s = 'hello'

s_iter = iter(s)

print(next(s_iter))

>>>
h
>>>
```

```python
s = 'hello'
s_iter = iter(s)

print(next(s_iter))
print('+')
print(next(s_iter))
print('+')
print(next(s_iter))
print('+')
print(next(s_iter))
print('+')
print(next(s_iter))

>>>
h
+
e
+
l
+
l
+
o
>>>
```
