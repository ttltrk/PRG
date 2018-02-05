
Module - Default Dictionary
======

[]()

[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Collections%20Module.ipynb)

```python
from collections import defaultdict

d = {'k1':1}
print(d['k1'])
print(d['k2'])

>>>
1
Traceback (most recent call last):
  File "python", line 5, in <module>
KeyError: 'k2'
>>>
```

```python
from collections import defaultdict

d = defaultdict(object)
print(d['one'])

>>>
<object object at 0x7f68d4d69250>
>>>
```

```python
from collections import defaultdict

d = defaultdict(object)

d['one']

for item in d:
  print(item)
  
>>>
one
>>>
```

```python
from collections import defaultdict

d = defaultdict(lambda: 0)

print(d['one'])

>>>
0
>>>
```

