import random

def ran1():
    if random.randint(0, 1) == 0:
        return 0
    else:
        return 1
        
def ran2():
    if random.randint(0, 1) == 0:
        return 0
    else:
        return 1
    
def ran3():
    if random.randint(0, 1) == 0:
        return 0
    else:
        return 1
    
i = 0
x = []
while i <= 6:
    x.append(ran1())
    if len(x) == 6:
        x1 = sum(x)
    i = i + 1
    
i = 0
xx = []
while i <= 6:
    xx.append(ran2())
    if len(xx) == 6:
        x2 = sum(xx)
    i = i + 1
    
i = 0
xxx = []
while i <= 6:
    xxx.append(ran2())
    if len(xxx) == 6:
        x3 = sum(xxx)
    i = i + 1
    
""" 
--------------------------------------------------------------------------------------
R1
--------------------------------------------------------------------------------------
"""
    
def a1_1():
    if x1 == 0 and x2 == 0 and x3 == 0:
        return 0
    elif x1 != 0 and x2 == 0 and x3 == 0:
        return 0
    elif x1 == 0 and x2 != 0 and x3 == 0:
        return 0
    elif x1 == 0 and x2 == 0 and x3 != 0:
        return 0
    elif x1 != 0 and x2 != 0 and x3 == 0:
        return 0
    elif x1 != 0 and x2 == 0 and x3 != 0:
        return 0
    elif x1 == 0 and x2 != 0 and x3 != 0:
        return 0
    elif x1 != 0 and x2 != 0 and x3 != 0:
        return ' '
    else:
        return ' '

def b1_1():
    if x1 == 1 and x2 == 1 and x3 == 1:
        return 1
    elif x1 != 1 and x2 == 1 and x3 == 1:
        return 1
    elif x1 == 1 and x2 != 1 and x3 == 1:
        return 1
    elif x1 == 1 and x2 == 1 and x3 != 1:
        return 1
    elif x1 != 1 and x2 != 1 and x3 == 1:
        return 1
    elif x1 != 1 and x2 == 1 and x3 != 1:
        return 1
    elif x1 == 1 and x2 != 1 and x3 != 1:
        return 1
    elif x1 != 1 and x2 != 1 and x3 != 1:
        return ' '
    else:
        return ' '

def c1_1():
    if x1 == 2 and x2 == 2 and x3 == 2:
        return 2
    elif x1 != 2 and x2 == 2 and x3 == 2:
        return 2
    elif x1 == 2 and x2 != 2 and x3 == 2:
        return 2
    elif x1 == 2 and x2 == 2 and x3 != 2:
        return 2
    elif x1 != 2 and x2 != 2 and x3 == 2:
        return 2
    elif x1 != 2 and x2 == 2 and x3 != 2:
        return 2
    elif x1 == 2 and x2 != 2 and x3 != 2:
        return 2
    elif x1 != 2 and x2 != 2 and x3 != 2:
        return ' '
    else:
        return ' '
    
def d1_1():
    if x1 == 3 and x2 == 3 and x3 == 3:
        return 3
    elif x1 != 3 and x2 == 3 and x3 == 3:
        return 3
    elif x1 == 3 and x2 != 3 and x3 == 3:
        return 3
    elif x1 == 3 and x2 == 3 and x3 != 3:
        return 3
    elif x1 != 3 and x2 != 3 and x3 == 3:
        return 3
    elif x1 != 3 and x2 == 3 and x3 != 3:
        return 3
    elif x1 == 3 and x2 != 3 and x3 != 3:
        return 3
    elif x1 != 3 and x2 != 3 and x3 != 3:
        return ' '
    else:
        return ' '

def e1_1():
    if x1 == 4 and x2 == 4 and x3 == 4:
        return 4
    elif x1 != 4 and x2 == 4 and x3 == 4:
        return 4
    elif x1 == 4 and x2 != 4 and x3 == 4:
        return 4
    elif x1 == 4 and x2 == 4 and x3 != 4:
        return 4
    elif x1 != 4 and x2 != 4 and x3 == 4:
        return 4
    elif x1 != 4 and x2 == 4 and x3 != 4:
        return 4
    elif x1 == 4 and x2 != 4 and x3 != 4:
        return 4
    elif x1 != 4 and x2 != 4 and x3 != 4:
        return ' '
    else:
        return ' '
    
def f1_1():
    if x1 == 5 and x2 == 5 and x3 == 5:
        return 5
    elif x1 != 5 and x2 == 5 and x3 == 5:
        return 5
    elif x1 == 5 and x2 != 5 and x3 == 5:
        return 5
    elif x1 == 5 and x2 == 5 and x3 != 5:
        return 5
    elif x1 != 5 and x2 != 5 and x3 == 5:
        return 5
    elif x1 != 5 and x2 == 5 and x3 != 5:
        return 5
    elif x1 == 5 and x2 != 5 and x3 != 5:
        return 5
    elif x1 != 5 and x2 != 5 and x3 != 5:
        return ' '
    else:
        return ' '

