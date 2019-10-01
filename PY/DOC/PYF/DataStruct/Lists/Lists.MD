
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [DS](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DataStruct/DS.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Data Structures - List</h3>

---

* <a href='#listtostr'>list to string</a><br>
* <a href='#listtotup'>list to tuple</a><br>
* <a href='#listtodict'>list to dictionary</a><br>
* <a href='#listtoset'>list to set</a><br>
* <a href='#strtoint'>string to int in list</a><br>
* <a href='#strint'>string list to int list</a><br>

---

* <a href='#remsecel'>remove every second element from the list</a><br>
* <a href='#sumlists'>sum of two lists</a><br>
* <a href='#maxnum'>find the max number in the list</a><br>
* <a href='#mintomax'>sort from the min to max</a><br>
* <a href='#negpos'>negative to positive</a><br>
* <a href='#sub'>Remove all the elements that occur in one list from another</a><br>
* <a href='#multele'>multiply elements</a><br>
* <a href='#avglist'>average of the list</a><br>
* <a href='#dedelem'>change dedicated elements in the list</a><br>
* <a href='#sortval'>sort the values</a><br>
* <a href='#findunique'>find unique numbers</a><br>
* <a href='#diff2arr'>differences between two arrays</a><br>
* <a href='#shortword'>shortest word in the list</a><br>
* <a href='#sumodd'>Sum of odd numbers</a><br>
* <a href='#findoddint'>find the larger odd integer or number</a><br>
* <a href='#findoccur'>find the occurencies in the list</a><br>
* <a href='#findmax'>find the max value in the list</a><br>
* <a href='#findevenocc'>find the even occuranves in in the list</a><br>


---

<h4 id='listtostr'>list to string</h4>

```python
list1 = ['1', '2', '3']
str1 = ''.join(list1)
str2 = ' '.join(list1)
str3 = '-'.join(list1)
str4 = 'x'.join(list1)

print(str1)
print(str2)
print(str3)
print(str4)

>>>
123
1 2 3
1-2-3
1x2x3
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='listtotup'>list to tuple</h4>

```python
l = [4,5,6]
t = tuple(l)

print(l)
print(t)

>>>
[4, 5, 6]
(4, 5, 6)
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='listtodict'>list to dictionary</h4>

```python
l = ['bi','double','duo','two']

d = dict((k,2) for k in l)

print(d)

>>>
{'bi': 2, 'double': 2, 'duo': 2, 'two': 2}
>>>
```

two lists into a dict

```python
#create two lists
abcL=list(st.ascii_lowercase)
numsL=[nums for nums in range(1,27)]
    
#convert two list into a dict
dic = dict(zip(abcL,numsL))
    
print(dic)
>>>
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='listtoset'>list to set</h4>

```python
l1 = ['bi','double','duo','two']
l2 = [1, 2, 3, 4, 5]

s1 = set(l1)
s2 = set(l2)

print(s1)
print(s2)

>>>
{'two', 'bi', 'double', 'duo'}
{1, 2, 3, 4, 5}
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='strtoint'>string to int in list</h4>

```python

def sum_mix(arr):

    #convert all the string into the int
    l = [int(i) for i in arr]

    ll = sum(l)
    return ll

print(sum_mix([8, 0, 0, '8', 15, 7, 2, 3, '7', 8, '6', 7]))

>>>
71
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='remsecel'>remove every second element from the list</h4>

```python
del mylist[1::2]
```

<a href='#^'>^^^</a>

---

<h4 id='sumlists'>sum of two lists</h4>

```python
sumOfTheList = firstList + secList
```

<a href='#^'>^^^</a>

---

<h4 id='maxnum'>find the max number in the list</h4>

```python
highest = max(arr)
```

<a href='#^'>^^^</a>

---

<h4 id='mintomax'>sort from the min to max</h4>

```python
l.sort()
```

<a href='#^'>^^^</a>

---

<h4 id='negpos'>negative to positive</h4>

```python
def invert(lst):
    lst[:] = [-1 * x for x in lst]
    return lst

print(invert([1,-2,3,-4,5]))

>>>
[-1, 2, -3, 4, -5]
>>>

```

<a href='#^'>^^^</a>

---

<h4 id='sub'>Remove all the elements that occur in one list from another</h4>

```python
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    res = [x for x in birds if x not in geese]
    return res


print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))

