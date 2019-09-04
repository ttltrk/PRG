
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

Roman Numerals Decoder

```python
def solution(roman):

    romanNums = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000, "(V)" : 5000}

    l1 = []
    l1.append(roman)

    matchers1 = ['IV', 'IX']
    matching1 = [s for s in l1 if any(xs in s for xs in matchers1)]
    matchers2 = ['XL', 'XC']
    matching2 = [s for s in l1 if any(xs in s for xs in matchers2)]
    matchers3 = ['CD','CM']
    matching3 = [s for s in l1 if any(xs in s for xs in matchers3)]
    matchers4 = ['M(V)']
    matching4 = [s for s in l1 if any(xs in s for xs in matchers4)]

    searchInDict = [romanNums[x] for x in roman]
    listSum = sum(searchInDict)

    if len(matching1) == 1 and len(matching2) == 0 and len(matching3) == 0 and len(matching4) == 0:
        return listSum-2
    elif len(matching1) == 1 and len(matching2) == 1 and len(matching3) == 0 and len(matching4) == 0:
        return listSum-22
    elif len(matching1) == 1 and len(matching2) == 1 and len(matching3) == 1 and len(matching4) == 0:
        return listSum-222
    elif len(matching1) == 1 and len(matching2) == 1 and len(matching3) == 1 and len(matching4) == 1:
        return listSum-2222
    elif len(matching1) == 1 and len(matching2) == 0 and len(matching3) == 0 and len(matching4) == 1:
        return listSum-2002
    elif len(matching1) == 1 and len(matching2) == 0 and len(matching3) == 1 and len(matching4) == 0:
        return listSum-202
    elif len(matching1) == 0 and len(matching2) == 1 and len(matching3) == 1 and len(matching4) == 1:
        return listSum-2220
    elif len(matching1) == 0 and len(matching2) == 0 and len(matching3) == 1 and len(matching4) == 1:
        return listSum-2200
    elif len(matching1) == 0 and len(matching2) == 0 and len(matching3) == 0 and len(matching4) == 1:
        return listSum-200
    elif len(matching1) == 0 and len(matching2) == 1 and len(matching3) == 0 and len(matching4) == 1:
        return listSum-2020
    elif len(matching1) == 0 and len(matching2) == 1 and len(matching3) == 1 and len(matching4) == 0:
        return listSum-220
    elif len(matching1) == 0 and len(matching2) == 1 and len(matching3) == 0 and len(matching4) == 0:
        return listSum-20
    elif len(matching1) == 0 and len(matching2) == 0 and len(matching3) == 1 and len(matching4) == 0:
        return listSum-200
    elif len(matching1) == 0 and len(matching2) == 0 and len(matching3) == 0 and len(matching4) == 1:
        return listSum-2000

    else:
        return listSum
```
     
---

Roman Numerals Encoder

```python
def solution(n):

    l = list(str(n))
    print(l)

    nums10 = {'1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':"VIII",'9':'IX','0':''}
    nums100 = {'1':'X','2':'XX','3':'XXX','4':'XL','5':'L','6':'LX','7':'LXX','8':'LXXX','9':'XC','0':''}
    nums1000 = {'1':'C','2':'CC','3':'CCC','4':'CD','5':'D','6':'DC','7':'DCC','8':'DCCC','9':'CM','0':''}
    nums5000 = {'1': 'M', '2': 'MM', '3': 'MMM', '4': 'M(V)', '5': '(V)'}

    if len(l) == 1:
        return nums10[str(n)]
    elif len(l) == 2:
        return nums100[str(l[0])]+nums10[str(l[1])]
    elif len(l) == 3:
        return nums1000[str(l[0])]+nums100[str(l[1])]+nums10[str(l[2])]
    elif len(l) == 4:
        return nums5000[str(l[0])]+nums1000[str(l[1])]+nums100[str(l[2])]+nums10[str(l[3])]
```

---
