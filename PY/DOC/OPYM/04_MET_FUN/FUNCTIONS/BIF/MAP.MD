
Map
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/04_MET_FUN/FUNCTIONS/BUILT_IN_FUNCTIONS.MD)

[jupyter](https://www.udemy.com/complete-python-bootcamp/learn/v4/t/lecture/3512786?start=15) | 
[book.pythontips](http://book.pythontips.com/en/latest/map_filter.html)

```python
def farenheit(T):
  return (9.0/5)*T + 32
  
print(farenheit(10))

>>>
50.0
>>>
```

```python
def fahrenheit(T):
  return (9.0/5)*T + 32
  
temp = [0, 22.5, 40, 100]

print(map(fahrenheit, temp))

>>>
<map object at 0x7f0c4701afd0>
>>>
```

```python
temp = [2, 10, 15]

x = list(map(lambda T: (9.0/5)*T + 32, temp))

print(x)

>>>
[35.6, 50.0, 59.0]
>>>
```

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

x = list(map(lambda x, y: x+y, a, b))

print(x)

>>>
[5, 7, 9]
>>>
```

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

x = list(map(lambda x, y, z: x+y+z, a, b, c))

print(x)

>>>
[12, 15, 18]
>>>
```

```python
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

print(squared)

>>>
[1, 4, 9, 16, 25]
>>>
```
