

---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [DS](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DataStruct/DS.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Data Structures - String Methods</h3>

[strings](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DataStruct/Str/Str.MD)

---

<a href='#str_capitalize'>capitalize</a><br>
<a href='#str_casefold'>casefold</a><br>
<a href='#str_center'>center</a><br>
<a href='#str_count'>count</a><br>
<a href='#str_encode'>encode</a><br>
<a href='#str_endswith'>endswith</a><br>
<a href='#str_expandtabs'>expandtabs</a><br>
<a href='#str_find'>find</a><br>
<a href='#str_format'>format</a><br>
<a href='#str_format_map'>format_map</a><br>
<a href='#str_index'>index</a><br>
<a href='#str_isalnum'>isalnum</a><br>
<a href='#str_isalpha'>isalpha</a><br>
<a href='#str_isdecimal'>isdecimal</a><br>
<a href='#str_isdigit'>isdigit</a><br>
<a href='#str_isidentifier'>isidentifier</a><br>
<a href='#str_islower'>islower</a><br>
<a href='#str_isnumeric'>isnumeric</a><br>
<a href='#str_isprintable'>isprintable</a><br>
<a href='#str_isspace'>isspace</a><br>
<a href='#str_istitle'>istitle</a><br>
<a href='#str_isupper'>isupper</a><br>
<a href='#str_join'>join</a><br>
<a href='#str_ljust'>ljust</a><br>
<a href='#str_lower'>lower</a><br>
<a href='#str_lstrip'>lstrip</a><br>
<a href='#str_maketrans'>maketrans</a><br>
<a href='#str_partition'>partition</a><br>
<a href='#str_replace'>replace</a><br>
<a href='#str_rfind'>rfind</a><br>
<a href='#str_rindex'>rindex</a><br>
<a href='#str_rpartition'>rpartition</a><br>
<a href='#str_rsplit'>rsplit</a><br>
<a href='#str_rstrip'>rstrip</a><br>
<a href='#str_split'>split</a><br>
<a href='#str_splitlines'>splitlines</a><br>
<a href='#str_startswith'>startswith</a><br>
<a href='#str_swapcase'>swapcase</a><br>
<a href='#str_title'>title</a><br>
<a href='#str_translate'>translate</a><br>
<a href='#str_upper'>upper</a><br>
<a href='#str_zfill'>zfill</a><br>

<a href='#^'>^^^</a>

---

<h4 id='str_capitalize'>capitalize</h4>

```python
txt1='hello, and welcome to my world.'
txt2='bye'
txt3='iGLO'

x1=txt1.capitalize()
x2=txt2.capitalize()
x3=txt3.capitalize()

print(x1)
print(x2)
print(x3)

>>>
Hello, and welcome to my world.
Bye
Iglo
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='str_casefold'>casefold</h4>

```python
txt1='Hello, And Welcome To My World!'
txt2='BYE'
txt3='Bye'

x1=txt1.casefold()
x2=txt2.casefold()
x3=txt3.casefold()

print(x1)
print(x2)
print(x3)

>>>
hello, and welcome to my world!
bye
bye
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='str_center'>center</h4>

```python
txt = "banana"

x1 = txt.center(10)
x2 = txt.center(20)
x3 = txt.center(30)
x4 = txt.center(10, 'x')
x5 = txt.center(20, 'x')
x6 = txt.center(30, 'x')

print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)

>>>
  banana  
       banana       
            banana            
xxbananaxx
xxxxxxxbananaxxxxxxx
xxxxxxxxxxxxbananaxxxxxxxxxxxx
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='str_count'>count</h4>

```python
s = 'blablaabcdefgblabla'
s1 = 'b'
s2 = 'f'

print(s.count(s1, 5, 10))
print(s.count(s1, 6, 100))
print(s.count(s2, 0, 100))

>>>
1
3
1
>>>
```

```python
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

>>>
2
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='str_encode'>encode</h4>

```python
string01 = 'pythön!'
print('The string is:', string01)

string02 = string01.encode()
print('The encoded version is:', string02)

string03 = "My name is Ståle"
str03 = string03.encode()
print(str03)

>>>
The string is: pythön!
The encoded version is: b'pyth\xc3\xb6n!'
b'My name is St\xc3\xa5le'
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='str_endswith'>endswith</h4>

```python
txt = "Hello, welcome to my world."

x = txt.endswith(".")
y = txt.endswith("a")

print(x)
print(y)

>>>

>>>
```

<a href='#^'>^^^</a>

---

<h4 id='str_expandtabs'>expandtabs</h4>

```python
txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

>>>
H	e	l	l	o
H       e       l       l       o
H e l l o
H   e   l   l   o
H         e         l         l         o
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='str_find'>find</h4>

```python
txt = "Hello, welcome to my world."

s1 = txt.find("Hello")
s2 = txt.find("welcome")
s3 = txt.find("to")
s4 = txt.find("my")
s5 = txt.find("world")

x1 = txt.find("e", 1, 10)
x2 = txt.find("e", 2, 10)

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(x1)
print(x2)
>>>
0
7
15
18
21
1
8
>>>
```

<a href='#^'>^^^</a>

---

format

<a href='#^'>^^^</a>

---

format_map

<a href='#^'>^^^</a>

---

index

<a href='#^'>^^^</a>

---

isalnum

<a href='#^'>^^^</a>

---

isalpha

<a href='#^'>^^^</a>

---

isdecimal

<a href='#^'>^^^</a>

---

isdigit

<a href='#^'>^^^</a>

---

isidentifier

<a href='#^'>^^^</a>

---

islower

<a href='#^'>^^^</a>

---

isnumeric

<a href='#^'>^^^</a>

---

isprintable

<a href='#^'>^^^</a>

---

isspace

<a href='#^'>^^^</a>

---

istitle

<a href='#^'>^^^</a>

---

isupper

<a href='#^'>^^^</a>

---

join

<a href='#^'>^^^</a>

---

ljust

<a href='#^'>^^^</a>

---

lower

<a href='#^'>^^^</a>

---

lstrip

<a href='#^'>^^^</a>

---


maketrans

<a href='#^'>^^^</a>

---

partition

<a href='#^'>^^^</a>

---

replace

<a href='#^'>^^^</a>

---

rfind

<a href='#^'>^^^</a>

---

rindex

<a href='#^'>^^^</a>

---

rpartition

<a href='#^'>^^^</a>

---

rsplit

<a href='#^'>^^^</a>

---

rstrip

---

<h4 id='str_split'>split</h4>

remove duplicate words

```python
def remove_duplicate_words(s):
    
    print(s)
    #bye hello bye szia
    
    x = s.split()
    print(x)    
    #['bye', 'hello', 'bye', 'szia']
    
    #remove duplicates with append
    uniqueWords = []
    l1=[uniqueWords.append(i) for i in x if not i in uniqueWords]
    print(uniqueWords)
    #['bye', 'hello', 'szia']
    
    str1 = ' '.join(uniqueWords)

    return str1
    
print(remove_duplicate_words('bye hello bye szia'))
    
>>>
bye hello bye szia
['bye', 'hello', 'bye', 'szia']
['bye', 'hello', 'szia']
bye hello szia
>>>
```

<a href='#^'>^^^</a>

---

splitlines

<a href='#^'>^^^</a>

---

startswith

<a href='#^'>^^^</a>

---

swapcase

<a href='#^'>^^^</a>

---

title

<a href='#^'>^^^</a>

---

translate

<a href='#^'>^^^</a>

---

upper

<a href='#^'>^^^</a>

---

zfill

<a href='#^'>^^^</a>

---
