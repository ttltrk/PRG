---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

### Read from IN1 and IN2, compile and write to OUT

---

```python
with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\TEST\\D1.txt', mode='r') as d1_txt:
    d1 = d1_txt.read()

with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\TEST\\D2.txt', mode='r') as d2_txt:
    d2 = d2_txt.read()

out = d1+d2

with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\TEST\\OUT.txt', mode='w') as out_txt:
    outtxt = out_txt.write(out)

with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\TEST\\OUT.txt', mode='r') as out_txt:
    outtxt = out_txt.read()

print(outtxt)
```
