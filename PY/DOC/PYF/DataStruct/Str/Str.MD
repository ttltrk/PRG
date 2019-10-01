
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [DS](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DataStruct/DS.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Data Structures - Strings</h3>

---

* <a href='#strbasics'>string basics</a><br>
* <a href='#strlistsep'>string to list separately</a><br>
* <a href='#strlistfull'>string to list full</a><br>
* <a href='#strset'>string to set</a><br>
* <a href='#strtup'>string to tuple</a><br>
* <a href='#pwdgen'>password check</a><br>
* <a href='#palcheck'>palindrome check</a><br>
* <a href='#changeordswap'>change the order and use swapcase</a><br>

---

<h4 id='strbasics'>string basics</h4>

```python
| P | y | t | h | o | n |
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

<a href='#^'>^^^</a>

---

```python
import string as st
def high():
    
    abc=st.ascii_lowercase
    print(abc)
    print(abc[-1])
    print(abc[::-1])

print(high())

>>>
abcdefghijklmnopqrstuvwxyz
z
zyxwvutsrqponmlkjihgfedcba
>>>
```

---

<h4 id='strlistsep'>string to list separately</h4>

```python
def split(word):
    l = [char for char in word]
    return l

print(split('heyho'))

>>>
['h', 'e', 'y', 'h', 'o']
>>>
```

```python
word = 'abc'
l = list(word)
print(l)

>>>
['a', 'b', 'c']
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='strlistful'>string to list full</h4>

```python
a = 'mary'
z = a.split()
print(z)

>>>
['mary']
>>>
```

```python
def high(x):    
    inpL = x.split()
    return inpL

high('man i need a taxi up to ubud')

>>>
['man', 'i', 'need', 'a', 'taxi', 'up', 'to', 'ubud']
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='strset'>string to set</h4>

```python
s = "blabla"
f = {s}

print(type(f))
print(f)

>>>
{'blabla'}
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='strtup'>String to tuple</h4>

```python
string="heyho"
a = tuple(string)

print(a)

>>>
('h', 'e', 'y', 'h', 'o')
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='pwdgen'>password check</h4>

```python
def password(string):

    #check if the string contains uppercase char
    r1 = [any(x.isupper() for x in string)]
    print(r1)

    #check if the string contains uppercase char
    r2 = [any(x.islower() for x in string)]
    print(r2)

    #check if the string contains uppercase char
    r3 = [any(x.isdigit() for x in string)]
    print(r3)

    r4 = len(string)
    print(r4)

    if r1 == [False] or r2 == [False] or r3 == [False] or r4 < 8:
        return False
    else:
        return True

print(password("abcd1234"))

>>>
[False]
[True]
[True]
8
False
>>>

```

<a href='#^'>^^^</a>

---

<h4 id='palcheck'>palindrome check</h4>

```python
def is_palindrome(s):

    st = s.lower()
    rev = st[::-1]

    if st == rev:
        return True
    else:
        return False

print(is_palindrome('Abba'))

>>>
True
>>>

```

<a href='#^'>^^^</a>

---

<h4 id='changeordswap'>change the order and use swapcase</h4>

```python
def string_transformer(s):

    #reverse the order of the words in the string
    reversed_string = " ".join(s.split(" ")[::-1])

    #use swapcase for change all the upper to lower and back
    sc = reversed_string.swapcase()
    return sc

print(string_transformer("Example string"))

>>>
STRING eXAMPLE
>>>
```

<a href='#^'>^^^</a>

---

```python
a = "Hello, World!"

print(a[1])
print(a[2:5])

>>>
e
llo
>>>
```

<a href='#^'>^^^</a>

---

```python
ms1 = 'Hello'
print(ms1)

ms2 = "Hello"
print(ms2)

ms3 = '''Hello'''
print(ms3)

ms4 = """Hello, welcome to
           the world of Python"""
print(ms4)

>>>
Hello
Hello
Hello
Hello, welcome to
           the world of Python
>>>
```

<a href='#^'>^^^</a>

---

```python
str = 'programiz'
print('str = ', str)

print('str[0] = ', str[0])

print('str[-1] = ', str[-1])

print('str[1:5] = ', str[1:5])

print('str[5:-2] = ', str[5:-2])

>>>
str =  programiz
str[0] =  p
str[-1] =  z
str[1:5] =  rogr
str[5:-2] =  am
>>>
```

<a href='#^'>^^^</a>

---

```python
ss = "Sammy Shark!"

print(ss[0])
print(ss[1])
print(ss[2])
print(ss[3])
print(ss[4])
print(ss[5])
print(ss[6])
print(ss[7])
print(ss[8])
print(ss[9])
print(ss[10])
print(ss[11])
print(ss[12])

>>>
S
a
m
m
y
 
S
h
a
r
k
!
>>>
```

<a href='#^'>^^^</a>

---

```python
ss = "Sammy Shark!"

print(ss[-1])
print(ss[-2])
print(ss[-3])
print(ss[-4])
print(ss[-5])
print(ss[-6])
print(ss[-7])
print(ss[-8])
print(ss[-9])
print(ss[-10])
print(ss[-11])
print(ss[-12])

>>>
!
k
r
a
h
S
 
y
m
m
a
S
>>>
```

<a href='#^'>^^^</a>

---

```python
ss = "Sammy Shark!"

print(ss[:5])
print(ss[6:11])
print(ss[7:])

>>>
Sammy
Shark
hark!
>>>
```

<a href='#^'>^^^</a>

---

```python
ss = "Sammy Shark!"

print(ss[0:12:1])
print(ss[0:12:2])
print(ss[0:12:3])
print(ss[::1])
print(ss[::2])
print(ss[::3])

>>>
Sammy Shark!
SmySak
SmSr
Sammy Shark!
SmySak
SmSr
>>>
```

<a href='#^'>^^^</a>

---

```python
ss = "Sammy Shark!"

print(ss[::-1])
print(ss[::-2])
print(ss[::-3])

>>>
!krahS ymmaS
!rh ma
!a m
>>>
```

<a href='#^'>^^^</a>

---

```python
str1 = 'Hello'
str2 ='World!'

print('str1 + str2 = ', str1 + str2)

print('str1 * 3 =', str1 * 3)

>>>
str1 + str2 =  HelloWorld!
str1 * 3 = HelloHelloHello
>>>
```

<a href='#^'>^^^</a>

---

```python
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')

>>>
3 letters found
>>>
```

<a href='#^'>^^^</a>

---

```python
str = 'cold'

list_enumerate = list(enumerate(str))

print('list(enumerate(str) = ', list_enumerate)
print('len(str) = ', len(str))

>>>
list(enumerate(str) =  [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]
len(str) =  4
>>>
```

<a href='#^'>^^^</a>

---

```python
print('''He said, "What's there?"''')
print('He said, "What\'s there?"')
print("He said, \"What's there?\"")

>>>
He said, "What's there?"
He said, "What's there?"
He said, "What's there?"
>>>
```

<a href='#^'>^^^</a>

---
