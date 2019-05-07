
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - OOP</h3>

---

```python
#==============================================================

class Employee:

    def __init__(self, name, number, place):
        self.name = name
        self.number = number
        self.place = place

    def displayEmployeeDetailsName(self):
        return self.name

    def displayEmployeeDetailsNumber(self):
        return self.number

    def displayEmployeeDetailsPlace(self):
        return self.place

class Dates:

    def __init__(self, date):
        self.date = date

    def displayEmpDate(self):
        return self.date

#==============================================================

e_emp1 = Employee('Su', 2, 'DS')
e_emp2 = Employee('Mate', 3, 'BA')
d_emp1 = Dates(2015)
d_emp2 = Dates(2017)

#==============================================================

ee_11 = e_emp1.displayEmployeeDetailsName()
ee_12 = e_emp1.displayEmployeeDetailsNumber()
ee_13 = e_emp1.displayEmployeeDetailsPlace()

ee_21 = e_emp2.displayEmployeeDetailsName()
ee_22 = e_emp2.displayEmployeeDetailsNumber()
ee_23 = e_emp2.displayEmployeeDetailsPlace()

de_11 = d_emp1.displayEmpDate()
de_21 = d_emp2.displayEmpDate()

#==============================================================

print(ee_11 , ee_12 , de_11)
print(ee_13, ee_22, de_21)

>>>
Su 2 2015
DS 3 2017
>>>
```

<a href='#^'>^^^</a>

---

```python
#==============================================================

class N1:

    def __init__(self, n1):
        self.n1 = n1
        
    def Number1(self):
        return self.n1

class N2:

    def __init__(self, n2):
        self.n2 = n2

    def Number2(self):
        return self.n2

#==============================================================

NUM1 = N1(10)
NUM2 = N2(15)

#==============================================================

NN1 = NUM1.Number1()
NN2 = NUM2.Number2()

#==============================================================

print(NN1 + NN2)

>>>
25
>>>
```

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

```python
class NameOfClass():

    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        print(self.param1)
```

```python
class Dog():

    def __init__(self,breed):
        self.breed = breed

my_dog = Dog(breed='Lab')

print(my_dog.breed)

>>>
Lab
>>>
```

```python
class Dog():

    def __init__(self,mybreed):
        self.breed = mybreed

my_dog = Dog(mybreed='Huskie')

print(my_dog.breed)

>>>
Huskie
>>>
```

```python
class Dog():

    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed='Huskie', name='Sam', spots='False')

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)

>>>
Huskie
Sam
False
>>>
```

```python
class Dog():

    species ='mammal'

    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed='Huskie', name='Sam', spots='False')

print(my_dog.species)

>>>
mammal
>>>
```

```python
class Dog():

    species ='mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    def bark(self):
        print('WOOF')

my_dog = Dog('lab','Frankie')

print(my_dog.name)
print(my_dog.species)
my_dog.bark()

>>>
Frankie
mammal
WOOF
>>>
```

```python
class Dog():

    species ='mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    def bark(self):
        print('WOOF, My name is {}'.format(self.name))

my_dog = Dog('lab','Frankie')

my_dog.bark()

>>>
WOOF, My name is Frankie
>>>
```

```python
class Dog():

    species ='mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    def bark(self,number):
        print('WOOF, My name is {} and the number is {}'.format(self.name,number))

my_dog = Dog('lab','Frankie')

my_dog.bark(2)

>>>
WOOF, My name is Frankie and the number is 2
>>>
```

```python
class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle()

print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())

>>>
3.14
1
6.28
>>>
```

```python
class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def get_circumference(self):
        print(self.radius * self.pi * 2)

my_circle = Circle(5)

print(my_circle.pi)
print(my_circle.radius)
my_circle.get_circumference()

>>>
3.14
5
31.4
>>>
```

```python
class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi

    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(5)

print(my_circle.area)

>>>
78.5
>>>
```

```python
class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*Circle.pi

    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(5)

print(my_circle.area)
print(my_circle.get_circumference())

>>>
78.5
31.4000000
>>>
```

```python
class Animal():
    
    def __init__(self):
        print('ANIMAL CREATED')

myanimal = Animal()

myanimal

>>>
ANIMAL CREATED
>>>
```

```python
class Animal():
    
    def __init__(self):
        print('ANIMAL CREATED')

    def whoami(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

myanimal = Animal()

myanimal.eat()
myanimal.whoami()

>>>
ANIMAL CREATED
I am eating
I am an animal
>>>
```

```python
class Animal():
    
    def __init__(self):
        print('ANIMAL CREATED')

    def whoami(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

mydog = Dog()

>>>
ANIMAL CREATED
Dog created
>>>
```

```python
class Animal():
    
    def __init__(self):
        print('ANIMAL CREATED')

    def whoami(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

mydog = Dog()
mydog.eat()
mydog.whoami()

>>>
ANIMAL CREATED
Dog created
I am eating
I am an animal
>>>
```

```python
class Animal():
    
    def __init__(self):
        print('ANIMAL CREATED')

    def whoami(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def whoami(self):
        print('I am a dog')

myanimal = Animal()
mydog = Dog()

mydog.whoami()
myanimal.whoami()

>>>
ANIMAL CREATED
ANIMAL CREATED
Dog created
I am a dog
I am an animal
>>>
```

```python
class Animal():
    
    def __init__(self):
        print('ANIMAL CREATED')

    def whoami(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def eat(self):
        print('I am a dog and eating')

    def bark(self):
        print('WOOF')

mydog = Dog()

mydog.eat()
mydog.bark()

>>>
ANIMAL CREATED
Dog created
I am a dog and eating
WOOF
>>>
```