>>>
['Mallard', 'Hook Bill', 'Crested', 'Blue Swedish']
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='strint'>string list to int list</h4>

```python
def scoreboard(string):

    l = ['nil', 'one', 'two', 'three', 'four']
    #print(l)

    #convert string to list
    z = string.split()
    #print(z)

    #find the matches in two diff lists
    a = [x for x in z if x in l]
    #print(a)

    #change the elements in the list
    for n, i in enumerate(a):
        if i == 'nil':
            a[n] = 0
        elif i == 'one':
            a[n] = 1
        elif i == 'two':
            a[n] = 2
        elif i == 'three':
            a[n] = 3
        elif i == 'four':
            a[n] = 4
        elif i == 'five':
            a[n] = 5
        elif i == 'six':
            a[n] = 6
        elif i == 'seven':
            a[n] = 7
        elif i == 'eight':
            a[n] = 8
        elif i == 'nine':
            a[n] = 9

    if len(a) == 1:
        a.append(a[n])
        return a
    else:
        return a

print(scoreboard("The score is two nil"))

>>>
[2, 0]
>>>

```

<a href='#^'>^^^</a>

---

<h4 id='multele'>multiply elements</h4>

```python
def grow(arr):

    result = 1
    for x in arr:
         result = result * x
    return result

print(grow([1,2,3]))

>>>
6
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='avglist'>average of the list</h4>

```python
l = [1, 5, 87, 45, 8, 8]

a = int(sum(l)/len(l))
print(a)

>>>
25
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='dedelem'>change dedicated elements in the list</h4>

```python
def DNAtoRNA(dna):

    #string to list
    l = list(dna)

    #change all the Ts to U
    for n, i in enumerate(l):
        if i == 'T':
            l[n] = 'U'

    #change list to string
    str1 = ''.join(l)

    return str1


print(DNAtoRNA("TTTT"))

>>>
UUUU
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='uniqueel'>find a unique element</h4>

```python
def find_uniq(arr):
    if (arr[0] == arr[1]) or (arr[0] != arr[1] and arr[0] == arr[2]):
        repeatableNum = arr[0]
    else:
        repeatableNum = arr[1]
    for nums in arr:
        if nums != repeatableNum:
            return nums

print(find_uniq(arr = [ 3, 10, 3, 3, 3 ]))

>>>
10
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='shortword'>shortest word in the list</h4>

```python
def find_short(s):

    z = s.split()
    minimunWordLength = min([len(word) for word in z])
    return minimunWordLength

print(find_short("bitcoin take over the world maybe who knows perhaps"))

>>>
3
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='sumodd'>Sum of odd numbers</h4>

```python

def row_sum_odd_numbers(n):

    #define the size of the list to 10000
    l = list(range(10000))

    #return only the odd elements
    ll = [nums for nums in l if nums %2 == 1]

    #find the first element
    firstElement = ((n*(n-1))+1)

    #check the index of the first element
    firstIndex = ll.index(firstElement)

    finalList = []

    #create the final list
    finalListBeta = ll[firstIndex:]
    finalList = finalListBeta[:n]

    print(finalList)
    
    #return sum of the finalList
    return sum(finalList)

print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(3))
print(row_sum_odd_numbers(4))
print(row_sum_odd_numbers(5))

>>>
[1]
1

[3, 5]
8

[7, 9, 11]
27

[13, 15, 17, 19]
64

[21, 23, 25, 27, 29]
125
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='findoddint'>find the larger odd integer or number</h4>

