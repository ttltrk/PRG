
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [Pack](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/Pack/Pack.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Packages/Modules/Files - Pandas</h3>

---

<a href='#panseries'>Series</a><br>
<a href='#pandf1'>DataFrames 1</a><br>
<a href='#pandf2'>DataFrames 2</a><br>
<a href='#pandf3'>DataFrames 3</a><br>
<a href='#panmissda'>Missing Data</a><br>
<a href='#pangroup'>Groupby</a><br>
<a href='#panmejoco'>Merging Joining and Concatenating</a><br>

---

<h4 id='panseries'>Series</h4>

01

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

<a href='#^'>^^^</a>

02

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

<a href='#^'>^^^</a>

03

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

<a href='#^'>^^^</a>

04

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

<a href='#^'>^^^</a>

05

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

<a href='#^'>^^^</a>

06

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

<a href='#^'>^^^</a>

07

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

<a href='#^'>^^^</a>

08

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

<a href='#^'>^^^</a>

09

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

<a href='#^'>^^^</a>

10

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

<a href='#^'>^^^</a>

11

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

<a href='#^'>^^^</a>

12

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

<a href='#^'>^^^</a>

13

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

<a href='#^'>^^^</a>

---

<h4 id='pandf'>DataFrames</h4>

01

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
>>>
```

<a href='#^'>^^^</a>

02

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print(' ')
print(df['W'])

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
A    2.706850
B    0.651118
C   -2.018168
D    0.188695
E    0.190794
Name: W, dtype: float64
>>>
```

<a href='#^'>^^^</a>

03

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print(' ')
print(df.W)

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
A    2.706850
B    0.651118
C   -2.018168
D    0.188695
E    0.190794
Name: W, dtype: float64
>>>
```

<a href='#^'>^^^</a>

04

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print(' ')
print(df[['W','Z']])

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
          W         Z
A  2.706850  0.503826
B  0.651118  0.605965
C -2.018168 -0.589001
D  0.188695  0.955057
E  0.190794  0.683509
>>>
```

<a href='#^'>^^^</a>

05

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

df['new'] = df['W']+df['Z']

print(df)
print(' ')
print(df['new'])

>>>
          W         X         Y         Z       new
A  2.706850  0.628133  0.907969  0.503826  3.210676
B  0.651118 -0.319318 -0.848077  0.605965  1.257083
C -2.018168  0.740122  0.528813 -0.589001 -2.607169
D  0.188695 -0.758872 -0.933237  0.955057  1.143752
E  0.190794  1.978757  2.605967  0.683509  0.874303
 
A    3.210676
B    1.257083
C   -2.607169
D    1.143752
E    0.874303
Name: new, dtype: float64
>>>
```

<a href='#^'>^^^</a>

06

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

df['new'] = df['W']+df['Z']

print(df)

a = df.drop('new', axis=1)

print(' ')
print(a)

print(' ')
print(df)

b = df.drop('new', axis=1, inplace=True)

print(' ')
print(df)

>>>
          W         X         Y         Z       new
A  2.706850  0.628133  0.907969  0.503826  3.210676
B  0.651118 -0.319318 -0.848077  0.605965  1.257083
C -2.018168  0.740122  0.528813 -0.589001 -2.607169
D  0.188695 -0.758872 -0.933237  0.955057  1.143752
E  0.190794  1.978757  2.605967  0.683509  0.874303
 
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
          W         X         Y         Z       new
A  2.706850  0.628133  0.907969  0.503826  3.210676
B  0.651118 -0.319318 -0.848077  0.605965  1.257083
C -2.018168  0.740122  0.528813 -0.589001 -2.607169
D  0.188695 -0.758872 -0.933237  0.955057  1.143752
E  0.190794  1.978757  2.605967  0.683509  0.874303
 
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
>>>
```

<a href='#^'>^^^</a>

07

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df.shape)

>>>
(5,4)
>>>
```

<a href='#^'>^^^</a>

08

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print(' ')
print(df.loc['A'])

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
W    2.706850
X    0.628133
Y    0.907969
Z    0.503826
Name: A, dtype: float64
>>>
```

<a href='#^'>^^^</a>

