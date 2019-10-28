
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [CF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/ControlFlow/CF.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Control Flow - while</h3>

---

<h4 id=''>while Template</h4>

```python
while some_boolean_condition:
    #do something
```

<a href='#^'>^^^</a>

```python
while some_boolean_condition:
    #do something
else:
    #do something different
```

<a href='#^'>^^^</a>

---

count the average of the lists

```python
import math

def sum_average(arr):

    x=0
    l=[]
    while x < len(arr):
        res=sum(arr[x])/len(arr[x])
        l.append(res)
        x += 1
    return math.floor(sum(l))
        
    
print(sum_average([[-4, 3, -8, -2], [2, 9, 1, -5], [-7, -2, -6, -4]]))

>>>
-6
>>>
```

<a href='#^'>^^^</a>

---

from dict find the numbers or sum as per the string/list

```python
import string as st

def words_to_marks(s):   
    
    abc=st.ascii_lowercase
    
    #join two lists into the dict
    labc=list(abc)    
    lnum=list(range(1,len(abc)+1))
    dic = dict(zip(labc,lnum))
    
    l=list(s)
    
    #from dict find the numbers or sum as per the string/list
    x=0
    l1=[]
    while x < len(l):
        l1.append(dic[l[x]])
        x += 1
    return sum(l1)

print(words_to_marks('attitude'))

>>>
100
>>>
```

<a href='#^'>^^^</a>

---

String reverse

```python
def reverse_slice(s):
    
    l=[]
    ss=s[::-1]
    l.append(ss)
    print(l)
    
    l.append(ss[1:])
    print(l)
    
    l.append(ss[2:])
    print(l)
    
    l.append(ss[3:])
    print(l)
    
    l.append(ss[4:])
    print(l)
    
    print(len(s))
    
print(reverse_slice('abcde'))

>>>
['edcba']
['edcba', 'dcba']
['edcba', 'dcba', 'cba']
['edcba', 'dcba', 'cba', 'ba']
['edcba', 'dcba', 'cba', 'ba', 'a']
5
>>>

def reverse_slice(s):
    
    x=1
    l=[]
    ss=s[::-1]
    l.append(ss)
    while x < len(s):
        l.append(ss[x:])
        x += 1
    return l

print(reverse_slice('abcde'))

>>>
['edcba', 'dcba', 'cba', 'ba', 'a']
>>>
```

<a href='#^'>^^^</a>

---

count the sheep

```python
def count_sheep(n):    
  
    x = 0
    while x < n:
        l=[]
        ll=[l.append(str(nums)+' sheep...') for nums in range(1,n+1)]
        x += 1
    str1=''.join(l)    
    return str1
   
print(count_sheep(5))    

>>>
1 sheep...2 sheep...3 sheep...4 sheep...5 sheep...
>>>
```

---

find the nex correct year

```python
def next_happy_year(year):

    x = year+1
    while x < year+5000:
        s = str(x)
        l = list(s)
        ll = [int(i) for i in l]
        checkYear = len(ll)
        template = [1] * checkYear
        listOutOrigin = []
        for element in ll:
            aa = ll.count(element)
            listOutOrigin.append(aa)
        if template == listOutOrigin:
            break
        x += 1

    l = [str(i) for i in ll]
    str1 = ''.join(l)
    final = int(str1)
    return final

print(next_happy_year(1987))

>>>
2013
>>>
```

---

<h4 id=''>Infinity loop</h4>

```python
x = 0

while x < 10:
    print(f'the current status of x is {x}')
    
>>>
...
>>>
```

<a href='#^'>^^^</a>

---

<h4 id=''>Basic while loop</h4>

```python
x = 0
while x < 5:
    print(f'the current status of x is {x}')
    #x = x + 1
    x += 1
    
>>>
the current status of x is 0
the current status of x is 1
the current status of x is 2
the current status of x is 3
the current status of x is 4
>>>
```

<a href='#^'>^^^</a>

```python
x = 1
while x < 5:
    print(f'the current status of x is {x}')
    #x = x + 1
    x += 1
    
>>>
the current status of x is 1
the current status of x is 2
the current status of x is 3
the current status of x is 4
>>>
```

<a href='#^'>^^^</a>

```python
x = 3
while x < 5:
    print(f'the current status of x is {x}')
    #x = x + 1
    x += 1   
    
>>>
the current status of x is 3
the current status of x is 4
>>>
```

<a href='#^'>^^^</a>

---

<h4 id=''>while with else</h4>

```python
x = 1
while x < 5:
    print(f'the current status of x is {x}')
    #x = x + 1
    x += 1
else:
    print('x is less than 5')
    
>>>
the current status of x is 1
the current status of x is 2
the current status of x is 3
the current status of x is 4
x is less than 5
>>>
```

<a href='#^'>^^^</a>

---

<h4 id=''>break while</h4>

```python
x = 0

while x < 5:
    if x == 2:
        break
    print(f'x is now {x}')
    x += 1
    
>>>
x is now 0
x is now 1
>>>
```

<a href='#^'>^^^</a>

---

```python

>>>

>>>
```

<a href='#^'>^^^</a>

---

```python

>>>

>>>
```

<a href='#^'>^^^</a>

---

```python
a = "hi world"

i = 1
while i < 6:
  print(a)
  i += 1
  
>>>
hi world
hi world
hi world
hi world
hi world
>>>
```

<a href='#^'>^^^</a>

```python
i = 1
while i < 6:
  print(i)
  i += 1
  
>>>
1
2
3
4
5
>>>
```

<a href='#^'>^^^</a>

```
x = 0

while x < 10:
    print ("X is currently: ", x)
    x +=1
	
>>>
X is currently:  0
X is currently:  1
X is currently:  2
X is currently:  3
X is currently:  4
X is currently:  5
X is currently:  6
X is currently:  7
X is currently:  8
X is currently:  9
>>> 
```

<a href='#^'>^^^</a>

```python
x = 0

while x < 10:
    print ("X is currently: ", x)
    x +=1
else:
    print ("All done!")
	
>>>
X is currently:  0
X is currently:  1
X is currently:  2
X is currently:  3
X is currently:  4
X is currently:  5
X is currently:  6
X is currently:  7
X is currently:  8
X is currently:  9
All done!
>>> 
```

<a href='#^'>^^^</a>

```python
while test:
	code statement
	if test:
		break
	if test:
		continue
else:
	final code statements
x = 0

while x < 10:
    print ("X is currently: ", x)
    print ("X is still less than 10, adding 1 to x")
    x +=1

    if x==3:
        print ("Hey x equals 3!")
    else:
        print ("continuing")
        continue
		
>>>
X is currently:  0
X is still less than 10, adding 1 to x
continuing
X is currently:  1
X is still less than 10, adding 1 to x
continuing
X is currently:  2
X is still less than 10, adding 1 to x
Hey x equals 3!
X is currently:  3
X is still less than 10, adding 1 to x
continuing
X is currently:  4
X is still less than 10, adding 1 to x
continuing
X is currently:  5
X is still less than 10, adding 1 to x
continuing
X is currently:  6
X is still less than 10, adding 1 to x
continuing
X is currently:  7
X is still less than 10, adding 1 to x
continuing
X is currently:  8
X is still less than 10, adding 1 to x
continuing
X is currently:  9
X is still less than 10, adding 1 to x
continuing
>>> 
```

<a href='#^'>^^^</a>

```python
x = 0

while x < 10:
    print ("X is currently: ", x)
    print ("X is still less than 10, adding 1 to x")
    x +=1

    if x==3:
        print ("Hey x equals 3!")
        break
    else:
        print ("continuing")
        continue
		
>>>
X is currently:  0
X is still less than 10, adding 1 to x
continuing
X is currently:  1
X is still less than 10, adding 1 to x
continuing
X is currently:  2
X is still less than 10, adding 1 to x
Hey x equals 3!
>>>
```

<a href='#^'>^^^</a>

---

```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
>>>
1
2
3
>>>
```

<a href='#^'>^^^</a>

---

```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    print("itt volt a harmadik step")
  if i == 5:
    print("itt meg az otodik")
  i += 1
  
>>>
1
2
3
itt volt a harmadik step
4
5
itt meg az otodik
>>>
```

<a href='#^'>^^^</a>

---

