```python
'''
lotto most drawn numbers
'''

import openpyxl
import pickle

from collections import Counter
from collections import OrderedDict
from openpyxl import load_workbook

#source file
wb = load_workbook(filename = 'C:path/path.xlsx')
sheet_ranges = wb['Sheet1']

#last 5 numbers from the source
a10, b10, c10, d10, e10 = sheet_ranges['A10'].value, sheet_ranges['B10'].value, sheet_ranges['C10'].value, sheet_ranges['D10'].value, sheet_ranges['E10'].value  
a9, b9, c9, d9, e9 = sheet_ranges['A9'].value, sheet_ranges['B9'].value, sheet_ranges['C9'].value, sheet_ranges['D9'].value, sheet_ranges['E9'].value  
a8, b8, c8, d8, e8 = sheet_ranges['A8'].value, sheet_ranges['B8'].value, sheet_ranges['C8'].value, sheet_ranges['D8'].value, sheet_ranges['E8'].value  
a7, b7, c7, d7, e7 = sheet_ranges['A7'].value, sheet_ranges['B7'].value, sheet_ranges['C7'].value, sheet_ranges['D7'].value, sheet_ranges['E7'].value  
a6, b6, c6, d6, e6 = sheet_ranges['A6'].value, sheet_ranges['B6'].value, sheet_ranges['C6'].value, sheet_ranges['D6'].value, sheet_ranges['E6'].value  
a5, b5, c5, d5, e5 = sheet_ranges['A5'].value, sheet_ranges['B5'].value, sheet_ranges['C5'].value, sheet_ranges['D5'].value, sheet_ranges['E5'].value  
a4, b4, c4, d4, e4 = sheet_ranges['A4'].value, sheet_ranges['B4'].value, sheet_ranges['C4'].value, sheet_ranges['D4'].value, sheet_ranges['E4'].value  
a3, b3, c3, d3, e3 = sheet_ranges['A3'].value, sheet_ranges['B3'].value, sheet_ranges['C3'].value, sheet_ranges['D3'].value, sheet_ranges['E3'].value  
a2, b2, c2, d2, e2 = sheet_ranges['A2'].value, sheet_ranges['B2'].value, sheet_ranges['C2'].value, sheet_ranges['D2'].value, sheet_ranges['E2'].value
a1, b1, c1, d1, e1 = sheet_ranges['A1'].value, sheet_ranges['B1'].value, sheet_ranges['C1'].value, sheet_ranges['D1'].value, sheet_ranges['E1'].value

#last 2 numbers from the source
g10, h10 = sheet_ranges['G10'].value, sheet_ranges['H10'].value
g9, h9 = sheet_ranges['G9'].value, sheet_ranges['H9'].value
g8, h8 = sheet_ranges['G8'].value, sheet_ranges['H8'].value
g7, h7 = sheet_ranges['G7'].value, sheet_ranges['H7'].value
g6, h6 = sheet_ranges['G6'].value, sheet_ranges['H6'].value
g5, h5 = sheet_ranges['G5'].value, sheet_ranges['H5'].value
g4, h4 = sheet_ranges['G4'].value, sheet_ranges['H4'].value
g3, h3 = sheet_ranges['G3'].value, sheet_ranges['H3'].value
g2, h2 = sheet_ranges['G2'].value, sheet_ranges['H2'].value
g1, h1 = sheet_ranges['G1'].value, sheet_ranges['H1'].value

#creating lists from the source
l1 = [a1, b1, c1, d1, e1, a2, b2, c2, d2, e2, a3, b3, c3, d3, e3, a4, b4, c4, d4, e4, a5, b5, c5, d5, e5,
      a6, b6, c6, d6, e6, a7, b7, c7, d7, e7, a8, b8, c8, d8, e8, a9, b9, c9, d9, e9, a10, b10, c10, d10, e10]

l2 = [g1, h1, g2, h2, g3, h3, g4, h4, g5, h5,
      g6, h6, g7, h7, g8, h8, g9, h9, g10, h10]

#count occurencies in the dictionary
d1 = Counter(l1)
d2 = Counter(l2)

#sort the dictionary values - desc
dd1 = OrderedDict(sorted(d1.items(), key=lambda t: t[1], reverse=True))
dd2 = OrderedDict(sorted(d2.items(), key=lambda t: t[1], reverse=True))

#print out the results line by line
for key in dd1:
    print('5: ', key, dd1[key])

print(' ')

for key in dd2:
    print('2: ', key, dd2[key])
```


