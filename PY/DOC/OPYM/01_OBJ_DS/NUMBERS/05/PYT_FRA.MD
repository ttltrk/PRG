
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD) - [Objects and Data Sructures](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/OBJ_DS.MD) - [Numbers](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/NUMBERS/NUMBERS.MD)

---

### Python Fractions

---

```python
import fractions

print(fractions.Fraction(1.5))
print(fractions.Fraction(5))
print(fractions.Fraction(1,3))

>>>
3/2
5
1/3
>>>
```

```python
import fractions

print(fractions.Fraction(1.1))
print(fractions.Fraction('1.1'))

>>>
2476979795053773/2251799813685248
11/10
>>>
```

```python
from fractions import Fraction as F

print(F(1,3) + F(1,3))
print(1 / F(5,6))
print(F(-3,10) > 0)
print(F(-3,10) < 0)

>>>
2/3
6/5
False
True
>>>
```

---
