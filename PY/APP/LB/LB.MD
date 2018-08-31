
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

### Loop back script

---

```python
def again():
    return work()

def exit():
    ch = input('do you want really log off: Y or N')
    if ch == 'Y':
        print('bye')
    else:
        return again()

def work():
    while True:
        a = input('word ')
        if a != 'exit':
            return again()
        else:
            return exit()

again()
```
