
Functions as Arguments
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD)

[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Decorators.ipynb)

```python
def hello():
  return 'hi trk!'
  
def other(func):
  print('other code goes here')
  print(func())
  
print(other(hello))

>>>
other code goes here
hi trk!
>>>
```


```python
def new_decorator(func):
  
  def wrap_func():
    print('code here, before executing the func')
    
    func()
    
    print('code here will execute after the func()')
    
  return wrap_func
  
def func_needs_decorator():
  print('This function needs a decorator')
  
func_needs_decorator = new_decorator(func_needs_decorator)

print(func_needs_decorator())

>>>
code here, before executing the func
This function needs a decorator
code here will execute after the func()
>>>
```


```python
def new_decorator(func):
  
  def wrap_func():
    print('code here, before executing the func')
    
    func()
    
    print('code here will execute after the func()')
    
  return wrap_func
  
@new_decorator
def func_needs_decorator():
  print('This function needs a decorator')
  
print(func_needs_decorator())

>>>
code here, before executing the func
This function needs a decorator
code here will execute after the func()
>>>
```


