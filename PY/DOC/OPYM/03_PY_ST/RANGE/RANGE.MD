
---

### range() - other examples

---

```python
>>> x = range(1,5)
>>> type (x)
<class 'range'>
>>> 
```

```python
>>> list(range(0, 10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
```

```python
>>> list(range(20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 
```

```python
>>> x = list(range(0,10))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> type(x)
<class 'list'>
>>> 
```

```python
>>> start = 5
>>> stop = 20
>>> list(range(start,stop))
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 
```


```python
>>> start = 5
>>> stop = 20
>>> list(range(start,stop,2))
[5, 7, 9, 11, 13, 15, 17, 19]
>>> 
```

```python
l = [1, 2, 3, 4, 5]

for num in range(1,11):
    print (num)
	
>>>
1
2
3
4
5
6
7
8
9
10
>>> 
```

---

[src - jupyter](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Range%28%29.ipynb)

---