09

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print(' ')
print(df.iloc[0])
print(' ')
print(df.iloc[2])

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
W    2.706850
X    0.628133
Y    0.907969
Z    0.503826
Name: A, dtype: float64
 
W   -2.018168
X    0.740122
Y    0.528813
Z   -0.589001
Name: C, dtype: float64
>>>
```

<a href='#^'>^^^</a>

10

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print(' ')
print(df.loc['B','Y'])

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
-0.8480769834036315
>>>
```

<a href='#^'>^^^</a>

11

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print(' ')
print(df.loc[['A','B'],['W','Y']])

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
          W         Y
A  2.706850  0.907969
B  0.651118 -0.848077
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='pandf2'>DataFrames 2</h4>


```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print(' ')
print(df > 0)

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
       W      X      Y      Z
A   True   True   True   True
B   True  False  False   True
C  False   True   True  False
D   True  False  False   True
E   True   True   True   True
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

booldf = df > 0

print(df)
print(' ')
print(df[booldf])

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118       NaN       NaN  0.605965
C       NaN  0.740122  0.528813       NaN
D  0.188695       NaN       NaN  0.955057
E  0.190794  1.978757  2.605967  0.683509
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print(' ')
print(df[df>0])

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118       NaN       NaN  0.605965
C       NaN  0.740122  0.528813       NaN
D  0.188695       NaN       NaN  0.955057
E  0.190794  1.978757  2.605967  0.683509
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print(' ')
print(df['W'])
print(' ')
print(df['W']>0)

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
A    2.706850
B    0.651118
C   -2.018168
D    0.188695
E    0.190794
Name: W, dtype: float64
 
A     True
B     True
C    False
D     True
E     True
Name: W, dtype: bool
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print(' ')
print(df[df['W']>0])

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print(' ')
print(df[df['Z']<0])

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
          W         X         Y         Z
C -2.018168  0.740122  0.528813 -0.589001
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

resultdf = df[df['W']>0]

print(df)
print(' ')
print(resultdf)
print(' ')
print(resultdf['X'])

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
A    0.628133
B   -0.319318
D   -0.758872
E    1.978757
Name: X, dtype: float64
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print(' ')
print(df[df['W']>0])
print(' ')
print(df[df['W']>0]['X'])

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
A    0.628133
B   -0.319318
D   -0.758872
E    1.978757
Name: X, dtype: float64
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print(' ')
print(df[df['W']>0])
print(' ')
print(df[(df['W']>0) & (df['W']>1)])

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
         W         X         Y         Z
A  2.70685  0.628133  0.907969  0.503826
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print(' ')
print(df.reset_index())

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
 
  index         W         X         Y         Z
0     A  2.706850  0.628133  0.907969  0.503826
1     B  0.651118 -0.319318 -0.848077  0.605965
2     C -2.018168  0.740122  0.528813 -0.589001
3     D  0.188695 -0.758872 -0.933237  0.955057
4     E  0.190794  1.978757  2.605967  0.683509
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

newind = 'CA NY WY OR CO'.split()
df['States'] = newind

print(newind)
print(' ')
print(df)

>>>
['CA', 'NY', 'WY', 'OR', 'CO']
 
          W         X         Y         Z States
A  2.706850  0.628133  0.907969  0.503826     CA
B  0.651118 -0.319318 -0.848077  0.605965     NY
C -2.018168  0.740122  0.528813 -0.589001     WY
D  0.188695 -0.758872 -0.933237  0.955057     OR
E  0.190794  1.978757  2.605967  0.683509     CO
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
l = [1, 2, 3, 4]

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

newind = 'CA NY WY OR CO'.split()
df['States'] = newind

print(df)
print(' ')
print(df.set_index('States'))

>>>
          W         X         Y         Z States
A  2.706850  0.628133  0.907969  0.503826     CA
B  0.651118 -0.319318 -0.848077  0.605965     NY
C -2.018168  0.740122  0.528813 -0.589001     WY
D  0.188695 -0.758872 -0.933237  0.955057     OR
E  0.190794  1.978757  2.605967  0.683509     CO
 
               W         X         Y         Z
States                                        
CA      2.706850  0.628133  0.907969  0.503826
NY      0.651118 -0.319318 -0.848077  0.605965
WY     -2.018168  0.740122  0.528813 -0.589001
OR      0.188695 -0.758872 -0.933237  0.955057
CO      0.190794  1.978757  2.605967  0.683509
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='pandf3'>DataFrames 3</h4>

```python
import numpy as np
import pandas as pd

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))

