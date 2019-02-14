
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - OOP</h3>

---

```python
class test1:

    var_1 = 25

    def elso(self):
        var_2 = 5
        return test1.var_1 + var_2

    def masodik(self):
        return 3

class test2:

    def harmadik(self):
        return 5

    def negyedik(self):
        print('hi all')

t1 = test1()
t2 = test2()

def control():
    return ((t2.harmadik() + t1.masodik()) + (t1.var_1 - t1.elso()))

print(control()) #3
t2.negyedik() #hi all
test2.negyedik(t2) #hi all

>>>
3
hi all
hi all
>>>
```

---

```python
class test1:

    def __init__(self):
        print('in init')

    def elso(self):
        return 3

    def masodik(self):
        print('hi all')

t1 = test1()

print(t1.elso())
t1.masodik()

>>>
in init
3
hi all
>>>
```

---

```python
class test1:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def elso(self):
        print('az elso ertekek: ', self.a, self.b)

    def masodik(self):
        print('a masodik ertekek: ', self.c, self.d)

t1 = test1('10', '20', '30', '40')

t1.elso()
t1.masodik()

>>>
az elso ertekek:  10 20
a masodik ertekek:  30 40
>>>
```

---

```python
class test1:
    pass

t1 = test1()
t2 = test1()

print(id(t1))
print(id(t2))

>>>
60030960
60029200
>>>
```

---

```python
class test1:

    def __init__(self):
        self.name = 'trk'
        self.age = 36

t1 = test1()
t2 = test1()

t1.name = 'ttl'
t1.age = 35

print(t1.name)
print(t2.name)

>>>
ttl
trk
>>>
```

---

```python
class test1:

    def __init__(self):
        self.name = 'trk'
        self.age = 36

    def update(self):
        self.age = 99

t1 = test1()
t2 = test1()

t1.name = 'ttl'
t1.age = 35

t1.update()

print(t1.age)
print(t2.name)

>>>
99
trk
>>>
```

---

```python
class test1:

    def __init__(self):
        self.name = 'trk'
        self.age = 36

    def compare(self, t2):
        if self.age == t2.age:
            return True
        else:
            return False

t1 = test1()
t2 = test1()

if t1.compare(t2):
    print('they are same')
else:
    print('they are different')

>>>
they are same
>>>
```

---

```python
class test1:

    def __init__(self):
        self.name = 'trk'
        self.age = 36

    def compare(self, t2):
        if self.age == t2.age:
            return True
        else:
            return False

t1 = test1()
t1.age = 30
t2 = test1()

if t1.compare(t2):
    print('they are same')
else:
    print('they are different')
    
>>>
they are different
>>>
```

---

```python
class Car:

    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 8

print(c1.com, c1.mil)
print(c2.com, c2.mil)

>>>
BMW 8
BMW 10
>>>
```

---

```python
class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 8
c1.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

>>>
BMW 8 5
BMW 10 4
>>>
```

---

```python
class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 8
Car.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

>>>
BMW 8 5
BMW 10 5
>>>
```

---

```python
class Student:

    school = 'trk'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

s1 = Student(99,3,1)
s2 = Student(700, 221, 19)

print(s1.avg())
print(s2.avg())

>>>
34.333333333333336
313.3333333333333
>>>
```

---

```python
class Student:

    school = 'trk'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def get_m1(self):
        return self.m1

    def set_m1(self, val):
        self.m1 = val

s1 = Student(99,3,1)
s2 = Student(700, 221, 19)

print(s1.get_m1())
s1.set_m1(1000)
print(s1.get_m1())

>>>
99
1000
>>>
```

---

```python
class Student:

    school = 'trk'

    def __init__(self, m1):
        self.m1 = m1

    def get_m1(self):
        return self.m1

    def set_m1(self, val):
        self.m1 = val

s1 = Student(100)

def kapcsolo():
    i = input('legyen valtoztatas? \n '
              'Yes = y, No = n \n '
              'alapbol 100-as az erosseg \n \n ')
    if i == 'y':
        v = int(input('allitsd be... \n'))
        s1.set_m1(v)
        print('az uj erosseg: ', s1.get_m1())
    else:
        print('az erosseg 100-as maradt')

kapcsolo()

>>>
legyen valtoztatas? 
 Yes = y, No = n 
 alapbol 100-as az erosseg 
 
 y
allitsd be... 
111
az uj erosseg:  111

legyen valtoztatas? 
 Yes = y, No = n 
 alapbol 100-as az erosseg 
 
 n
az erosseg 100-as maradt 100
>>>
```

