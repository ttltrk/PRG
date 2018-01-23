
reduce()
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/04_MET_FUN/FUNCTIONS/BUILT_IN_FUNCTIONS.MD)

[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Reduce.ipynb)

```python
lst = [1, 2, 3, 4, 5]

print(max(lst))

>>>
5
>>>
```

```
import functools

lst = [1, 2, 3, 4, 5]
max_find = lambda a,b: a if (a>b) else b

print(functools.reduce(max_find,lst))

>>>
5
>>>
```