```python
def find_it(seq):

    #find the odd integers
    res = [nums for nums in seq if nums % 2 == 1]
    #print(res)

    #find the occurencies
    listOutOrigin = []
    for element in res:
        a = res.count(element)
        listOutOrigin.append(a)
    #print(listOutOrigin)

    #join odd integers with odd occurencies into the dict
    dictionary = dict(zip(res, listOutOrigin))
    #print(dictionary)

    #max value and max key from dict
    max_value = max(dictionary.values())  # maximum value
    max_keys = [k for k, v in dictionary.items() if v == max_value]  # getting all keys containing the `maximum`
    #print(max_value, max_keys)

    return max_keys[0]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5, -1, -1, -1, -1, -1, -1, -1]))

>>>
-1
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='findoccur'>find the occurencies in the list</h4>

```python
def find_it(seq):

    #find the occurencies
    listOutOrigin = []
    for element in seq:
        a = seq.count(element)
        listOutOrigin.append(a)
    return listOutOrigin

print(find_it([12, 10, 8, 12, 7, 6, 4, 10, 12, 16, 16, 16]))

>>>
[3, 2, 1, 3, 1, 1, 1, 2, 3, 3, 3, 3]
>>>

```

<a href='#^'>^^^</a>

---

<h4 id='findmax'>find the max value in the list</h4>

```python
def find_it(seq):

    return max(seq)

print(find_it([12, 10, 8, 12, 7, 6, 4, 10, 12, 16, 16, 16]))

>>>
16
>>>

```

<a href='#^'>^^^</a>

---

```python
a = [1,2,3]
print(a)

a[2]=4
print(a)

>>>
[1, 2, 3]
[1, 2, 4]
>>>
```

<a href='#^'>^^^</a>

---

```python
# empty list
my_list = []
print(my_list)

# list of integers
my_list = [1, 2, 3]
print(my_list)

# list with mixed datatypes
my_list = [1, "Hello", 3.4]
print(my_list)

>>>
[]
[1, 2, 3]
[1, 'Hello', 3.4]
>>>
```

<a href='#^'>^^^</a>

---

```python
# nested list
my_list = ["mouse", [8, 4, 6], ['a']]

print(my_list)

>>>
['mouse', [8, 4, 6], ['a']]
>>>
```

<a href='#^'>^^^</a>

---

```python
#min max
l1 = [1, 2, 3, 50, 60, 100]

print(min(l1))
print(max(l1))

>>>
1
100
>>>
```

---

```python
my_list = ['p','r','o','b','e']

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

>>>
p
r
o
b
e
>>>
```

<a href='#^'>^^^</a>

---

```python
n_list = ["Happy", [2,0,1,5]]

print(n_list[0][1])    
print(n_list[1][3])

>>>
a
5
>>>
```

<a href='#^'>^^^</a>

---

```python
my_list = ['p','r','o','b','e']

print(my_list[-1])
print(my_list[-5])

>>>
e
p
>>>
```

<a href='#^'>^^^</a>

---

```python
my_list = [1, 2, 3, 4, 5, 6, 7]

print(my_list[2:5])
print(my_list[:-5])
print(my_list[5:])
print(my_list[:])

>>>
[3, 4, 5]
[1, 2]
[6, 7]
[1, 2, 3, 4, 5, 6, 7]
>>>
```

<a href='#^'>^^^</a>

---

```python
lst = ["apple", "banana", "cherry"]

print(lst)

lst[1] = "blackcurrant"

print(lst)

>>>
['apple', 'banana', 'cherry']
['apple', 'blackcurrant', 'cherry']
>>>
```

<a href='#^'>^^^</a>

---

```python
lst = ["apple", "banana", "cherry"]
lst.append("damson")

print(lst)
print(lst * 2)

>>>
['apple', 'banana', 'cherry', 'damson']
['apple', 'banana', 'cherry', 'damson', 'apple', 'banana', 'cherry', 'damson']
>>>
```

<a href='#^'>^^^</a>

---

```python
lst = ["apple", "banana", "cherry"]

