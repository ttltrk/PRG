
"""
1024
512
256
128
64
32
16
8
4
2
1
"""

lst1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

num = int(input("number?"))
lst2 = [int(i) for i in str(num)]

print(len(lst2))
print(lst2[1])
print(lst2[1]*lst1[1])