""" 
--------------------------------------------------------------------------------------
R2
--------------------------------------------------------------------------------------
"""
    
    
def a1_2():
    if x1 == 0 and x2 == 0 and x3 == 0:
        return 0
    elif x1 != 0 and x2 == 0 and x3 == 0:
        return 0
    elif x1 == 0 and x2 != 0 and x3 == 0:
        return 0
    elif x1 == 0 and x2 == 0 and x3 != 0:
        return 0
    elif x1 != 0 and x2 != 0 and x3 == 0:
        return ' '
    elif x1 != 0 and x2 == 0 and x3 != 0:
        return ' '
    elif x1 == 0 and x2 != 0 and x3 != 0:
        return ' '
    elif x1 != 0 and x2 != 0 and x3 != 0:
        return ' '
    else:
        return ' '

def b1_2():
    if x1 == 1 and x2 == 1 and x3 == 1:
        return 1
    elif x1 != 1 and x2 == 1 and x3 == 1:
        return 1
    elif x1 == 1 and x2 != 1 and x3 == 1:
        return 1
    elif x1 == 1 and x2 == 1 and x3 != 1:
        return 1
    elif x1 != 1 and x2 != 1 and x3 == 1:
        return ' '
    elif x1 != 1 and x2 == 1 and x3 != 1:
        return ' '
    elif x1 == 1 and x2 != 1 and x3 != 1:
        return ' '
    elif x1 != 1 and x2 != 1 and x3 != 1:
        return ' '
    else:
        return ' '

def c1_2():
    if x1 == 2 and x2 == 2 and x3 == 2:
        return 2
    elif x1 != 2 and x2 == 2 and x3 == 2:
        return 2
    elif x1 == 2 and x2 != 2 and x3 == 2:
        return 2
    elif x1 == 2 and x2 == 2 and x3 != 2:
        return 2
    elif x1 != 2 and x2 != 2 and x3 == 2:
        return ' '
    elif x1 != 2 and x2 == 2 and x3 != 2:
        return ' '
    elif x1 == 2 and x2 != 2 and x3 != 2:
        return ' '
    elif x1 != 2 and x2 != 2 and x3 != 2:
        return ' '
    else:
        return ' '
    
def d1_2():
    if x1 == 3 and x2 == 3 and x3 == 3:
        return 3
    elif x1 != 3 and x2 == 3 and x3 == 3:
        return 3
    elif x1 == 3 and x2 != 3 and x3 == 3:
        return 3
    elif x1 == 3 and x2 == 3 and x3 != 3:
        return 3
    elif x1 != 3 and x2 != 3 and x3 == 3:
        return ' '
    elif x1 != 3 and x2 == 3 and x3 != 3:
        return ' '
    elif x1 == 3 and x2 != 3 and x3 != 3:
        return ' '
    elif x1 != 3 and x2 != 3 and x3 != 3:
        return ' '
    else:
        return ' '

def e1_2():
    if x1 == 4 and x2 == 4 and x3 == 4:
        return 4
    elif x1 != 4 and x2 == 4 and x3 == 4:
        return 4
    elif x1 == 4 and x2 != 4 and x3 == 4:
        return 4
    elif x1 == 4 and x2 == 4 and x3 != 4:
        return 4
    elif x1 != 4 and x2 != 4 and x3 == 4:
        return ' '
    elif x1 != 4 and x2 == 4 and x3 != 4:
        return ' '
    elif x1 == 4 and x2 != 4 and x3 != 4:
        return ' '
    elif x1 != 4 and x2 != 4 and x3 != 4:
        return ' '
    else:
        return ' '
    
def f1_2():
    if x1 == 5 and x2 == 5 and x3 == 5:
        return 5
    elif x1 != 5 and x2 == 5 and x3 == 5:
        return 5
    elif x1 == 5 and x2 != 5 and x3 == 5:
        return 5
    elif x1 == 5 and x2 == 5 and x3 != 5:
        return 5
    elif x1 != 5 and x2 != 5 and x3 == 5:
        return ' '
    elif x1 != 5 and x2 == 5 and x3 != 5:
        return ' '
    elif x1 == 5 and x2 != 5 and x3 != 5:
        return ' '
    elif x1 != 5 and x2 != 5 and x3 != 5:
        return ' '
    else:
        return ' '
    
""" 
--------------------------------------------------------------------------------------
R3
--------------------------------------------------------------------------------------
""" 

