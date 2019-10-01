
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [DS](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DataStruct/DS.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Data Structures - Nested List</h3>

---

* <a href='#neslisbasics'>Basics</a><br>

---

<h4 id='neslisbasics'>Basics</h4>

```python
def high(x):
   
    #create a list from a string
    inpL = x.split()
    
    #insert every element from list into a nested list
    i=0
    new_list=[]
    while i<len(inpL):
        new_list.append(inpL[i:i+1])
        i+=1
    print(new_list)

high('man i need a taxi up to ubud')

>>>
[['man'], ['i'], ['need'], ['a'], ['taxi'], ['up'], ['to'], ['ubud']]
>>>
```

```python
def high(x):
    
    inpL = x.split()
   
    #slice a string into a nested list
    fl=[list(i) for s in inpL for i in s.split()]
    print(fl)
    
high('man i need a taxi up to ubud')

>>>
[['m', 'a', 'n'], ['i'], ['n', 'e', 'e', 'd'], ['a'], ['t', 'a', 'x', 'i'], ['u', 'p'], ['t', 'o'], ['u', 'b', 'u', 'd']]
>>>
```

```python
def high(x):
    
    abc=st.ascii_lowercase
    
    abcL=list(abc)
    numsL=[nums for nums in range(1,27)]
    inpL = x.split()
    
    #convert two list into a dict
    dic = dict(zip(abcL,numsL))
       
    #slice a string into a nested list
    fl=[list(i) for s in inpL for i in s.split()]
    print(fl)
    
    #change the values to the numbers
    fl3=[]
    fl2=[fl3.append(dic[value]) for sub_list in fl for value in sub_list]
    print(fl3)
    
high('man i need a taxi up to ubud')

>>>
[['m', 'a', 'n'], ['i'], ['n', 'e', 'e', 'd'], ['a'], ['t', 'a', 'x', 'i'], ['u', 'p'], ['t', 'o'], ['u', 'b', 'u', 'd']]
[13, 1, 14, 9, 14, 5, 5, 4, 1, 20, 1, 24, 9, 21, 16, 20, 15, 21, 2, 21, 4]
>>>
```

---

