
"""
convert numbers from binary to decimal easly
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
  elif len(lst2) == 4:
    return 4
  elif len(lst2) == 5:
    return 5
  elif len(lst2) == 6:
    return 6
    
l = length()

def check():
  if l == 1:
    print(lst1[0]*num)
  elif l == 2:
    print((lst1[1]*lst2[0])+(lst1[0]*lst2[1]))
  elif l == 3:
    print((lst1[2]*lst2[0])+(lst1[1]*lst2[1])+(lst1[0]*lst2[2]))
  elif l == 4:
    print((lst1[3]*lst2[0])+(lst1[2]*lst2[1])+(lst1[1]*lst2[2])+(lst1[0]*lst2[3]))
  elif l == 5:
    print((lst1[4]*lst2[0])+(lst1[3]*lst2[1])+(lst1[2]*lst2[2])+(lst1[1]*lst2[3])+(lst1[0]*lst2[4]))
  elif l == 6:
    print((lst1[5]*lst2[0])+(lst1[4]*lst2[1])+(lst1[3]*lst2[2])+(lst1[2]*lst2[3])+(lst1[1]*lst2[4])+(lst1[0]*lst2[5]))
    
check()
