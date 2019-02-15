
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Errors and Exceptions</h3>

---

```python
def add(n1,n2):
    print(n1+n2)

num1 = 10
num2 = input('add a number ')

add(num1,num2)

>>>
add a number 20
Traceback (most recent call last):
  File "C:tt3.py", line 12, in <module>
    add(num1,num2)
  File "C:t3.py", line 7, in add
    print(n1+n2)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

```python
try:
    result = 10+10

except:
    print('hey it looks like you are not adding correctly!')

print(result)

>>>
20
>>>
```

```python
try:
    result = 10+'10'

except:
    print('hey it looks like you are not adding correctly!')

else:
    print('add went well')
    print(result)

>>>
hey it looks like you are not adding correctly!
>>>
```

```python
try:
    result = 10+10

except:
    print('hey it looks like you are not adding correctly!')

else:
    print('add went well')
    print(result)

>>>
add went well
20
>>>
```

```python
try:
    f = open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\TEST\\testfile.txt', 'w') 
    f.write('Write a test line')
    
except TypeError:
    print('There was a type error!')

except OSError:
    print('Hey you have an OS error!')

finally:
    print('I always run!')

>>>
I always run!
>>>
```

```python
def ask_for_int():
    try:
        result = int(input('Please provide number: '))
    except:
        print('Whoops, that is not a number')
    finally:
        print('End of try/except/finally')

ask_for_int()

>>>
Please provide number: 17
End of try/except/finally
>>>

>>>
Please provide number: dd
Whoops, that is not a number
End of try/except/finally
>>>
```

```python
def ask_for_int():

    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Whoops, that is not a number')
            continue
        else:
            print('Yes thank you')
            break
        finally:
            print('End of try/except/finally')
            print('I will always run at the end')

ask_for_int()

>>>
Please provide number: 2
Yes thank you
End of try/except/finally
I will always run at the end
>>>

>>>
Please provide number: dd
Whoops, that is not a number
End of try/except/finally
I will always run at the end
Please provide number: cc
Whoops, that is not a number
End of try/except/finally
I will always run at the end
Please provide number: 3
Yes thank you
End of try/except/finally
I will always run at the end
>>>
```

```python
try:
    for i in ['a','b','c']:
        print(i**2)

except:
    print('Type error, watch out!')

>>>
Type error, watch out!
>>>
```

```python
try:
    x = 5
    y = 0
    z = x/y

except:
    print('error')

finally:
    print('all done')

>>>
error
all done
>>>
```

```python
def ask():

    while True:
        try:
            n = int(input('Enter a number: '))
        except:
            print('Please try again! \n')
            continue
        else:
            break

    print('Your number squared is: ')
    print(n**2)

ask()

>>>
Enter a number: we
Please try again! 

Enter a number: pe
Please try again! 

Enter a number: ti
Please try again! 

Enter a number: 10
Your number squared is: 
100
>>> 
```

---


