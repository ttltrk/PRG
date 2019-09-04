
```python
def solution(roman):

    romanNums = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000, "(V)" : 5000}

    l1 = []
    l1.append(roman)
    #print(l1)

    matchers1 = ['IV', 'IX']
    matching1 = [s for s in l1 if any(xs in s for xs in matchers1)]
    print(matching1)
    matchers2 = ['XL', 'XC']
    matching2 = [s for s in l1 if any(xs in s for xs in matchers2)]
    print(matching2)
    matchers3 = ['CD','CM']
    matching3 = [s for s in l1 if any(xs in s for xs in matchers3)]
    print(matching3)
    matchers4 = ['M(V)']
    matching4 = [s for s in l1 if any(xs in s for xs in matchers4)]
    print(matching4)

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
