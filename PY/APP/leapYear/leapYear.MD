
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

### Python - Leap Year

```python
def is_leap(year):
    v1 = (year % 4 == 0)
    v2 = (year % 100 != 0)
    v3 = (year % 400 == 0)
    return v1 and (v2 or v3)

print(is_leap(int(input('year? \n \n'))))
```
