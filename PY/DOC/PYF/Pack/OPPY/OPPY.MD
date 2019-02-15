
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [Pack](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/Pack/Pack.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Packages/Modules/Files - OpenPyxl</h3>

---

<a href='#oplocfil'>Locate a file</a><br>
<a href='#oploadworkb'>Load workbook</a><br>
<a href='#opcrereftshe'>Creating reference to sheet</a><br>
<a href='#'>Creating and deleting sheet in workbook</a><br>
<a href='#'>Read and write data at cell level</a><br>
<a href='#'>Reading a row from excel sheet</a><br>
<a href='#'>Write a row to excel sheet</a><br>
<a href='#'>Read and write column</a><br>
<a href='#'>Copying sheet</a><br>
<a href='#'>Create a new folder</a><br>
<a href='#'>Copy excel files</a><br>
<a href='#'>Moving excel files</a><br>
<a href='#'>Deleting excel files</a><br>
<a href='#'>Finding files</a><br>

<a href='#^'>^^^</a>

---

<h4 id='oplocfil'>Locate a file</h4>

```python
import openpyxl
import os

print(os.getcwd())

>>>
C:\path\path
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='oploadworkb'>Load workbook</h4>

```python
import openpyxl
import os

path='C:/path/path/op_test.xlsx'
wb = openpyxl.load_workbook('op_test.xlsx')
print(type(wb))
print(path)

>>>
<class 'openpyxl.workbook.workbook.Workbook'>
C:/path/path/op_test.xlsx
>>>
```

```python
import openpyxl
import os

wb=openpyxl.load_workbook('C:/path/path/op_test.xlsx')

print(wb.sheetnames)

>>>
['employee_data', 'Sheet1', 'Sheet2']
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='opcrereftshe'>Creating reference to sheet</h4>

```python
import openpyxl
import os

wb=openpyxl.load_workbook('C:/path/path/op_test.xlsx')
wb.sheetnames
sheet = wb['employee_data']

print(sheet.title)

>>>
employee_data
>>>
```

```python
import openpyxl
import os

wb=openpyxl.load_workbook('C:/path/path/op_test.xlsx')
wb.sheetnames
sheet = wb['employee_data']

print('title of the table: ', sheet.title)
print('max row: ', sheet.max_row)
print('max column: ', sheet.max_column)

>>>
title of the table:  employee_data
max row:  6
max column:  4
>>>
```

```python
import openpyxl
import os

wb=openpyxl.load_workbook('C:/path/path/op_test.xlsx')
wb.sheetnames
sheet = wb['employee_data']
sheet.title='NewTitle'
wb.save('C:/path/path/op_test.xlsx')

print('title of the table: ', sheet.title)
print('max row: ', sheet.max_row)
print('max column: ', sheet.max_column)

>>>
title of the table:  NewTitle
max row:  6
max column:  4
>>>
```

<a href='#^'>^^^</a>

---
