
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

a = int(input("number:"))

def check_num():
  return(len(str(abs(a))))

b = check_num()
  
def main_check():
  if b == 1:
    return 1
  elif b == 2:
    return 2
  else: 
    return 3 
  
def check1():
  return (a * 1)
  
print(check2())
