
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [CF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/ControlFlow/CF.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Control Flow - decorators</h3>

---

```python
def hello():
    return 'hi'

print(hello())
greet = hello
print(greet())

>>>
hi
hi
>>>
```

```python
def hello(name='trk'):
    print('the hello() function was executed')

    def greet():
        return '\t this is tge greet() func inside hello'

    print(greet())

hello()

>>>
the hello() function was executed
	 this is tge greet() func inside hello
>>>
```

```python
def hello(name='trk'):
    print('the hello() function was executed')

    def greet():
        return '\t this is the greet() func inside hello'

    def welcome():
        return '\t this is welcome() inside hello '

    print(greet())
    print(welcome())
    print('this is the end of hello() function')

hello()

>>>
the hello() function was executed
	 this is the greet() func inside hello
	 this is welcome() inside hello 
this is the end of hello() function
>>>
```

```python
def hello(name='trk'):
    print('the hello() function was executed')

    def greet():
        return '\t this is the greet() func inside hello'

    def welcome():
        return '\t this is welcome() inside hello '

    print('Im going to return a function')

    if name == 'trk':
        return greet
    else:
        return welcome

my_new_func = hello('trk')

print(my_new_func())

>>>
the hello() function was executed
Im going to return a function
	 this is the greet() func inside hello
>>>
```

```python
def cool():

    def super_cool():
        return 'I am very cool!'

    return super_cool

some_func = cool()
print(some_func())

>>>
I am very cool!
>>>
```

```python
def hello():
    return 'hi trk'

def other(some_def_func):
    print('Other code runs here')
    print(some_def_func)

print(hello())
other(hello)

>>>
hi trk
Other code runs here
<function hello at 0x00F29B28>
>>>
```

```python
def new_decorator(original_func):

    def wrap_func():
        print('some extra code, before the original function')

        original_func()
        print('some extra code, after the original function')

    return wrap_func

def func_needs_decorator():
    print('I want to be decorated')

#func_needs_decorator()
decrated_func = new_decorator(func_needs_decorator)
decrated_func()

>>>
some extra code, before the original function
I want to be decorated
some extra code, after the original function
>>>
```

```python
def new_decorator(original_func):

    def wrap_func():
        print('some extra code, before the original function')

        original_func()
        print('some extra code, after the original function')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print('I want to be decorated')

func_needs_decorator()

>>>
some extra code, before the original function
I want to be decorated
some extra code, after the original function
>>>
```

<a href='#^'>^^^</a>

---
