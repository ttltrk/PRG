
Datetime
======

[<<<]()

[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Datetime.ipynb)

```python
import datetime

t = datetime.time(5, 25, 1)

print(t)
print(datetime.time.min)
print(datetime.time.max)

>>>
05:25:01
00:00:00
23:59:59.999999
>>>
```


```python
import datetime

today = datetime.date.today()

print(today)

>>>
2018-02-08
>>>
```


```python
import datetime

today = datetime.date.today()

print(today.day)

>>>
8
>>>
```


```python
import datetime

d1 = datetime.date(2018,2,9)
print(d1)

d2 = d1.replace(year=1983)
print(d2)

d3 = d1-d2
print(d3)

>>>
2018-02-09
1983-02-09
12784 days, 0:00:00
>>>
```

