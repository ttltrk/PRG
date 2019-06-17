


```python
#-----------------------------------------------------------

import funks
import funks2

#-----------------------------------------------------------

def exit():
    print('bye')

def again():
    return go()

#-----------------------------------------------------------

def go():
    while True:
        ch = int(input('1 - 2 - 3 - 99 \n'))
        var = ' '
        if ch == 1 and ch != 99:
            funks.first()
            var = again()
        elif ch == 2 and ch != 99:
            funks.second()
            var = again()
        elif ch == 3 and ch != 99:
            funks2.third()
            var = again()
        elif ch == 99:
            var = exit()
        return var

#-----------------------------------------------------------

go()
```

```python
#funks.py

def first():
    print('oh yes first \n')

def second():
    print('yeah second \n')
```    
   
```python
#funks2.py
def third():
    ch = input('hey, go for it \n \n')
    print(ch)    
```
