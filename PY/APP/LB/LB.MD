
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

### Loop back script

---

```python
def again():
    return work()

def exit():
    print('bye')

def work():
    while True:
        a = input('word ')
        if a != 'exit':
            return again()
        else:
            return exit()

again()
```