print(outside)
print(' ')
print(inside)
print(' ')
print(hier_index)
print(' ')
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

>>>
['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
 
[1, 2, 3, 1, 2, 3]
 
[('G1', 1), ('G1', 2), ('G1', 3), ('G2', 1), ('G2', 2), ('G2', 3)]
 
MultiIndex(levels=[['G1', 'G2'], [1, 2, 3]],
           labels=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn


outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))

hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])

print(df)

>>>
             A         B
G1 1  1.280937 -0.236612
   2  0.372966  1.201955
   3  0.449831  0.219009
G2 1 -0.171675 -1.316123
   2  0.845793  0.285667
   3  1.206388  0.854464
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn


outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))

hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])

print(df)
print(' ')
print(df.loc['G1'])

>>>
             A         B
G1 1 -0.426018  0.601013
   2  0.283416 -0.852927
   3  0.005474  0.994846
G2 1  0.085804  0.562624
   2 -0.351142  1.856567
   3  1.360953  0.200511
 
          A         B
1 -0.426018  0.601013
2  0.283416 -0.852927
3  0.005474  0.994846
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn


outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))

hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])

print(df)
print(' ')
print(df.loc['G1'])
print(' ')
print(df.loc['G1'].loc[1])

>>>
             A         B
G1 1  0.157766 -1.808455
   2  0.724344 -2.247547
   3  1.952164  0.785557
G2 1 -0.604003  0.004664
   2 -1.771062  1.327195
   3 -0.902754 -1.506650
 
          A         B
1  0.157766 -1.808455
2  0.724344 -2.247547
3  1.952164  0.785557
 
A    0.157766
B   -1.808455
Name: 1, dtype: float64
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn


outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))

hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])

print(df)
print(' ')

df.index.names = ['Groups','Num']
print(df)

>>>
             A         B
G1 1 -1.725999 -1.690544
   2  0.792964  1.390087
   3  1.188152  1.368345
G2 1  0.983025 -2.201848
   2  1.011586  0.602077
   3 -0.146601 -0.581571
 
                   A         B
Groups Num                    
G1     1   -1.725999 -1.690544
       2    0.792964  1.390087
       3    1.188152  1.368345
G2     1    0.983025 -2.201848
       2    1.011586  0.602077
       3   -0.146601 -0.581571
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))

hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
df.index.names = ['Groups','Num']

print(df)
print(' ')
print(df.loc['G2'])
print(' ')
print(df.loc['G2'].loc[2])
print(' ')
print(df.loc['G2'].loc[2]['B'])

>>>
                   A         B
Groups Num                    
G1     1    1.133368  2.463548
       2    0.913694 -0.543514
       3   -1.990372 -0.156860
G2     1   -0.711758 -0.037313
       2   -1.313573  0.507473
       3   -0.340687 -0.656961
 
            A         B
Num                    
1   -0.711758 -0.037313
2   -1.313573  0.507473
3   -0.340687 -0.656961
 
A   -1.313573
B    0.507473
Name: 2, dtype: float64
 
0.5074734431695828
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))

hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
df.index.names = ['Groups','Num']

print(df)
print(' ')
print(df.xs(1,level='Num'))

>>>
                   A         B
Groups Num                    
G1     1    0.311833 -1.176028
       2   -0.136651 -0.191222
       3   -0.404261  0.579887
G2     1   -1.564641  1.009269
       2   -0.410623 -1.718002
       3    0.431931  1.650564
 
               A         B
Groups                    
G1      0.311833 -1.176028
G2     -1.564641  1.009269
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='panmissda'>Missing Data</h4>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)

print(d)
print(' ')
print(df)

>>>
{'A': [1, 2, nan], 'B': [5, nan, nan], 'C': [1, 2, 3]}
 
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
2  NaN  NaN  3
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

c1 = [1,2,3]
c2 = [4,5,6]
c3 = [7,8,9]

c = {'A':c1, 'B':c2, 'C':c3}
df = pd.DataFrame(c)

