
zip()
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/04_MET_FUN/FUNCTIONS/BUILT_IN_FUNCTIONS.MD)

[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Zip.ipynb)

```python
x = [1, 2, 3]
y = [4, 5, 6]

z = list(zip(x,y))

print(z)

>>>
[(1, 4), (2, 5), (3, 6)]
>>>
```

```python
a = [1, 2, 3, 4, 5]
b = [2, 2, 10, 1, 1]

for pair in zip(a,b): 
  print(max(pair))
  
>>>
2
2
10
4
5
>>>
```

```python
d1 = {'a': 1 , 'b': 2}
d2 = {'c': 3 , 'd': 4}

print(list(zip(d1, d2)))

>>>
[('a', 'c'), ('b', 'd')]
>>>
```