---

```python
class Student:

    school = 'trk'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    @classmethod
    def info(cls):
        return cls.school

s1 = Student(100,200,300)


print(Student.info())

>>>
trk
>>>
```

---

```python
class Student:

    school = 'trk'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student class...in abc module")

s1 = Student(100,200,300)


print(Student.getSchool())
Student.info()

>>>
trk
This is Student class...in abc module
>>>
```

---

```python
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print(self.name, self.rollno)

s1 = Student('trk', 2)
s2 = Student('vrg', 3)

s1.show()
s2.show()

>>>
trk 2
vrg 3
>>>
```

---

```python
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop

    def show(self):
        print(self.name, self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

s1 = Student('trk', 2)
s2 = Student('vrg', 3)

lap1 = s1.lap
lap2 = s2.lap

print(lap1)

>>>
<class '__main__.Student.Laptop'>
>>>
```

---

```python
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('trk', 2)
s2 = Student('vrg', 3)

lap1 = Student.Laptop()
lap2 = Student.Laptop()

s1.show()

>>>
trk 2
HP i5 8
>>>
```

---

```python
class A:

    def Feat1(self):
        print("Feat1 is working")

    def Feat2(self):
        print("Feat2 is working")

a1 = A()

a1.Feat1()
a1.Feat2()

>>>
Feat1 is working
Feat2 is working
>>>
```

---

```python
class A:

    def Feat1(self):
        print("Feat1 is working")

    def Feat2(self):
        print("Feat2 is working")

class B(A):

    def Feat3(self):
        print("Feat3 is working")

    def Feat4(self):
        print("Feat4 is working")

a1 = A()
b1 = B()


a1.Feat1()
a1.Feat2()

b1.Feat1()
b1.Feat2()
b1.Feat3()
b1.Feat4()

>>>
Feat1 is working
Feat2 is working
Feat1 is working
Feat2 is working
Feat3 is working
Feat4 is working
>>>
```

---

```python
class A:

    def Feat1(self):
        print("Feat1 is working")

    def Feat2(self):
        print("Feat2 is working")

class B(A):

    def Feat3(self):
        print("Feat3 is working")

    def Feat4(self):
        print("Feat4 is working")

class C(B):

    def Feat5(self):
        print("Feat5 is working")

    def Feat6(self):
        print("Feat6 is working")

a1 = A()
b1 = B()
c1 = C()

print('------------ \n')
print('A class: \n')
a1.Feat1()
a1.Feat2()
print('\n ------------ \n')
print('B class: \n')
b1.Feat1()
b1.Feat2()
b1.Feat3()
b1.Feat4()
print('\n ------------ \n')
print('C class: \n')
c1.Feat1()
c1.Feat2()
c1.Feat3()
c1.Feat4()
c1.Feat5()
c1.Feat6()

>>>
------------ 

A class: 

Feat1 is working
Feat2 is working

 ------------ 

B class: 

Feat1 is working
Feat2 is working
Feat3 is working
Feat4 is working

 ------------ 

C class: 

Feat1 is working
Feat2 is working
Feat3 is working
Feat4 is working
Feat5 is working
Feat6 is working
>>>
```

```python
class A:

    def Feat1(self):
        print("Feat1 is working")

    def Feat2(self):
        print("Feat2 is working")

class B():

    def Feat3(self):
        print("Feat3 is working")

    def Feat4(self):
        print("Feat4 is working")

class C(A,B):

    def Feat5(self):
        print("Feat5 is working")

    def Feat6(self):
        print("Feat6 is working")

a1 = A()
b1 = B()
c1 = C()

print('------------ \n')
print('A class: \n')
a1.Feat1()
a1.Feat2()
print('\n ------------ \n')
print('B class: \n')
b1.Feat3()
b1.Feat4()
print('\n ------------ \n')
print('C class: \n')
c1.Feat1()
c1.Feat2()
c1.Feat3()
c1.Feat4()
c1.Feat5()
c1.Feat6()

>>>
------------ 

A class: 

Feat1 is working
Feat2 is working

 ------------ 

B class: 

Feat3 is working
Feat4 is working

 ------------ 

C class: 

Feat1 is working
Feat2 is working
Feat3 is working
Feat4 is working
Feat5 is working
Feat6 is working
>>>
```

