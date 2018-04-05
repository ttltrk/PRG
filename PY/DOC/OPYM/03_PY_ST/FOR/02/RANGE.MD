
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD) - [Python Statements](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/03_PY_ST/PY_ST.MD) - [for loops](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/03_PY_ST/FOR/FORLOOP.MD)

---

### range()

---

```python
print(range(10))
print(list(range(10)))
print(list(range(2, 8)))
print(list(range(2, 20, 3)))

>>>
range(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 3, 4, 5, 6, 7]
[2, 5, 8, 11, 14, 17]
>>>
```

---

```python
genre = ['pop', 'rock', 'jazz']

for i in range(len(genre)):
	print("I like", genre[i])

>>>
I like pop
I like rock
I like jazz
>>>
```

---
