
Special Methods
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD)

[jupyter](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Object%20Oriented%20Programming.ipynb)

```python
class Book(object):

    def __init__(self, title, author, pages):

        print("A book has been created!")
        self.title = title
        self.author = author
        self.pages = pages

b = Book("Python","Jose",100)

print(b)

>>>
A book has been created!
>>>
```

```python
class Book(object):

    def __init__(self, title, author, pages):

        print("A book has been created!")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):

        return("Title: %s, Author: %s, pages: %s " % (self.title, self.author, self.pages))

b = Book("Python","Jose",100)

print(b)

>>>
A book has been created!
Title: Python, Author: Jose, pages: 100
>>>
```

```python
class Book(object):

    def __init__(self, title, author, pages):

        print("A book has been created!")
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):

        return self.pages

b = Book("Python","Jose",100)

print(len(b))

>>>
A book has been created!
100
>>>
```

```python
class Book(object):

    def __init__(self, title, author, pages):

        print("A book has been created!")
        self.title = title
        self.author = author
        self.pages = pages

    def __del__(self):

        print("A book is gone!")

b = Book("Python","Jose",100)

del b

>>>
A book has been created!
A book is gone!
>>>
```