---

```python
class A:

    def __init__(self):
        print('Print A init')

    def Feat1(self):
        print("Feat1 is working")

    def Feat2(self):
        print("Feat2 is working")

class B(A):

    def __init__(self):
        print('Print B init')

    def Feat3(self):
        print("Feat3 is working")

    def Feat4(self):
        print("Feat4 is working")


b = B()

>>>
Print B init
>>>
```

---

```python
class A:

    def __init__(self):
        print('Print A init')

    def Feat1(self):
        print("Feat1 is working")

    def Feat2(self):
        print("Feat2 is working")

class B(A):

    def __init__(self):
        super().__init__()
        print('Print B init')

    def Feat3(self):
        print("Feat3 is working")

    def Feat4(self):
        print("Feat4 is working")


b = B()

>>>
Print A init
Print B init
>>>
```

---

```python
class A:

    def __init__(self):
        print('Print A init')

    def Feat1(self):
        print("Feat1 is working")

    def Feat2(self):
        print("Feat2 is working")

class B:

    def __init__(self):
        print('Print B init')

    def Feat3(self):
        print("Feat3 is working")

    def Feat4(self):
        print("Feat4 is working")

class C(A,B):

    def __init__(self):
        print('Print C init')


b = C()

>>>
Print C init
>>>
```

---

```python
class A:

    def __init__(self):
        print('Print A init')

    def Feat1(self):
        print("Feat1 is working")

    def Feat2(self):
        print("Feat2 is working")

class B:

    def __init__(self):
        print('Print B init')

    def Feat3(self):
        print("Feat3 is working")

    def Feat4(self):
        print("Feat4 is working")

class C(A,B):

    def __init__(self):
        super().__init__()
        print('Print C init')


b = C()

>>>
Print A init
Print C init
>>>
```

---

```python
class PyCharm:

    def execute(self):
        print("compiling")
        print("running")

class Laptop:

    def code(self, ide):
        ide.execute()

ide = PyCharm()

lap1 = Laptop()
lap1.code(ide)

>>>
compiling
running
>>>
```

---

```python
class PyCharm:

    def execute(self):
        print("compiling")
        print("running")

class MyEditor:

    def execute(self):
        print("Spell check")
        print("Convention check")

class Laptop:

    def code(self, ide):
        ide.execute()

ide = PyCharm()
mye = MyEditor()

lap1 = Laptop()

lap1.code(ide)
lap1.code(mye)

>>>
compiling
running
Spell check
Convention check
>>>
```

---

```python
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3

s1 = Student(50, 55)
s2 = Student(41, 44)

s3 = s1+s2

print(s3.m1)

>>>
91
>>>
```

---

```python
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

s1 = Student(50, 55)
s2 = Student(141, 44)

s3 = s1+s2

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')


>>>
s2 wins
>>>
```

---

```python
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return self.m1, self.m2

s1 = Student(50, 55)
s2 = Student(141, 44)

s3 = s1+s2

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')

a = 9
print(a.__str__())
print(s1.__str__())

>>>
s2 wins
9
(50, 55)
>>>
```

---

```python
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a, b):
        s = a+b

        return s

s1 = Student(55,12)

print(s1.sum(5,9))

>>>
14
>>>
```

---

```python
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):

        s = 0

        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a

        return s

s1 = Student(55,12)

print('3 nums: 5+9+6 = ', s1.sum(5,9,6))
print('2 nums: 5+9 = ',s1.sum(5,9,))
print('only 1 num: 5 = ',s1.sum(5))

>>>
3 nums: 5+9+6 =  20
2 nums: 5+9 =  14
only 1 num: 5 =  5
>>>
```

---

```python
class A:

    def show(self):
        print('in A Show')

class B(A):
    pass

a1 = B()
a1.show()

>>>
in A Show
>>>
```

---

```python
class A:

    def show(self):
        print('in A Show')

class B(A):

    def show(self):
        print('in B Show')

a1 = B()
a1.show()

>>>
in B Show
>>>
```

---
