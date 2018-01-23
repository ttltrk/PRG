
filter()
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/04_MET_FUN/FUNCTIONS/BUILT_IN_FUNCTIONS.MD)

[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Filter.ipynb)

```python
def even_check(num):
  if num % 2 == 0: 
    return True
  else: 
    return False
    
print(even_check(4))
print(even_check(5))

>>>
True
False
>>>
```

```python
def even_check(num):
  if num % 2 == 0: 
    return True
  else: 
    return False
    
even_check(35)

lst = range(10)

f = filter(even_check, lst)

print(f)

>>>
<filter object at 0x7f4d216a1be0>
>>>
```

