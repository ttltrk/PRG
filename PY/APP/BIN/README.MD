
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

### Binary ~ Decimal Converter

---

```python
"""
input = 1010

1 x 8 = 8
0 x 4 = 0
1 x 2 = 2
0 x 1 = 0

0+2+0+8 = 10

1010 = 10 
"""
lst1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
num = int(input("give me a number between 0 and 11111111, you can only use binary numbers: \n"))
lst2 = [int(i) for i in str(num)]

def length():
    res = 0
    if len(lst2) == 1:
        res = 1
    elif len(lst2) == 2:
        res = 2
    elif len(lst2) == 3:
        res = 3
    elif len(lst2) == 4:
        res = 4
    elif len(lst2) == 5:
        res = 5
    elif len(lst2) == 6:
        res = 6
    elif len(lst2) == 7:
        res = 7
    elif len(lst2) == 8:
        res = 8
    elif len(lst2) == 9:
        res = 9
    elif len(lst2) == 10:
        res = 10
    return res



l = length()


def check():
    if l == 1:
        print(lst1[0] * num)
    elif l == 2:
        print((lst1[1] * lst2[0]) + (lst1[0] * lst2[1]))
    elif l == 3:
        print((lst1[2] * lst2[0]) + (lst1[1] * lst2[1]) + (lst1[0] * lst2[2]))
    elif l == 4:
        print((lst1[3] * lst2[0]) + (lst1[2] * lst2[1]) + (lst1[1] * lst2[2]) + (lst1[0] * lst2[3]))
    elif l == 5:
        print(
            (lst1[4] * lst2[0]) + (lst1[3] * lst2[1]) + (lst1[2] * lst2[2]) + (lst1[1] * lst2[3]) + (lst1[0] * lst2[4]))
    elif l == 6:
        print((lst1[5] * lst2[0]) + (lst1[4] * lst2[1]) + (lst1[3] * lst2[2]) + (lst1[2] * lst2[3]) + (
                    lst1[1] * lst2[4]) + (lst1[0] * lst2[5]))
    elif l == 7:
        print((lst1[6] * lst2[0]) + (lst1[5] * lst2[1]) + (lst1[4] * lst2[2]) + (lst1[3] * lst2[3]) + (
                    lst1[2] * lst2[4]) + (lst1[1] * lst2[5]) + (lst1[0] * lst2[6]))
    elif l == 8:
        print((lst1[7] * lst2[0]) + (lst1[6] * lst2[1]) + (lst1[5] * lst2[2]) + (lst1[4] * lst2[3]) + (
                    lst1[3] * lst2[4]) + (lst1[2] * lst2[5]) + (lst1[1] * lst2[6]) + (lst1[0] * lst2[7]))
    elif l == 9:
        print((lst1[8] * lst2[0]) + (lst1[7] * lst2[1]) + (lst1[6] * lst2[2]) + (lst1[5] * lst2[3]) + (
                    lst1[4] * lst2[4]) + (lst1[3] * lst2[5]) + (lst1[2] * lst2[6]) + (lst1[1] * lst2[7]) + (
                          lst1[0] * lst2[8]))
    elif l == 10:
        print((lst1[9] * lst2[0]) + (lst1[8] * lst2[1]) + (lst1[7] * lst2[2]) + (lst1[6] * lst2[3]) + (
                    lst1[5] * lst2[4]) + (lst1[4] * lst2[5]) + (lst1[3] * lst2[6]) + (lst1[2] * lst2[7]) + (
                          lst1[1] * lst2[8]) + (lst1[0] * lst2[9]))


check()
```