def a1_3():
    if x1 == 0 and x2 == 0 and x3 == 0:
        return 0
    elif x1 != 0 and x2 == 0 and x3 == 0:
        return ' '
    elif x1 == 0 and x2 != 0 and x3 == 0:
        return ' '
    elif x1 == 0 and x2 == 0 and x3 != 0:
        return ' '
    elif x1 != 0 and x2 != 0 and x3 == 0:
        return ' '
    elif x1 != 0 and x2 == 0 and x3 != 0:
        return ' '
    elif x1 == 0 and x2 != 0 and x3 != 0:
        return ' '
    elif x1 != 0 and x2 != 0 and x3 != 0:
        return ' '
    else:
        return ' '
    
def b1_3():
    if x1 == 1 and x2 == 1 and x3 == 1:
        return 1
    elif x1 != 1 and x2 == 1 and x3 == 1:
        return ' '
    elif x1 == 1 and x2 != 1 and x3 == 1:
        return ' '
    elif x1 == 1 and x2 == 1 and x3 != 1:
        return ' '
    elif x1 != 1 and x2 != 1 and x3 == 1:
        return ' '
    elif x1 != 1 and x2 == 1 and x3 != 1:
        return ' '
    elif x1 == 1 and x2 != 1 and x3 != 1:
        return ' '
    elif x1 != 1 and x2 != 1 and x3 != 1:
        return ' '
    else:
        return ' '
    
def c1_3():
    if x1 == 2 and x2 == 2 and x3 == 2:
        return 2
    elif x1 != 2 and x2 == 2 and x3 == 2:
        return ' '
    elif x1 == 2 and x2 != 2 and x3 == 2:
        return ' '
    elif x1 == 2 and x2 == 2 and x3 != 2:
        return ' '
    elif x1 != 2 and x2 != 2 and x3 == 2:
        return ' '
    elif x1 != 2 and x2 == 2 and x3 != 2:
        return ' '
    elif x1 == 2 and x2 != 2 and x3 != 2:
        return ' '
    elif x1 != 2 and x2 != 2 and x3 != 2:
        return ' '
    else:
        return ' '
    
def d1_3():
    if x1 == 3 and x2 == 3 and x3 == 3:
        return 3
    elif x1 != 3 and x2 == 3 and x3 == 3:
        return ' '
    elif x1 == 3 and x2 != 3 and x3 == 3:
        return ' '
    elif x1 == 3 and x2 == 3 and x3 != 3:
        return ' '
    elif x1 != 3 and x2 != 3 and x3 == 3:
        return ' '
    elif x1 != 3 and x2 == 3 and x3 != 3:
        return ' '
    elif x1 == 3 and x2 != 3 and x3 != 3:
        return ' '
    elif x1 != 3 and x2 != 3 and x3 != 3:
        return ' '
    else:
        return ' '
    
def e1_3():
    if x1 == 4 and x2 == 4 and x3 == 4:
        return 4
    elif x1 != 4 and x2 == 4 and x3 == 4:
        return ' '
    elif x1 == 4 and x2 != 4 and x3 == 4:
        return ' '
    elif x1 == 4 and x2 == 4 and x3 != 4:
        return ' '
    elif x1 != 4 and x2 != 4 and x3 == 4:
        return ' '
    elif x1 != 4 and x2 == 4 and x3 != 4:
        return ' '
    elif x1 == 4 and x2 != 4 and x3 != 4:
        return ' '
    elif x1 != 4 and x2 != 4 and x3 != 4:
        return ' '
    else:
        return ' '
    
def f1_3():
    if x1 == 5 and x2 == 5 and x3 == 5:
        return 5
    elif x1 != 5 and x2 == 5 and x3 == 5:
        return ' '
    elif x1 == 5 and x2 != 5 and x3 == 5:
        return ' '
    elif x1 == 5 and x2 == 5 and x3 != 5:
        return ' '
    elif x1 != 5 and x2 != 5 and x3 == 5:
        return ' '
    elif x1 != 5 and x2 == 5 and x3 != 5:
        return ' '
    elif x1 == 5 and x2 != 5 and x3 != 5:
        return ' '
    elif x1 != 5 and x2 != 5 and x3 != 5:
        return ' '
    else:
        return ' '

print('|''---''|''---''|''---''|''---''|''---''|''---''|')
print('|',a1_3(),'|',b1_3(),'|',c1_3(),'|',d1_3(),'|',e1_3(),'|',f1_3(),'|')
print('|''---''|''---''|''---''|''---''|''---''|''---''|')
print('|',a1_2(),'|',b1_2(),'|',c1_2(),'|',d1_2(),'|',e1_2(),'|',f1_2(),'|')
print('|''---''|''---''|''---''|''---''|''---''|''---''|')
print('|',a1_1(),'|',b1_1(),'|',c1_1(),'|',d1_1(),'|',e1_1(),'|',f1_1(),'|')
print('|''---''|''---''|''---''|''---''|''---''|''---''|')
print('|'' 0 ''|'' 1 ''|'' 2 ''|'' 3 ''|'' 4 ''|'' 5 ''|')
