
lst1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
num = int(input("give me a number between 0 and 11111111, you can only use binary numbers: \n"))
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
  elif len(lst2) == 7:
    return 7
  elif len(lst2) == 8:
    return 8
  elif len(lst2) == 9:
    return 9
  elif len(lst2) == 10:
    return 10
  
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
  elif l == 7:
    print((lst1[6]*lst2[0])+(lst1[5]*lst2[1])+(lst1[4]*lst2[2])+(lst1[3]*lst2[3])+(lst1[2]*lst2[4])+(lst1[1]*lst2[5])+(lst1[0]*lst2[6]))
  elif l == 8: 
    print((lst1[7]*lst2[0])+(lst1[6]*lst2[1])+(lst1[5]*lst2[2])+(lst1[4]*lst2[3])+(lst1[3]*lst2[4])+(lst1[2]*lst2[5])+(lst1[1]*lst2[6])+(lst1[0]*lst2[7]))
  elif l == 9: 
    print((lst1[8]*lst2[0])+(lst1[7]*lst2[1])+(lst1[6]*lst2[2])+(lst1[5]*lst2[3])+(lst1[4]*lst2[4])+(lst1[3]*lst2[5])+(lst1[2]*lst2[6])+(lst1[1]*lst2[7])+(lst1[0]*lst2[8]))
  elif l == 10:  
    print((lst1[9]*lst2[0])+(lst1[8]*lst2[1])+(lst1[7]*lst2[2])+(lst1[6]*lst2[3])+(lst1[5]*lst2[4])+(lst1[4]*lst2[5])+(lst1[3]*lst2[6])+(lst1[2]*lst2[7])+(lst1[1]*lst2[8])+(lst1[0]*lst2[9]))

check()