print(c)
print(' ')
print(df)

>>>
{'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
 
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

x = np.nan

c1 = [1,2,3,4,5]
c2 = [10,11,12,x,x]
c3 = [20,21,22,23,x]

c = {'C1':c1, 'C2':c2, 'C3':c3}
df = pd.DataFrame(c)

print(c)
print(' ')
print(df)

>>>
{'C1': [1, 2, 3, 4, 5], 'C2': [10, 11, 12, nan, nan], 'C3': [20, 21, 22, 23, nan]}
 
   C1    C2    C3
0   1  10.0  20.0
1   2  11.0  21.0
2   3  12.0  22.0
3   4   NaN  23.0
4   5   NaN   NaN
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)

print(d)
print(' ')
print(df)
print(' ')
print(df.dropna())

>>>
{'A': [1, 2, nan], 'B': [5, nan, nan], 'C': [1, 2, 3]}
 
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
2  NaN  NaN  3
 
     A    B  C
0  1.0  5.0  1
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)

print(d)
print(' ')
print(df)
print(' ')
print(df.dropna(axis=1))

>>>
{'A': [1, 2, nan], 'B': [5, nan, nan], 'C': [1, 2, 3]}
 
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
2  NaN  NaN  3
 
   C
0  1
1  2
2  3
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)

print(d)
print(' ')
print(df)
print(' ')
print(df.dropna(thresh=2))

>>>
{'A': [1, 2, nan], 'B': [5, nan, nan], 'C': [1, 2, 3]}
 
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
2  NaN  NaN  3
 
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)

print(d)
print(' ')
print(df)
print(' ')
print(df.fillna(value='FILL VALUE'))

>>>
{'A': [1, 2, nan], 'B': [5, nan, nan], 'C': [1, 2, 3]}
 
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
2  NaN  NaN  3
 
            A           B  C
0           1           5  1
1           2  FILL VALUE  2
2  FILL VALUE  FILL VALUE  3
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd
from numpy.random import randn

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)

print(d)
print(' ')
print(df)
print(' ')
print(df['A'].fillna(value=df['A'].mean()))

>>>
{'A': [1, 2, nan], 'B': [5, nan, nan], 'C': [1, 2, 3]}
 
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
2  NaN  NaN  3
 
0    1.0
1    2.0
2    1.5
Name: A, dtype: float64
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='pangroup'>Groupby</h4>

