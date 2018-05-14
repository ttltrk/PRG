

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