print(lst)

lst.remove("banana")

print(lst)
print(len(lst))

>>>
['apple', 'banana', 'cherry']
['apple', 'cherry']
2
>>>
```

<a href='#^'>^^^</a>

---

```python
print(range(10))
print(list(range(10)))
print(list(range(2, 8)))
print(list(range(2, 20, 3)))

>>>
range(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 3, 4, 5, 6, 7]
[2, 5, 8, 11, 14, 17]
>>>
```

<a href='#^'>^^^</a>

---

```python
>>> x = range(1,5)
>>> type (x)
<class 'range'>
>>> 
```

<a href='#^'>^^^</a>

---

```python
>>> list(range(0, 10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
```

<a href='#^'>^^^</a>

---

```python
>>> list(range(20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 
```

<a href='#^'>^^^</a>

---

```python
>>> x = list(range(0,10))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> type(x)
<class 'list'>
>>> 
```

<a href='#^'>^^^</a>

---

```python
>>> start = 5
>>> stop = 20
>>> list(range(start,stop))
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 
```

<a href='#^'>^^^</a>

---

```python
>>> start = 5
>>> stop = 20
>>> list(range(start,stop,2))
[5, 7, 9, 11, 13, 15, 17, 19]
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='sortval'>sort the values</h4>


```python
def men_from_boys(arr):
    le, lo, ls = [], [], []

    for nums in arr:
        if nums % 2 == 0:
            le.append(nums)
        else:
            lo.append(nums)

    le.sort(reverse=False)
    lo.sort(reverse=True)
    le = list(dict.fromkeys(le))
    lo = list(dict.fromkeys(lo))
    ls.extend(le)
    ls.extend(lo)
    return ls

print(men_from_boys([1,2,3,4,5,3,4,5,6,1,2,3]))

>>>
[2, 4, 6, 5, 3, 1]
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='findunique'>find unique numbers</h4>

```python
def find_uniq(arr):
    if (arr[0] == arr[1]) or (arr[0] != arr[1] and arr[0] == arr[2]):
        repeatableNum = arr[0]
    else:
        repeatableNum = arr[1]

    for nums in arr:
        if nums != repeatableNum:
            return nums

    return nums

print(find_uniq([1,2,1]))

>>>
2
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='diff2arr'>Differences between two arrays</h4>

```python
def firstElem(tem):

    main = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

    #change the temp list to lowercase
    temp = [x.lower() for x in tem]

    #find the first element
    for x in temp:
        for y in main:
            if x == y:

                firstElem = main.index(y)
                tempnum = len(temp)
                lastElem = tempnum+firstElem
                convmain = main[firstElem:lastElem + 1]
                diff = list(set(convmain) - set(temp))

                #list to string
                finalConv = ''.join(diff)

                #change the output from lower to upper if it is needed
                if tem[0].isupper():
                    return finalConv.upper()
                else:
                    return finalConv

print(firstElem(['O','Q','R','S']))

>>>
P
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='findevenocc'>find the even occuranves in in the list</h4>

```python
def odd_ones_out(numbers):

    #print(numbers)

    #occurencies
    listOutOrigin = []
    for element in numbers:
        a = numbers.count(element)
        listOutOrigin.append(a)
    #print(listOutOrigin)

    #find the even occurencies in the list
    findTrue = [occurencies % 2 == 0 for occurencies in listOutOrigin]
    #print(findTrue)

    #find more than one index in the list
    findIndexesInTheList1 = [i for i, e in enumerate(findTrue) if e == True]
    #print(findIndexesInTheList1)

    #make a list for the results
    finalRes = [numbers[indexes] for indexes in findIndexesInTheList1]
    return finalRes

print(odd_ones_out([75, 68, 75, 47, 68]))

>>>
[75, 68, 75, 68]
>>>
```

<a href='#^'>^^^</a>

---
