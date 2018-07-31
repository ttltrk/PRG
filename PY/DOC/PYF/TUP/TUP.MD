
---

### Python tuples

---

```python
tup = ("apple", "banana", "cherry")

print(tup)

>>>
('apple', 'banana', 'cherry')
>>>
```

---

```python
tup = ("apple", "banana", "cherry")

print(tup[1])

>>>
banana
>>>
```

---

```python
tup = ("apple", "banana", "cherry")

tup[1] = "blackcurrant"

>>>
Traceback (most recent call last):
  File "/Users/attilatorok/Desktop/tst.py", line 3, in <module>
    tup[1] = "blackcurrant"
TypeError: 'tuple' object does not support item assignment
>>>
```

---

```python
tup = ("apple", "banana", "cherry")

print(len(tup))

>>>
3
>>>
```

---
