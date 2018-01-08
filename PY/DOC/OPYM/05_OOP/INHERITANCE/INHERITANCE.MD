
Inheritance
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD)

[jupyter](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Object%20Oriented%20Programming.ipynb)

```python
class Animal(object):

    def __init__(self):
        print("Animal created")

a = Animal()

print(a)

>>>
Animal created
>>>
```

```python
class Animal(object):

    def __init__(self):
        print("Animal created")

    def whoAmI (self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("woof!")

d = Dog()

print(d)
print(d.whoAmI())
print(d.eat())
print(d.bark())

>>>
Animal created
Dog created
Dog
Eating
woof!
>>>
```
