

---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

### Python - OS part

```python
import os

#-----------------------------------------------------------------------------
# print working dir

print(os.getcwd()) 

#-----------------------------------------------------------------------------
# change the working dir

os.chdir('C:\\Users\\bla\\Desktop\\bla\\bla\\PY')

#-----------------------------------------------------------------------------
# list out the actual folder

print('print working dir: ',os.getcwd())
py_dir = os.listdir()
print('files / dirs in the actual dir: ',py_dir)
print('3rd file from the dir: ',py_dir[2])

#-----------------------------------------------------------------------------
# create new dir in the actual dir

os.mkdir('A1')
```
