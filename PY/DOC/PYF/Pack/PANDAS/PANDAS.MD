
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [Pack](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/Pack/Pack.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Packages/Modules/Files - Pandas</h3>

---

<h4 id='^^pandas'></h4>
<a href='#panseries'>Series</a><br>

---

<h4 id='panseries'>Series</h4>

```python
import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

print(labels)
print(my_data)
print(arr)
print(d)

>>>
['a', 'b', 'c']
[10, 20, 30]
[10 20 30]
{'a': 10, 'b': 20, 'c': 30}
>>>
```

```python
import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

a = pd.Series(data = my_data)

print(a)

>>>
0    10
1    20
2    30
dtype: int64
>>>
```

```python
import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

a = pd.Series(data = my_data,index=labels)

print(a)

>>>
a    10
b    20
c    30
dtype: int64
>>>
```

```python
import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

a = pd.Series(arr)

print(a)

>>>
0    10
1    20
2    30
dtype: int32
>>>
```

```python
import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

a = pd.Series(arr,labels)

print(a)

>>>
a    10
b    20
c    30
dtype: int32
>>>
```

```python
import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

a = pd.Series(d)

print(a)

>>>
a    10
b    20
c    30
dtype: int64
>>>
```

```python
import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

a = pd.Series(data=labels)

print(a)

>>>
0    a
1    b
2    c
dtype: object
>>>
```

```python
import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

a = pd.Series(data=labels)

print(a[1])

>>>
b
>>>
```

```python
import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

a = pd.Series(data=[sum,print,len])

print(a)

>>>
0      <built-in function sum>
1    <built-in function print>
2      <built-in function len>
dtype: object
>>>
```

```python
import numpy as np
import pandas as pd

ser1 = pd.Series([1,2,3,4],['usa', 'ger', 'ussr', 'jpn'])
print(ser1)

>>>
usa     1
ger     2
ussr    3
jpn     4
dtype: int64
>>>
```

```python
import numpy as np
import pandas as pd

ser1 = pd.Series([1,2,3,4],['usa', 'ger', 'ussr', 'jpn'])
ser2 = pd.Series([1,2,5,4],['usa', 'ger', 'ita', 'jpn'])

print(ser1)
print(' ')
print(ser2)

>>>
usa     1
ger     2
ussr    3
jpn     4
dtype: int64
 
usa    1
ger    2
ita    5
jpn    4
dtype: int64
>>>
```

```python
import numpy as np
import pandas as pd

ser1 = pd.Series([1,2,3,4],['usa', 'ger', 'ussr', 'jpn'])
ser2 = pd.Series([1,2,5,4],['usa', 'ger', 'ita', 'jpn'])

print(ser1['usa'])
print(ser1['ussr'])
print(ser2['ita'])

>>>
1
3
5
>>>
```

```python
import numpy as np
import pandas as pd

ser1 = pd.Series([1,2,3,4],['usa', 'ger', 'ussr', 'jpn'])
ser2 = pd.Series([1,2,5,4],['usa', 'ger', 'ita', 'jpn'])

print(ser1+ser2)

>>>
ger     4.0
ita     NaN
jpn     8.0
usa     2.0
ussr    NaN
dtype: float64
>>>
```

---
