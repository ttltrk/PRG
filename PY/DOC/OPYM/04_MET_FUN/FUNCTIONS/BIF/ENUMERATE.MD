
enumerate()
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/04_MET_FUN/FUNCTIONS/BUILT_IN_FUNCTIONS.MD)

[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Enumerate.ipynb)

```python
l = ['a', 'b', 'c']

for item in l:
  print(item)

>>>
a
b
c
>>>
```


```python
l = ['a', 'b', 'c']

count = 0
for item in l:
  print(count)
  print(item)
  count += 1

>>>
0
a
1
b
2
c
>>>
```


```python
l = ['a', 'b', 'c']

for (count, item) in enumerate(l):
  print(count)
  print(item)
  
>>>
0
a
1
b
2
c
>>>
```


```python
l = ['a', 'b', 'c']

for (count, item) in enumerate(l):
  if count >=2:
    break
  else:
    print(item)
    
>>>
a
b
>>>
```


```python

>>>

>>>
```


```python

>>>

>>>
```


```python

>>>

>>>
```


```python

>>>

>>>
```
