

---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [CF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/ControlFlow/CF.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Control Flow - Functions</h3>
<h3 id='^^def'></h3>

---

* <a href='#temp_0'>temp_0</a>
* <a href='#temp_01'>temp_01</a>
* <a href='#temp_02'>temp_02</a>
* <a href='#temp_03'>temp_03</a>
* <a href='#temp_04'>temp_04</a>
* <a href='#temp_05'>temp_05</a>
* <a href='#say_hello'>say_hello</a>
* <a href='#sum_strings'>sum_strings</a>
* <a href='#bigger'>bigger</a>
* <a href='#trueorfalse'>true or false</a>
* <a href='#dog_check'>dog_check</a>
* <a href='#cat_check'>cat_check</a>
* <a href='#pig_latin'>pig_latin</a>
* <a href='#lesser_of_two_evens'>lesser_of_two_evens</a>
* <a href='#args'>args</a>
* <a href='#kwargs'>kwargs</a>
* <a href='#animal_crackers'>animal_crackers</a>
* <a href='#makes_twenty'>makes_twenty</a>
* <a href='#defevenodd'>even and odd numbers</a>
* <a href='#old_macdonald'>old_macdonald</a>
* <a href='#uppersec'>upper() every 2nd char</a>
* <a href='#master_yoda'>master_yoda</a>
* <a href='#almost_there'>almost_there</a>
* <a href='#has_33'>has_33</a>
* <a href='#paper_doll'>paper_doll</a>
* <a href='#blackjack'>blackjack</a>
* <a href='#summer_69'>summer_69</a>
* <a href='#count_primes'>count_primes</a>
* <a href='#fibon'>fibon</a>
* <a href='#map'>map</a><br>
* <a href='#filter'>filter</a><br>
* <a href='#funnesstat'>nested statement</a><br>

<a href='#^'>^^^</a>

---

<h4 id='temp_0'>temp_0</h4>

```py
def elso():
    print('elso')

def masodik():
    return 'masodik'

elso()
print(masodik())

>>>
elso
masodik
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='temp_01'>temp_01</h4>

```python
######################
#variables
######################

vn11 = 10
vn12 = 9
vn13 = 5
vn14 = 8

vn31 = 27
vn32 = 71

######################
#Level 1
######################

def l11(a,b):
    x11 = a+b
    return x11

def l12(a,b):
    x12 = a*b
    return x12

######################
#Level 2
######################

def l21():
    y21 = l11(vn11, vn12)+l12(vn13, vn14)
    return y21

def l22():
    y22 = l11(vn11, vn12) - l12(vn13, vn14)
    return y22

######################
#Level 3
######################

def l31():
    z31 = l21() + vn31
    return z31

def l32():
    z32 = l21() + vn32
    return z32

def l33():
    z33 = l22() - 10
    return z33

######################
#prime, again, exit
######################

def prime():
    while True:
        p1 = int(input('n1-n2-n3-n4 or n5 exit \n'))
        if p1 == 1:
            print(l31())
        elif p1 == 2:
            print(l32())
        elif p1 == 3:
            print(l33())
        elif p1 == 4:
            print(l31(), l32(), l33())
        elif p1 == 5:
            return exit()

def again():
    return prime()

def exit():
    print('bye')

######################
#run
######################

prime()
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='temp_02'>temp_02</h4>

```python
#your variables
x = 2
y = 3
m = 'yellow'
n = ' '
p = 'uuuuuugh'

#first todo function
def first(aa, bb):
    a = aa+bb
    return a

#second todo function
def sec(nn, mm):
    k = 'hello'
    return k+n+mm

#third todo function
def third(fff, ooo):
    l = 'fffUUU'
    return l+fff+ooo

#main function
def prime():
    a = int(input('num?'))
    if a == 1:
        print(first(x,y))
    elif a == 2:
        print(sec(n,m))
    elif a == 3:
        print(third(n, p))
    else:
        print('give me a num')

prime()

>>>
num?1
5

num?2
hello yellow

num?3
fffUUU uuuuuugh
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='temp_03'>temp_03</h4>

```python
a = 10
b = 20
d = 3
e = 6

def elso():
    c = a+b
    return c

def masodik():
    f = d+e
    return f

ee = elso()
mm = masodik()

def harmadik():
    x = ee+mm
    return x

def negyedik(x,y):
    final = x+y
    print(final)

print(harmadik())
negyedik(ee, mm)

>>>
39
39
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='temp_04'>temp_04</h4>

```python
hometown = 'ds'
age = '35'
user_name = 'trk'

x = 10
y = 20
z = 42

def year(ccc, aaa):
    print("Hello, ", ccc, ". You are", aaa, "old")

def place(ccc, bbb):
    print('hey', ccc, 'you are from', bbb, 'right?')

def greet(ccc):
    print("Hello, ", ccc, ". Good morning!")

def kkk():
    yu = 66+18
    return yu

kyu = kkk()

def ct():
    ppp = z+y+z+kyu
    return ppp

def sowhat():
    xxx = ct() + z
    print(xxx)

year(user_name, age)
place(user_name, hometown)
greet(user_name)
print(ct())
sowhat()
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='temp_05'>temp_05</h4>

```python
#variables
a = "hello world"
b = "xyz"
c = 5
d = 7

#functions
def pr(par1):
  print(par1)
  
def ps(par1, par2):
  return (par1+par2)

def ms(par1,par2):
  return (par1-par2)

#STDOUT
pr(a)
pr(b)
print(ps(c,d))
print(ms(c,d))

>>>
hello world
xyz
12
-2
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='say_hello'>say_hello</h4>

```python
def say_hello(name='NAME'):
    print('hello', name)

say_hello()
say_hello('trk')

>>>
hello NAME
hello trk
>>>
```

```python
def say_hello(name='trk'):
  print("the say_hello() function has been executed")
  
  def greet():
    return "\t This is inside the greet() function"
  
  def welcome():
    return "\t This is inside the welcome() function"
    
  print(greet())
  print(welcome())
  print("now we are back inside the hello() function")
    
print(say_hello())

>>>
the say_hello() function has been executed
	 This is inside the greet() function
	 This is inside the welcome() function
now we are back inside the hello() function
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='sum_strings'>sum_strings</h4>

```python
def sum_strings(num1, num2):
    return (num1 + num2)

x = add_num("one", "two")

print(x)

>>>
onetwo
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='bigger'>bigger</h4>

```python
#variables
a = 5
b = 10
bigger = 0

#function
def func(num1, num2):
  if num1 > num2:
    bigger = num1
  else:
    bigger = num2
  return bigger

#print
print(func(a, b))

>>>
10
>>>
```

```python
#variables
a = 5
b = 10
bigger = 0

#function
def func(num1, num2):
  if num1 > num2:
    bigger = num1
  else:
    bigger = num2
  return bigger

#print
print(func(a, 4))
print(func(a, b))

>>>
5
10
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='trueorfalse'>true or false</h4>

```python
a = 20
b = 4
c = True
d = False

def no(p1,p2,p3):
  if (p3 == True):
    print(p3, p1+p2)
  else:
    print(p3, p1-p2)
  
no(a,b,c)
no(a,b,d)

>>>
(True, 24)
(False, 16)
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='dog_check'>dog_check</h4>

```python
def dog_check(s):
    if 'dog' in s:
        return True
    else:
        return False

print(dog_check('my dog ran away'))
print(dog_check('my Dog ran away'))
print(dog_check('my cat ran away'))

>>>
True
False
False
>>>
```

```python
def dog_check(s):
    if 'dog' in s.lower():
        return True
    else:
        return False

print(dog_check('my dog ran away'))
print(dog_check('my Dog ran away'))
print(dog_check('my cat ran away'))

>>>
True
True
False
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='cat_check'>cat_check</h4>

```python
def cat_check(s):
    return 'cat' in s.lower()

print(cat_check('my dog ran away'))
print(cat_check('my Cat ran away'))
print(cat_check('my cat ran away'))

>>>
False
True
True
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='pig_latin'>pig_latin</h4>

```python
def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

print(pig_latin('word'))
print(pig_latin('trk'))
print(pig_latin('Hello'))
print(pig_latin('apple'))

>>>
ordway
rktay
elloHay
appleay
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='args'>args</h4>

```python
def mf(*args):
    return sum(args)*2

print(mf(10, 20, 30))

>>>
120
>>>
```

```python
def mf(*args):
    print (args)

mf(10, 20, 30)

>>>
(10, 20, 30)
>>>
```

```python
def mf(*whatever):
    print (whatever)

mf(1, 2, 3, 4, 5)

>>>
(1, 2, 3, 4, 5)
>>>
```

```python
def mf(*args):
    for item in args:
        print(item)

mf(1, 2, 3, 4, 5)

>>>
1
2
3
4
5
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='defevenodd'>even and odd numbers</h4>

```python
def mf(*args):
    l_e = []
    l_o = []
    for nums in args:
        if nums%2 == 0:
            l_e.append(nums)
        elif nums%2 == 1:
            l_o.append(nums)
    print('odd numbers are:', l_o)
    print('even numbers are:', l_e)

mf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

>>>
odd numbers are: [1, 3, 5, 7, 9]
even numbers are: [2, 4, 6, 8, 10]
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='kwargs'>kwargs</h4>

```python
def mf(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my fruit of choice is {}' .format(kwargs['fruit']))
    else:
        print('i didnt find any fruit here')

mf(fruit='apple', veggie ='lettuce')

>>>
{'fruit': 'apple', 'veggie': 'lettuce'}
my fruit of choice is apple
>>>
```

```python
def mf(*args, **kwargs):
    print('I would like {} {}' .format(args[0], kwargs['food']))
    print(' ')
    print(args)
    print(kwargs)

mf(10, 20, 30, 40, 50, fruit='apple', food ='eggs')

>>>
I would like 10 eggs
 
(10, 20, 30, 40, 50)
{'fruit': 'apple', 'food': 'eggs'}>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lesser_of_two_evens'>lesser_of_two_evens</h4>

```python
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a < b:
            result = a
        else:
            result = b
    else:
        if a > b:
            result = a
        else:
            result = b
    return result

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(8,4))
print(lesser_of_two_evens(2,5))
print(lesser_of_two_evens(7,5))

>>>
2
4
5
7
>>>
```

```python
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        result = min(a,b)
    else:
        result = max(a,b)
    return result

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(8,4))
print(lesser_of_two_evens(2,5))
print(lesser_of_two_evens(7,5))

>>>
2
4
5
7
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='animal_crackers'>animal_crackers</h4>

```python
def animal_crackers(text):
    wordlist = text.split()
    print(wordlist)

    first = wordlist[0]
    second = wordlist[1]

    return first[0] == second[0]

print(animal_crackers('Levelhead Llama'))
print(animal_crackers('Crazy Kangaroo'))

>>>
['Levelhead', 'Llama']
True
['Crazy', 'Kangaroo']
False
>>>
```

```python
def animal_crackers(text):
    wordlist = text.split()

    return wordlist[0][0] == wordlist[1][0]

print(animal_crackers('Levelhead Llama'))
print(animal_crackers('Crazy Kangaroo'))

>>>
True
False
>>>
```

```python
def animal_crackers(text):
    wordlist1 = text.split()
    wordlist2 = text.lower().split()

    print(wordlist1[0][0] == wordlist1[1][0])
    print(wordlist2[0][0] == wordlist2[1][0])

animal_crackers('Crazy cat')

>>>
False
true
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='makes_twenty'>makes_twenty</h4>

```python
def makes_twenty(n1, n2):
    if n1+n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False

print(makes_twenty(10, 10))
print(makes_twenty(20, 10))
print(makes_twenty(10, 20))
print(makes_twenty(21, 19))

>>>
True
True
True
False
>>>
```

```python
def makes_twenty(n1, n2):
    return (n1+n2) == 20 or n1 == 20 or n2 == 20

print(makes_twenty(10, 10))
print(makes_twenty(20, 10))
print(makes_twenty(10, 20))
print(makes_twenty(21, 19))

>>>
True
True
True
False
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='old_macdonald'>old_macdonald</h4>

```python
def old_macdonald(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return first_letter.upper()+inbetween+fourth_letter.upper()+rest

print(old_macdonald('macdonald'))

>>>
MacDonald
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='uppersec'>upper() every 2nd char</h4>

```python
def test(text):
    s1 = text[0:100:2].upper()
    s2 = text[1:100:2].lower()
    l1 = list(s1)
    l2 = list(s2)
    baz = [x + y for x, y in zip(l1, l2)]
    s3 = ''.join(baz)
    return s3

print(test('abcdefgijklmnop'))

>>>
AbCdEfGiJkLmNo
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='master_yoda'>master_yoda</h4>

```python
def master_yoda(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    return ' '.join(reverse_word_list)

print(master_yoda('I am home'))

>>>
home am I
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='almost_there'>almost_there</h4>

```python
def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)

print(almost_there(104))
print(almost_there(89))
print(almost_there(189))
print(almost_there(204))
print(almost_there(211))

>>>
True
False
False
True
False
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='has_33'>has_33</h4>

```python
def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] ==3:
            return True

    return False

print(has_33([1,3,3]))
print(has_33([3,1,3]))
print(has_33([1,3,1,3]))
print(has_33([1,2,3,3]))

>>>
True
False
False
True
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='paper_doll'>paper_doll</h4>

```python
def paper_doll(text):
    result = ''
    for char in text:
        result += char*3
    return result


print(paper_doll('hello'))
print(paper_doll('trk'))

>>>
hhheeellllllooo
tttrrrkkk
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='blackjack'>blackjack</h4>

```python
def blackjack(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) <= 31:
        return sum([a, b, c])-10
    else:
        return 'BUST'

print(blackjack(8, 7, 9))
print(blackjack(5, 6, 7))
print(blackjack(9, 9, 11))

>>>
BUST
18
19
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='summer_69'>summer_69</h4>

```python
def summer_69(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num!=6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(summer_69([5, 6, 7, 8, 9, 10]))
print(summer_69([6, 7, 8, 9, 10]))

>>>
36
15
10
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='spy_game'>spy_game</h4>

```python
def spy_game(nums):

    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([1, 2, 3, 0, 4, 0, 7]))
print(spy_game([1, 2, 3, 0, 0, 7]))
print(spy_game([0, 7, 0]))

>>>
True
True
False
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='count_primes'>count_primes</h4>

```python
def count_primes(num):
    if num < 2:
        return 0
    primes = [2]
    x = 3

    while x <= num:
        for y in range(3,x,2):
            if x%2 == 0:
                x +=2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(20))

>>>
[2, 3, 5, 7, 9, 11, 13, 15, 17, 19]
10
>>>
```

```python
def is_prime(num):
    """
    IN: A number
    OUT: A print statement wheter or not the number is prime.
    """

    for n in range(2, num):
        if num % n == 0:
            print ("not prime")
            break
        else:
            print ("the number is prime!")
            
is_prime(12)

>>>
not prime
>>>
```

```python
def is_prime(num):
    """
    IN: A number
    OUT: A print statement wheter or not the number is prime.
    """

    for n in range(2, num):
        if num % n == 0:
            print ("not prime")
            break
        else:
            print ("the number is prime!")
            
is_prime(11)
    
>>>
the number is prime!
the number is prime!
the number is prime!
the number is prime!
the number is prime!
the number is prime!
the number is prime!
the number is prime!
the number is prime!
>>> 
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='fibon'>fibon</h4>

```python
def fibon(n):
  a = 1
  b = 1
  
  output = []
  
  for i in range(n):
    output.append(a)
    a,b = b, a+b 
    
  return output
  
print(fibon(10))

>>>
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>>
```

```python
def genfibon(n):
  a = 1
  b = 1
  
  for i in range(n):
    yield a
    t = a
    a = b
    b = t+b 

for num in genfibon(10):
  print(num)
  
>>>
1
1
2
3
5
8
13
21
34
55
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='map'>map</h4>

```python
def square(num):
    return num**2

nums = [1, 2, 3, 4, 5]

for item in map(square, nums):
    print(item)
    
>>>
1
4
9
16
25
>>>
```

```python
def square(num):
    return num**2

nums = [1, 2, 3, 4, 5]

print(list(map(square,nums)))

>>>
[1, 4, 9, 16, 25]
>>>
```

```python
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))

>>>
['EVEN', 'E', 'S']
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='filter'>filter</h4>

```python
def check_even(num):
    return num%2 == 0

mynums = [1, 2, 3, 4, 5, 6]

print(list(filter(check_even, mynums)))

>>>
[2, 4, 6]
>>>
```

```python
def check_even(num):
    return num%2 == 0

mynums = [1, 2, 3, 4, 5, 6]

for n in filter(check_even,mynums):
    print(n)
    
>>>
2
4
6
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='funnesstat'>Nested statement</h4>

```python
name = 'THIS IS A GLOBAL STRING'

def greet():

    name = 'Sammy'

    def hello():
        name = 'IM A LOCAL'
        print('Hello '+name)

    hello()

greet()

>>>
Hello IM A LOCAL
>>>
```

```python
name = 'THIS IS A GLOBAL STRING'

def greet():

    name = 'Sammy'

    def hello():
        #name = 'IM A LOCAL'
        print('Hello '+name)

    hello()

greet()

>>>
Hello Sammy
>>>
```

```python
name = 'THIS IS A GLOBAL STRING'

def greet():

    #name = 'Sammy'

    def hello():
        #name = 'IM A LOCAL'
        print('Hello '+name)

    hello()

greet()

>>>
Hello THIS IS A GLOBAL STRING
>>>
```

```python
x = 50

def func(x):
    print(f'X is {x}')

    x = 200
    print(f'I just LOCALLY changed x to {x}')

func(x)
print(f'outside print x is: {x}')

>>>
X is 50
I just LOCALLY changed x to 200
outside print x is: 50
>>>
```

```python
x = 50

def func():
    global x
    print(f'X is {x}')

    x = 'NEW VALUE'
    print(f'I just LOCALLY changed x to {x}')

func()
print(f'outside print x is: {x}')

>>>
X is 50
I just LOCALLY changed x to NEW VALUE
outside print x is: NEW VALUE
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---
