
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
