
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [Pack](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/Pack/Pack.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Packages/Modules/Files - NumPy</h3>

---

<h4 id='^^numpy'></h4>
<a href='#npyarr'>Numpy arrays</a><br>
<a href='#npyarange'>Numpy arange</a><br>
<a href='#npyzeros'>Numpy zeros</a><br>
<a href='#npyones'>Numpy ones</a><br>
<a href='#npylinspace'>Numpy linspace</a><br>
<a href='#npyeye'>Numpy eye</a><br>
<a href='#npyrandomr'>Numpy random rand</a><br>
<a href='#npyrandomrn'>Numpy random randn</a><br>
<a href='#npyrandomri'>Numpy random randint</a><br>
<a href='#npyreshape'>Numpy reshape</a><br>
<a href='#npyarrind'>Numpy array indexing</a><br>
<a href='#npysliceofarr'>Numpy slice of array</a><br>
<a href='#npyarrind'>Numpy array indexing</a><br>

<a href='#^'>^^^</a>

---

<h4 id='npyarr'>Numpy arrays</h4>

```python
import numpy as np

ml = [1,2,3]
a = np.array(ml)
print(a)

>>>
[1 2 3]
>>>
```

```python
import numpy as np

mm = [[1,2,3],[4,5,6],[7,8,9]]
m = np.array(mm)
print(m)

>>>
[[1 2 3]
 [4 5 6]
 [7 8 9]]
>>>
``` 

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='npyarange'>Numpy arange</h4>

```python
import numpy as np

ran1 = np.arange(0,11)
ran2 = np.arange(0,11,2)

print(ran1)
print(ran2)

>>>
[ 0  1  2  3  4  5  6  7  8  9 10]
[ 0  2  4  6  8 10]
>>>
```

```python
import numpy as np

arr = np.arange(1,11)

a = arr > 5

print(a)

>>>
[False False False False False  True  True  True  True  True]
>>>
```

```python
import numpy as np

arr = np.arange(1,11)

a = arr[arr>5]

print(a)

>>>
[ 6  7  8  9 10]
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='npyzeros'>Numpy zeros</h4>

```python
import numpy as np

a = np.zeros(3)
b = np.zeros((2,3))
c = np.zeros((3,3))

print(a)
print(b)
print(c)

>>>
[0. 0. 0.]
[[0. 0. 0.]
 [0. 0. 0.]]
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='npyones'>Numpy ones</h4>

```python
import numpy as np

a = np.ones(3)
b = np.ones((2,3))
c = np.ones((3,3))

print(a)
print(b)
print(c)

>>>
[1. 1. 1.]
[[1. 1. 1.]
 [1. 1. 1.]]
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='npylinspace'>Numpy linspace</h4>

```python
import numpy as np

a = np.linspace(0,5,10)

print(a)

>>>
[0.         0.55555556 1.11111111 1.66666667 2.22222222 2.77777778
 3.33333333 3.88888889 4.44444444 5.        ]
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='npyeye'>Numpy eye</h4>

```python
import numpy as np

x = np.eye(1)
a = np.eye(2)
b = np.eye(3)
c = np.eye(4)
d = np.eye(5)

print(x)
print(a)
print(b)
print(c)
print(d)

>>>
[[1.]]
[[1. 0.]
 [0. 1.]]
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='npyrandomr'>Numpy random rand</h4>

```python
import numpy as np

a = np.random.rand(3)
b = np.random.rand(3,3)

print(a)
print(b)

>>>
[0.26010697 0.50160926 0.6739515 ]
[[0.47716672 0.6133023  0.06112184]
 [0.65200764 0.0232473  0.30127692]
 [0.14864509 0.48827363 0.44294204]]
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='npyrandomrn'>Numpy random randn</h4>

```python
import numpy as np

a = np.random.randn(3)

print(a)

>>>
[ 0.47887281 -0.66330668 -1.02834794]
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='npyrandomri'>Numpy random randint</h4>

```python
import numpy as np

a = np.random.randint(0,50)
b = np.random.randint(0,50,5)

print(a)
print(b)

>>>
43
[ 8 10 25 23 10]
>>>
```

```python
import numpy as np

b = np.random.randint(0,50,5)
bmax = b.max()
bmin = b.min()

print(b)
print(bmax)
print(bmin)

>>>
[34 31 15 46  6]
46
6
>>>
```

```python
import numpy as np

b = np.random.randint(0,50,5)
bmax = b.max()
bmin = b.min()
bamax = b.argmax()
bamin = b.argmin()

print(b)
print(bmax)
print(bmin)
print(bamax)
print(bamin)

>>>
[35 17 39 21 10]
39
10
2
4
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='npyreshape'>Numpy reshape</h4>

```python
import numpy as np

ran1 = np.arange(0,25)
re = ran1.reshape(5,5)

print(re)

>>>
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
>>>
```

```python
import numpy as np

arr = np.arange(50).reshape(5,10)
print(arr)

>>>
[[ 0  1  2  3  4  5  6  7  8  9]
 [10 11 12 13 14 15 16 17 18 19]
 [20 21 22 23 24 25 26 27 28 29]
 [30 31 32 33 34 35 36 37 38 39]
 [40 41 42 43 44 45 46 47 48 49]]
>>>
```

```python
import numpy as np

arr = np.arange(50).reshape(5,10)
print(arr)
print(' ')
a = arr[1:3]
print(a)

>>>
[[ 0  1  2  3  4  5  6  7  8  9]
 [10 11 12 13 14 15 16 17 18 19]
 [20 21 22 23 24 25 26 27 28 29]
 [30 31 32 33 34 35 36 37 38 39]
 [40 41 42 43 44 45 46 47 48 49]]
 
[[10 11 12 13 14 15 16 17 18 19]
 [20 21 22 23 24 25 26 27 28 29]]
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='npyarrind'>Numpy array indexing</h4>

```python
import numpy as np

arr = np.arange(0,11)
a1 = arr[8]
a2 = arr[1:4]

print(arr)
print(a1)
print(a2)

arr[0:5] = 100

print(arr)

>>>
[ 0  1  2  3  4  5  6  7  8  9 10]
8
[1 2 3]
[100 100 100 100 100   5   6   7   8   9  10]
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='npysliceofarr'>Numpy slice of array</h4>

```python
import numpy as np

arr = np.arange(0,11)

slice_of_arr = arr[0:6]

print(slice_of_arr)

slice_of_arr[:] = 99

print(slice_of_arr)
print(arr)

>>>
[0 1 2 3 4 5]
[99 99 99 99 99 99]
[99 99 99 99 99 99  6  7  8  9 10]
>>>
```

```python
import numpy as np

arr = np.arange(0,11)
myins = int(input('add number: '))

slice_of_arr = arr[0:6]
arr[9] = myins

print(slice_of_arr)

slice_of_arr[:] = 99

print(slice_of_arr)
print(myins)
print(arr)

>>>
add number: 222
[0 1 2 3 4 5]
[99 99 99 99 99 99]
222
[ 99  99  99  99  99  99   6   7   8 222  10]
>>>
```

```python
import numpy as np

arr = np.arange(0,11)

print(arr)

arr_copy = arr.copy()

print(arr_copy)

arr_copy[:] = 100

print(arr_copy)

>>>
[ 0  1  2  3  4  5  6  7  8  9 10]
[ 0  1  2  3  4  5  6  7  8  9 10]
[100 100 100 100 100 100 100 100 100 100 100]
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='npyarrind'>Numpy array indexing</h4>

```python
import numpy as np

arr = np.array([[5,10,15],[20,25,30],[35,40,45]])

print(arr)
print(arr[0])

>>>
[[ 5 10 15]
 [20 25 30]
 [35 40 45]]
[ 5 10 15]
>>>
```

```python
import numpy as np

arr = np.array([[5,10,15],[20,25,30],[35,40,45]])

print(arr)
print(arr[0])
print(arr[0][2])
print(arr[0,2])

>>>
[[ 5 10 15]
 [20 25 30]
 [35 40 45]]
[ 5 10 15]
15
15
>>>
```

```python
import numpy as np

arr = np.array([[5,10,15],[20,25,30],[35,40,45]])

print(' ')
print('array')
print(arr)

print(' ')
print(':1')
print(arr[:1])

print(' ')
print(':2')
print(arr[:2])

print(' ')
print('1:')
print(arr[1:])

print(' ')
print('2:')
print(arr[2:])

print(' ')
print(':1,1:')
print(arr[:1,1:])

print(' ')
print(':2,1:')
print(arr[:2,1:])

print(' ')
print(':1,2:')
print(arr[:1,2:])

print(' ')
print(':2,2:')
print(arr[:2,2:])

>>>
array
[[ 5 10 15]
 [20 25 30]
 [35 40 45]]
 
:1
[[ 5 10 15]]
 
:2
[[ 5 10 15]
 [20 25 30]]
 
1:
[[20 25 30]
 [35 40 45]]
 
2:
[[35 40 45]]
 
:1,1:
[[10 15]]
 
:2,1:
[[10 15]
 [25 30]]
 
:1,2:
[[15]]
 
:2,2:
[[15]
 [30]]
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='npyops'>Numpy Operations</h4>

```python
import numpy as np

arr = np.arange(0,11)
a = arr+arr
b = arr-arr
c = arr*arr
d = arr + 100
e = arr ** 3

print(arr)
print(a)
print(b)
print(c)
print(d)
print(e)

>>>
[ 0  1  2  3  4  5  6  7  8  9 10]
[ 0  2  4  6  8 10 12 14 16 18 20]
[0 0 0 0 0 0 0 0 0 0 0]
[  0   1   4   9  16  25  36  49  64  81 100]
[100 101 102 103 104 105 106 107 108 109 110]
[   0    1    8   27   64  125  216  343  512  729 1000]
>>>
```

```python
import numpy as np

arr = np.arange(0,11)
np1 = np.sqrt(arr)
np2 = np.sin(arr)

print(np1)
print('')
print(np2)

>>>
[0.         1.         1.41421356 1.73205081 2.         2.23606798
 2.44948974 2.64575131 2.82842712 3.         3.16227766]

[ 0.          0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427
 -0.2794155   0.6569866   0.98935825  0.41211849 -0.54402111]
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---
