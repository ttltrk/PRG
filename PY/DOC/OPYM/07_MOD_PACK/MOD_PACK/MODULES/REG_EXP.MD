
Regular Expressions
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/07_MOD_PACK/MOD_PACK/MOD_PACK.MD)

[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Regular%20Expressions.ipynb)

```python
import re

patterns = ['t1', 't2']
text = 'This is a string with t1, but not the other t'

print(re.search('hello', 'hello world!'))

>>>
<_sre.SRE_Match object; span=(0, 5), match='hello'>
>>>
```

```python
import re

patterns = ['t1', 't2']
text = 'This is a string with t1, but not the other t'

match = re.search(patterns[0], text)

print(match.start())
print(match.end())

>>>
22
24
>>>
```

```python
import re

split_term = '@'

phrase = 'What is your email, is it hello@gmail.com?'

print(re.split(split_term, phrase))

>>>
['What is your email, is it hello', 'gmail.com?']
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