```python
import numpy as np
import pandas as pd


data = {'Company':['GOOG','GOOG','MSFT','MSFT', 'FB', 'FB'],
        'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales':[200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

print(df)

>>>
  Company   Person  Sales
0    GOOG      Sam    200
1    GOOG  Charlie    120
2    MSFT      Amy    340
3    MSFT  Vanessa    124
4      FB     Carl    243
5      FB    Sarah    350
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd


data = {'Company':['GOOG','GOOG','MSFT','MSFT', 'FB', 'FB'],
        'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales':[200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)
byComp = df.groupby('Company')

print(df)
print(' ')
print(byComp.mean())

>>>
  Company   Person  Sales
0    GOOG      Sam    200
1    GOOG  Charlie    120
2    MSFT      Amy    340
3    MSFT  Vanessa    124
4      FB     Carl    243
5      FB    Sarah    350
 
         Sales
Company       
FB       296.5
GOOG     160.0
MSFT     232.0
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd


data = {'Company':['GOOG','GOOG','MSFT','MSFT', 'FB', 'FB'],
        'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales':[200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

byComp = df.groupby('Company')

print(df)
print(' ')
print(byComp.mean())
print(' ')
print(byComp.sum())
print(' ')
print(byComp.std())

>>>
  Company   Person  Sales
0    GOOG      Sam    200
1    GOOG  Charlie    120
2    MSFT      Amy    340
3    MSFT  Vanessa    124
4      FB     Carl    243
5      FB    Sarah    350
 
         Sales
Company       
FB       296.5
GOOG     160.0
MSFT     232.0
 
         Sales
Company       
FB         593
GOOG       320
MSFT       464
 
              Sales
Company            
FB        75.660426
GOOG      56.568542
MSFT     152.735065
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd


data = {'Company':['GOOG','GOOG','MSFT','MSFT', 'FB', 'FB'],
        'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales':[200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

byComp = df.groupby('Company')

print(df)
print(' ')
print(byComp.sum().loc['FB'])

>>>
  Company   Person  Sales
0    GOOG      Sam    200
1    GOOG  Charlie    120
2    MSFT      Amy    340
3    MSFT  Vanessa    124
4      FB     Carl    243
5      FB    Sarah    350
 
Sales    593
Name: FB, dtype: int64
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd


data = {'Company':['GOOG','GOOG','MSFT','MSFT', 'FB', 'FB'],
        'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales':[200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

byComp = df.groupby('Company')

print(df)
print(' ')
print(byComp.count())

>>>
  Company   Person  Sales
0    GOOG      Sam    200
1    GOOG  Charlie    120
2    MSFT      Amy    340
3    MSFT  Vanessa    124
4      FB     Carl    243
5      FB    Sarah    350
 
         Person  Sales
Company               
FB            2      2
GOOG          2      2
MSFT          2      2
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd


data = {'Company':['GOOG','GOOG','MSFT','MSFT', 'FB', 'FB'],
        'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales':[200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

byComp = df.groupby('Company')

print(df)
print(' ')
print(byComp.max())
print(' ')
print(byComp.min())

>>>
  Company   Person  Sales
0    GOOG      Sam    200
1    GOOG  Charlie    120
2    MSFT      Amy    340
3    MSFT  Vanessa    124
4      FB     Carl    243
5      FB    Sarah    350
 
          Person  Sales
Company                
FB         Sarah    350
GOOG         Sam    200
MSFT     Vanessa    340
 
          Person  Sales
Company                
FB          Carl    243
GOOG     Charlie    120
MSFT         Amy    124
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd


data = {'Company':['GOOG','GOOG','MSFT','MSFT', 'FB', 'FB'],
        'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales':[200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

byComp = df.groupby('Company')

print(df)
print(' ')
print(byComp.describe())

>>>
  Company   Person  Sales
0    GOOG      Sam    200
1    GOOG  Charlie    120
2    MSFT      Amy    340
3    MSFT  Vanessa    124
4      FB     Carl    243
5      FB    Sarah    350
 
        Sales                                                        
        count   mean         std    min     25%    50%     75%    max
Company                                                              
FB        2.0  296.5   75.660426  243.0  269.75  296.5  323.25  350.0
GOOG      2.0  160.0   56.568542  120.0  140.00  160.0  180.00  200.0
MSFT      2.0  232.0  152.735065  124.0  178.00  232.0  286.00  340.0
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd


data = {'Company':['GOOG','GOOG','MSFT','MSFT', 'FB', 'FB'],
        'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales':[200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

byComp = df.groupby('Company')

print(df)
print(' ')
print(byComp.describe().transpose())
print(' ')
print(byComp.describe().transpose()['FB'])

>>>
  Company   Person  Sales
0    GOOG      Sam    200
1    GOOG  Charlie    120
2    MSFT      Amy    340
3    MSFT  Vanessa    124
4      FB     Carl    243
5      FB    Sarah    350
 
Company              FB        GOOG        MSFT
Sales count    2.000000    2.000000    2.000000
      mean   296.500000  160.000000  232.000000
      std     75.660426   56.568542  152.735065
      min    243.000000  120.000000  124.000000
      25%    269.750000  140.000000  178.000000
      50%    296.500000  160.000000  232.000000
      75%    323.250000  180.000000  286.000000
      max    350.000000  200.000000  340.000000
 
Sales  count      2.000000
       mean     296.500000
       std       75.660426
       min      243.000000
       25%      269.750000
       50%      296.500000
       75%      323.250000
       max      350.000000
Name: FB, dtype: float64
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='panmejoco'>Merging Joining and Concatenating</h4>

```python
import numpy as np
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0,1,2,3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4,5,6,7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8,9,10,11])

print(df1)
print(' ')
print(df2)
print(' ')
print(df3)


>>>
    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
 
    A   B   C   D
4  A4  B4  C4  D4
5  A5  B5  C5  D5
6  A6  B6  C6  D6
7  A7  B7  C7  D7
 
      A    B    C    D
