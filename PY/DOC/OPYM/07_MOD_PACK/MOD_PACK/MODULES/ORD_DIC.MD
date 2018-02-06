
OrderedDict
======

[<<<]()

[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Collections%20Module.ipynb)

```python
d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d)

>>>
{'a': 1, 'b': 2, 'c': 3}
>>>
```

```python
d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['e'] = 4
d['f'] = 5

for k,v in d.items():
  print(k,v)
  
>>>
a 1
b 2
c 3
e 4
f 5
>>>
```

```python
from collections import OrderedDict

d = OrderedDict()

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['e'] = 4
d['f'] = 5

for k,v in d.items():
  print(k,v)
  
>>>
a 1
b 2
c 3
e 4
f 5
>>>
```