```python
class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says woof'

class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says meow'

niko = Dog('niko')
felix = Cat('felix')

print(niko.speak())
print(felix.speak())

>>>
niko says woof
felix says meow
>>>
```

```python
class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says woof'

class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says meow'

def pet_speak(pet):
    print(pet.speak())

niko = Dog('niko')
felix = Cat('felix')

pet_speak(niko)
pet_speak(felix)

>>>
niko says woof
felix says meow
>>>
```

```python
class Book():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

b = Book('Python manual','trk',99)

print(b)
print(str(b))
print(len(b))

>>>
Python manual by trk
Python manual by trk
99
>>>
```

```python
class Book():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')

b = Book('Python manual','trk',99)

del b
print(b)

>>>
A book object has been deleted

Traceback (most recent call last):
    print(b)
NameError: name 'b' is not defined
>>>
```

```python
class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):

        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):

        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return (y2-y1) / (x2-x1)

c1 = (3,2)
c2 = (8,10)

myline = Line(c1,c2)

print(myline.distance())
print(myline.slope())

>>>
9.433981132056603
1.6
>>>
```

```python
class Cylinder:

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * 3.14 * (self.radius)**2

    def surface_area(self):
        top = 3.14 * (self.radius**2)
        return (2*top) + (2*3.14*self.radius*self.height)

mycyl = Cylinder(2,3)

print(mycyl.volume())
print(mycyl.surface_area())

>>>
56.52
94.2
>>>
```

```python
class Account():

    def __init__(self,owner,balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):

        self.balance = self.balance + dep_amt
        print(f'Added {dep_amt} to the balance')

    def withdrawal(self,wd_amt):

        if self.balance >= wd_amt:
            self.balance = self.balance
            print('Withdrawal accepted')
        else:
            print('Sorry not enough funds')

    def __str__(self):

        return f'Owner: {self.owner} \nBalance: {self.balance}'

a = Account('Sam',500)

print(a)
a.deposit(100)
print(a)

>>>
Owner: Sam 
Balance: 500
Added 100 to the balance
Owner: Sam 
Balance: 600
>>>
```

```python
class Account():

    def __init__(self,owner,balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):

        self.balance = self.balance + dep_amt
        print(f'Added {dep_amt} to the balance')

    def withdrawal(self,wd_amt):

        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print('Withdrawal accepted')
        else:
            print('Sorry not enough funds')

    def __str__(self):

        return f'Owner: {self.owner} \nBalance: {self.balance}'

a = Account('Sam',500)

print(a)
a.withdrawal(350)
print(a)

>>>
Owner: Sam 
Balance: 500
Withdrawal accepted
Owner: Sam 
Balance: 150
>>>
```

---

```python
class NameOfClass():

  def __init__(self, param1, param2):
    self.param1 = param1
    self.param2 = param2
  
  def some_methods(self):
    print(self.param1)
```

```python
class Sample():
    pass

my_sample = Sample()

print(type(my_sample))

>>>
<class '__main__.Sample'>
>>>
```

```python
class Dog():

    def __init__(self, breed, name):

        self.breed = breed
        self.name = name

my_dog = Dog(breed='Lab', name='cat')

print(my_dog.breed)
print(my_dog.name)

>>>
Lab
cat
>>>
```

```python
class Complex:
    def __init__(self, alma, korte, szilva):
        self.a = alma
        self.k = korte
        self.sz = szilva

x = Complex(5, 10, 15)

def masik():
    res = x.a + x.k + x.sz
    print('res =', res)
    print('a1 =', x.a)
    print('b1 =', x.k)
    print('c1 =', x.sz)

masik()

>>>
res = 30
a1 = 5
b1 = 10
c1 = 15
>>>
```

```python
class Door:
    def __init__(self, number, status):
        self.number = number
        self.status = status

    def open(self):
        self.status = 'open'

    def close(self):
        self.status = 'closed'

door1 = Door(1, 'closed')
door2 = Door(2, 'open')

print("door1 = Door(1, 'closed') =", door1.number)
print("door2 = Door(2, 'open') =", door2.number)
print("door1 = Door(1, 'closed') =", door1.status)
print("door2 = Door(2, 'open') =", door2.status)

>>>
door1 = Door(1, 'closed') = 1
door2 = Door(2, 'open') = 2
door1 = Door(1, 'closed') = closed
door2 = Door(2, 'open') = open
>>>
```

```python
class Door:

    colour ='brown'

    def __init__(self, number, status):
        self.number = number
        self.status = status

    def open(self):
        self.status = 'open'

    def close(self):
        self.status = 'closed'

door1 = Door(1, 'closed')
door2 = Door(2, 'closed')

print(Door.colour)
print(door1.colour)
print(door2.colour)

Door.colour = 'white'

print(Door.colour)
print(door1.colour)
print(door2.colour)

>>>
brown
brown
brown
white
white
white
>>>
```

```python
class Door:
    colour = 'brown'

    def __init__(self, number, status):
        self.number = number
        self.status = status

    @classmethod
    def knock(cls):
        print("Knock!")

    @classmethod
    def paint(cls, colour):
        cls.colour = colour

    def open(self):
        self.status = 'open'

    def close(self):
        self.status = 'closed'

d = Door
d1 = Door(1, 'open')
d2 = Door(2, 'close')

print(d.colour)
print(d1.colour)
print(d2.colour)

d.paint('white')

print(d.colour)
print(d1.colour)
print(d2.colour)

d1.paint('yellow')

print(d.colour)
print(d1.colour)
print(d2.colour)

>>>
brown
brown
brown
white
white
white
yellow
yellow
yellow
>>>
```

<a href='#^'>^^^</a>

---