8    A8   B8   C8   D8
9    A9   B9   C9   D9
10  A10  B10  C10  D10
11  A11  B11  C11  D11
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0,1,2,3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4,5,6,7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8,9,10,11])

print(pd.concat([df1, df2, df3]))

>>>
      A    B    C    D
0    A0   B0   C0   D0
1    A1   B1   C1   D1
2    A2   B2   C2   D2
3    A3   B3   C3   D3
4    A4   B4   C4   D4
5    A5   B5   C5   D5
6    A6   B6   C6   D6
7    A7   B7   C7   D7
8    A8   B8   C8   D8
9    A9   B9   C9   D9
10  A10  B10  C10  D10
11  A11  B11  C11  D11
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0,1,2,3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4,5,6,7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8,9,10,11])

print(pd.concat([df1, df2, df3]))
print(' ')
print(pd.concat([df1, df2, df3], axis=1))

>>>
      A    B    C    D
0    A0   B0   C0   D0
1    A1   B1   C1   D1
2    A2   B2   C2   D2
3    A3   B3   C3   D3
4    A4   B4   C4   D4
5    A5   B5   C5   D5
6    A6   B6   C6   D6
7    A7   B7   C7   D7
8    A8   B8   C8   D8
9    A9   B9   C9   D9
10  A10  B10  C10  D10
11  A11  B11  C11  D11
 
      A    B    C    D    A    B    C    D    A    B    C    D
0    A0   B0   C0   D0  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
1    A1   B1   C1   D1  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
2    A2   B2   C2   D2  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
3    A3   B3   C3   D3  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
4   NaN  NaN  NaN  NaN   A4   B4   C4   D4  NaN  NaN  NaN  NaN
5   NaN  NaN  NaN  NaN   A5   B5   C5   D5  NaN  NaN  NaN  NaN
6   NaN  NaN  NaN  NaN   A6   B6   C6   D6  NaN  NaN  NaN  NaN
7   NaN  NaN  NaN  NaN   A7   B7   C7   D7  NaN  NaN  NaN  NaN
8   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   A8   B8   C8   D8
9   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   A9   B9   C9   D9
10  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  A10  B10  C10  D10
11  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  A11  B11  C11  D11

Process finished with exit code 0
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})

print(left)
print(' ')
print(right)

>>>
  key   A   B
0  K0  A0  B0
1  K1  A1  B1
2  K2  A2  B2
3  K3  A3  B3
 
  key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left,right,how='inner', on='key'))

>>>
  key   A   B   C   D
0  K0  A0  B0  C0  D0
1  K1  A1  B1  C1  D1
2  K2  A2  B2  C2  D2
3  K3  A3  B3  C3  D3
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K2', 'K3'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2':['K0', 'K0', 'K0', 'K0'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left,right,on=['key1', 'key2']))

>>>
  key1 key2   A   B   C   D
0   K0   K0  A0  B0  C0  D0
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K2', 'K3'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2':['K0', 'K0', 'K0', 'K0'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left,right, how='outer', on=['key1', 'key2']))

>>>
  key1 key2    A    B    C    D
0   K0   K0   A0   B0   C0   D0
1   K0   K1   A1   B1  NaN  NaN
2   K1   K2   A2   B2  NaN  NaN
3   K2   K3   A3   B3  NaN  NaN
4   K1   K0  NaN  NaN   C1   D1
5   K1   K0  NaN  NaN   C2   D2
6   K2   K0  NaN  NaN   C3   D3
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K2', 'K3'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2':['K0', 'K0', 'K0', 'K0'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left,right, how='right', on=['key1', 'key2']))

>>>
  key1 key2    A    B   C   D
0   K0   K0   A0   B0  C0  D0
1   K1   K0  NaN  NaN  C1  D1
2   K1   K0  NaN  NaN  C2  D2
3   K2   K0  NaN  NaN  C3  D3
>>>
```

<a href='#^'>^^^</a>

```python
import numpy as np
import pandas as pd

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                      'D': ['D0', 'D1', 'D2']},
                       index=['K0', 'K1', 'K2'])

print(left.join(right))

>>>
     A   B   C   D
K0  A0  B0  C0  D0
K1  A1  B1  C1  D1
K2  A2  B2  C2  D2
>>>
```

<a href='#^'>^^^</a>


