
[30 Days of Python](https://www.udemy.com/30-days-of-python/learn/v4/content)
======

### Section 1 - Welcome
  * <a href='#1'>1 - Welcome</a>
  * <a href='#2'>2 - Getting help</a>
  * <a href='#3'>3 - Youtube and Suggestions</a>

### Section 2 - Days 1: Basics
  * <a href='#4'>4 - Setup, String, Variables and Integers</a>

### Section 3 - Day 2 & 3 - Lists, Dictionaries, Tuples and Loops
  * <a href='#5'>5 - Lists</a>
  * <a href='#6'>6 - Dictionaries and Tuples</a>
  * <a href='#7'>7 - Loops: For Loops and While Loops</a>

### Section 4 - Day 4: Conditionals
  * <a href='#8'>8 - Conditionals</a>
  * <a href='#9'>9 - Using Conditionals Expressions</a>

### Section 5 - Day 5: Functions
  * <a href='#10'>10 - Functions P1</a>
  * <a href='#11'>11 - Functions P2</a>

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

### <h3 id='1'>1 - Welcome</h3>

[[Welcome.udemy](https://www.udemy.com/30-days-of-python/learn/v4/t/lecture/5800476?start=0)]

### <h3 id='2'>2 - Getting help</h3>

[[Getting help.udemy](https://www.udemy.com/30-days-of-python/learn/v4/t/lecture/5800738?start=0)]

### <h3 id='3'>3 - Youtube and Suggestions</h3>

[[Youtube and Suggestions.udemy](https://www.udemy.com/30-days-of-python/learn/v4/t/lecture/5800742?start=0)]

Days 1: Basics
------

### <h3 id='4'>4 - Setup, String, Variables and Integers</h3>

[[Setup, String, Variables and Integers.udemy](https://www.udemy.com/30-days-of-python/learn/v4/t/lecture/5800734?start=0)]

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

### <h3 id='5'>5 - Lists</h3>

[[Lists.udemy](https://www.udemy.com/30-days-of-python/learn/v4/t/lecture/5872358?start=0)]

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

### <h3 id='6'>6 - Dictionaries and Tuples</h3>

[[Dictionaries and Tuples.udemy](https://www.udemy.com/30-days-of-python/learn/v4/t/lecture/5872366?start=0)]

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

### <h3 id='7'>7 - Loops: For Loops and While Loops</h3>

[[Loops: For Loops and While Loops.udemy](https://www.udemy.com/30-days-of-python/learn/v4/t/lecture/5872370?start=0)]

FOR LOOP

```python
bag = [112, 3472, 34538, 10, 3827]

for items in bag:
  print(items)
  
>>>
112
3472
34538
10
3827
>>>
```

```python
bag = [1, 2, 3, 4, 5, 6, 7]

i = 0
for item in bag:
  i = i + 1
  print(i)
  
>>>
1
2
3
4
5
6
7
>>>
```

```python
bag = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in bag:
  if item == 10:
    print('yeahhhh')
    
>>>
yeahhhh
>>>
```

WHILE LOOP

```python
i = 10
while i < 11:
  print("yup")
  i = i + 1
  
>>>
yup
>>>
```

```python
i = 0
while i < 11:
  print(i)
  i = i + 1

>>>
0
1
2
3
4
5
6
7
8
9
10
>>>
```

### <h3 id='8'>8 - Conditionals</h3>

[[Conditionals.udemy](https://www.udemy.com/30-days-of-python/learn/v4/t/lecture/5872374?start=0)]

```python
True

>>>
True
>>>
```

```python
False

>>>
False
>>>
```

```python
obj_a = True
print(obj_a == "d")

>>>
False
>>>
```

```python
list_a = [1,2,3]
list_b = [1,2,3]
list_c = [4,5,6]

print(list_a == list_b)
print(list_b == list_c)
print(list_c != list_a)

>>>
True
False
True
>>>
```

```python

>>>

>>>
```

```python

>>>
True
False
True
>>>
```

### <h3 id='9'>9 - Using Conditionals Expressions</h3>

[[Using Conditionals Expressions.udemy](https://www.udemy.com/30-days-of-python/learn/v4/t/lecture/5872376?start=0)]

```python
list_a = [1,2,3,4]

for nums in list_a:
    print(nums)
    
>>>
1
2
3
4
>>>
```

```python
list_a = [1,2,3,4]

for nums in list_a:
    print(nums**2)
    
>>>
1
4
9
16
>>>
```

isinstance()

```python
list_d = ["jean", 12, "joerg", 34]
list_e = []

for i in list_d:
    if isinstance(i, int):
        list_e.append(i)
    
print(list_e)

>>>
[12, 34]
>>>
```

```python
list_d = ["jean", 12, "joerg", 34]
list_e = []

x = 0

print(list_d[x])
print(list_d[x+1])

>>>
jean
12
>>>
```

```python
list_d = ["jean", 12, "joerg", 34]
list_e = []

for i in list_d:
    if isinstance(i, int):
        list_e.append(i)
        list_d.pop(x)
    x += 1
    
print(list_e)
print(list_d)

>>>
[12, 34]
['jean', 'joerg']
>>>
```

### <h3 id='10'>10 - Functions P1</h3>

[[Functions P1.udemy](https://www.udemy.com/30-days-of-python/learn/v4/t/lecture/5872380?start=0)]

```sort()```

```python
str_items = ["phd", "abc", "nba", "BBB", "ABB", "AAA"]
str_items.sort()

print(str_items)

>>>
['AAA', 'ABB', 'BBB', 'abc', 'nba', 'phd']
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

```python

>>>

>>>
```
