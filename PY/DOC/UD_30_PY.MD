
[30 Days of Python](https://www.udemy.com/30-days-of-python/learn/v4/content)
======

### Welcome
  * <a href='#1'>Welcome</a>
  * <a href='#2'>Getting help</a>
  * <a href='#3'>Youtube and Suggestions</a>

### Days 1: Basics
  * <a href='#4'>Setup, String, Variables and Integers</a>

### Day 2 & 3 - Lists, Dictionaries, Tuples and Loops
  * <a href='#5'>Lists</a>
  * <a href='#6'>Dictionaries and Tuples</a>
  * <a href='#7'>Loops: For Loops and While Loops</a>

### Section 4

### Section 5

### Section 6

### Section 7

### Section 8

### Section 9

### Section 10

### Section 11

### Section 12

### Section 13

### Section 14

### Section 15

Welcome
------

#### <h4 id='1'>Welcome</h4>

#### <h4 id='2'>Getting help</h4>

#### <h4 id='3'>Youtube and Suggestions</h4>

Days 1: Basics
------

#### <h4 id='4'>Setup, String, Variables and Integers</h4>

STRINGS

```python
print("this is a word")

>>>
this is a word
>>>
```

```python
print("this is a" + " another string")

>>>
this is a another string
>>>
```

VARIABLES

```python
abc = "some string"
print(abc)

>>>
some string
>>>
```

```python
abc = "some string"
print(abc + abc)

>>>
some stringsome string
>>>
```

NUMBERS

```python
a = 2 * 2
print(a)

b = 2 * "2"
print(b)

>>>
4
22
>>>
```

Day 2 & 3 - Lists, Dictionaries, Tuples and Loops
------

#### <h4 id='5'>Lists</h4>

```python
l = ['some string', 123, 'another string']
print(l)

>>>
['some string', 123, 'another string']
>>>
```

```python
l = ['some string', 123, 'another string']
l.append(456)
print(l)

>>>
['some string', 123, 'another string', 456]
>>>
```

```python
l = ['some string', 123, 'another string', 456]
l.pop()
print(l)

>>>
['some string', 123, 'another string']
>>>
```

```python
l = ['some string', 123, 'another string', 456]
print(len(l))

>>>
4
>>>
```

```python
l = ['some string', 123, 'another string', 456]
print(l[0])

>>>
some string
>>>
```

```python
another_list = ['John', 'Jack', 'James']
james_name = another_list[2]
print(james_name)

>>>
James
>>>
```

#### <h4 id='6'>Dictionaries and Tuples</h4>

Dictionaries

```python
a_dict = {"abc":"A string"}
print(a_dict)

>>>
{'abc': 'A string'}
>>>
```

```python
a_dict = {"abc":"A string"}
a_dict["abc"] = "another new string"
a_dict["def"] = "string too"

print(a_dict)
print(a_dict["abc"])

>>>
{'abc': 'another new string', 'def': 'string too'}
another new string
>>>
```

```python
new_abc = {"0":"another string", "yetanother":"another"}
sss = {"f":"123"}
new_abc["yetanother"] = sss
print(new_abc)

>>>
{'0': 'another string', 'yetanother': {'f': '123'}}
>>>
```

Tuples

```python
tup = ("abc", "123")
print(tup)

>>>
('abc', '123')tup = (("abc", "123"), ("def"))
>>>
```

```python
tup = (("abc", "123"), ("def"))
print(tup)
print(tup[0])
print(tup[0][1])

>>>
(('abc', '123'), 'def')
('abc', '123')
123
>>>
```

```python
tup = (("abc", "123"), ("def"))
tup += ("yetanother", 298)
print(tup)
print(tup[2])

>>>
(('abc', '123'), 'def', 'yetanother', 298)
yetanother
>>>
```

```python

>>>

>>>
```

#### <h4 id='7'>Loops: For Loops and While Loops</h4>
