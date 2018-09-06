---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

### Read from IN, write to OUT

---

```python
with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\TEST\\IN.txt', mode='r') as in_txt:
    intxt = in_txt.read()

with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\TEST\\OUT.txt', mode='w') as out_txt:
    outtxt = out_txt.write(intxt)

with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\TEST\\OUT.txt', mode='r') as out_txt:
    outtxt = out_txt.read()

print(outtxt)
```
