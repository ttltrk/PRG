
Methods
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD)

[jupyter](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Object%20Oriented%20Programming.ipynb)

```python
class Circle(object):
    pass
	
>>>
None
>>>
```

```python
class Circle(object):

    #Class object attributes
    pi = 3.14

    def __init__(self):
        pass

c = Circle()

print(c)

>>>
<__main__.Circle object at 0x02D47E50>
>>>
```

```python
class Circle(object):

    #Class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

c = Circle()

print(c.pi)
print(c.radius)

>>>
3.14
1
>>>
```

```python
class Circle(object):

    #Class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

c = Circle(radius = 100)

print(c.pi)
print(c.radius)

>>>
3.14
100
>>>
```

```python
class Circle(object):

    #Class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        #radius**2 * pi
        return (self.radius**2) * Circle.pi

c = Circle(radius = 100)

print(c.area)

>>>
<bound method Circle.area of <__main__.Circle object at 0x02D87E50>>
>>>
```

```python
class Circle(object):

    #Class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        #radius**2 * pi
        return (self.radius**2) * Circle.pi

c = Circle(radius = 100)

print(c.area())

>>>
31400.0
>>>
```

```python
class Circle(object):

    #Class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        #radius**2 * pi
        return (self.radius**2) * Circle.pi

    def set_radius(self, new_radius):
        #This methods takes in a radius and resets the current radius of the circle
        self.radius = new_radius
        

c = Circle(radius = 10)
c.set_radius(20)

print(c.radius)

>>>
20
>>>
```

```python
class Circle(object):

    #Class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        #radius**2 * pi
        return (self.radius**2) * Circle.pi

    def set_radius(self, new_radius):
        #This methods takes in a radius and resets the current radius of the circle
        self.radius = new_radius

    def get_radius(self):
        return self.radius
        

c = Circle(radius = 10)

print(c.get_radius())

>>>
10
>>>
```
