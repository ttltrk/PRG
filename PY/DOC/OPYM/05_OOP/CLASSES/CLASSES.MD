
Classes
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD)

[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Object%20Oriented%20Programming.ipynb)

```python
class Sample(object):
    pass

x = Sample()

print(x)
	
>>>
<__main__.Sample object at 0x02D77E50>
>>>
```

```python
class Dog(object):

    def __init__(self, breed):
        self.breed = breed

sam = Dog(breed="Lab")

print(sam)

>>>
<__main__.Dog object at 0x02D27E50>
>>>
```

```python
class Dog(object):

    def __init__(self, breed):
        self.breed = breed

sam = Dog(breed="Lab")

print(sam.breed)

>>>
Lab
>>>
```

```python
class Dog(object):

    #Class Object Attribute
    species = "mammal"

    def __init__(self, breed):
        self.breed = breed

sam = Dog(breed="Lab")

print(sam.species)

>>>
mammal
>>>
```

```python
class Dog(object):

    #Class Object Attribute
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

sam = Dog(breed="Lab", name = "Sammy")

print(sam.name)

>>>
Sammy
>>>
```

```python
class Dog(object):

    #Class Object Attribute
    species = "mammal"

    def __init__(self, breed, name, fur=True):
        self.breed = breed
        self.name = name
        self.fur = fur

sam = Dog(breed="Lab", name = "Sammy")

print(sam.fur)

>>>
True
>>>
```
