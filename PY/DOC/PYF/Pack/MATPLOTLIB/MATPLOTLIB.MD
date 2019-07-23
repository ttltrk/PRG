
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [Pack](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/Pack/Pack.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Packages/Modules/Files - Matplotlib</h3>

---

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

print(x)
print(y)

plt.plot(x,y, 'r-')
print(plt.show())
```

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

print(x)
print(y)

plt.plot(x,y, 'r-')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
print(plt.show())
```

<a href='#^'>^^^</a>

---

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

plt.subplot(1,2,1)
plt.plot(x,y, 'r-')

plt.subplot(1,2,2)
plt.plot(y,x, 'b-')

print(plt.show())
```

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set Title')

print(plt.show())
```

<a href='#^'>^^^</a>
