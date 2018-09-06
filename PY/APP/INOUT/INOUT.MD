---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

### Read from IN1 and IN2, compile and write to OUT

---

```python
with open('C:\\path\\path\\D1.txt', mode='r') as d1_txt:
    d1 = d1_txt.read()

with open('C:\\path\\path\\D2.txt', mode='r') as d2_txt:
    d2 = d2_txt.read()
    
#string to list
sp1 = d1.split()
sp2 = d2.split()

sp = sp1+sp2

#list to set
ss = set(sp)
sss = sorted(ss)

#set to string
ssp = ' '.join(sss)

with open('C:\\path\\path\\OUT.txt', mode='w') as out_txt:
    outtxt = out_txt.write(ssp)

with open('C:\\path\\path\\OUT.txt', mode='r') as out_txt:
    outtxt = out_txt.read()

print(outtxt)
```
