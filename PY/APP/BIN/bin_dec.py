
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

def check():
  return(len(str(abs(a))))

b = check()
  
def check2():
  if b == 1:
    return (a * 1)
  elif b == 2:
    print("2")
  else:
    print("3")

print(check2())
