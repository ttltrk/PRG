
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

def length():
  if len(lst2) == 1:
    return 1
  elif len(lst2) == 2:
    return 2
  elif len(lst2) == 3:
    return 3
    
l = length()

def check():
  if l == 1:
    print(lst1[0]*num)
  elif l == 2:
    print((lst1[0]*lst2[0])+(lst1[1]*lst2[1]))
  elif l == 3:
    print((lst1[2]*lst2[0])+(lst1[1]*lst2[1])+(lst1[0]*lst2[2]))
  
check()
