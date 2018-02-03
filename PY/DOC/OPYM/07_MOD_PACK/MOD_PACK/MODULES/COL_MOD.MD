
Collections Modules
======

[]()

[jupyter](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Collections%20Module.ipynb)

```python
from collections import Counter

l = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4]

print(Counter(l))

>>>
Counter({1: 6, 4: 6, 2: 3, 3: 1})
>>>
```

```python
from collections import Counter

s = 'aaaaseddfjdkfjieedjaskjfsidljfcidksfcikm'

print(Counter(s))

>>>
Counter({'d': 6, 'a': 5, 'f': 5, 'j': 5, 's': 4, 'k': 4, 'i': 4, 'e': 3, 'c': 2, 'l': 1, 'm': 1})
>>>
```

```python
from collections import Counter

s = 'word word up word up show word up up up up'

word = s.split()

print(Counter(word))

>>>
Counter({'up': 6, 'word': 4, 'show': 1})
>>>
```
