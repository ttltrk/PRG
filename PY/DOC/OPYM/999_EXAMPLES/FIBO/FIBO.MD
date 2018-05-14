

---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD) - [Examples/Apps](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/999_EXAMPLES/EXAM.MD)

---

### Fibonacci

---

```python
def fib(n):
    fibonacci = []
    a = 0
    b = 1
    for i in range(n):
        fibonacci.append(b)
        a, b = b, a+b
    return fibonacci

print(fib(10))

>>>
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>>
```
