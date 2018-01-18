
Map
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/04_MET_FUN/FUNCTIONS/BUILT_IN_FUNCTIONS.MD)

[jupyter](https://www.udemy.com/complete-python-bootcamp/learn/v4/t/lecture/3512786?start=15)

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
