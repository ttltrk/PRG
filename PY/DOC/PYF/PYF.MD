
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD) - [UX](https://github.com/ttltrk/ELSE/blob/master/M/UX/UX.MD)

---

<h3 id='^'>Python</h3>

---

* [Data Structures](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DataStruct/DS.MD)
* [Control Flow](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/ControlFlow/CF.MD)
* [OOP](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/OOP/OOP.MD)
* [Packages/Modules/Files](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/Pack/Pack.MD)
* [Errors](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/ERR/ERR.MD)
* [ETL](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/ETL/ETL.MD)
* [DB](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DB/DB.MD)
* [HW](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/HW/HW.MD)
* [Front end](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/FrontEnd/FE.MD)
* [DS/DL/ML]()

---




<h3 id='errexc'>errors and exceptions</h3>

---

```python
def add(n1,n2):
    print(n1+n2)

num1 = 10
num2 = input('add a number ')

add(num1,num2)

>>>
add a number 20
Traceback (most recent call last):
  File "C:tt3.py", line 12, in <module>
    add(num1,num2)
  File "C:t3.py", line 7, in add
    print(n1+n2)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

```python
try:
    result = 10+10

except:
    print('hey it looks like you are not adding correctly!')

print(result)

>>>
20
>>>
```

```python
try:
    result = 10+'10'

except:
    print('hey it looks like you are not adding correctly!')

else:
    print('add went well')
    print(result)

>>>
hey it looks like you are not adding correctly!
>>>
```

```python
try:
    result = 10+10

except:
    print('hey it looks like you are not adding correctly!')

else:
    print('add went well')
    print(result)

>>>
add went well
20
>>>
```

```python
try:
    f = open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\TEST\\testfile.txt', 'w') 
    f.write('Write a test line')
    
except TypeError:
    print('There was a type error!')

except OSError:
    print('Hey you have an OS error!')

finally:
    print('I always run!')

>>>
I always run!
>>>
```

```python
def ask_for_int():
    try:
        result = int(input('Please provide number: '))
    except:
        print('Whoops, that is not a number')
    finally:
        print('End of try/except/finally')

ask_for_int()

>>>
Please provide number: 17
End of try/except/finally
>>>

>>>
Please provide number: dd
Whoops, that is not a number
End of try/except/finally
>>>
```

```python
def ask_for_int():

    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Whoops, that is not a number')
            continue
        else:
            print('Yes thank you')
            break
        finally:
            print('End of try/except/finally')
            print('I will always run at the end')

ask_for_int()

>>>
Please provide number: 2
Yes thank you
End of try/except/finally
I will always run at the end
>>>

>>>
Please provide number: dd
Whoops, that is not a number
End of try/except/finally
I will always run at the end
Please provide number: cc
Whoops, that is not a number
End of try/except/finally
I will always run at the end
Please provide number: 3
Yes thank you
End of try/except/finally
I will always run at the end
>>>
```

```python
try:
    for i in ['a','b','c']:
        print(i**2)

except:
    print('Type error, watch out!')

>>>
Type error, watch out!
>>>
```

```python
try:
    x = 5
    y = 0
    z = x/y

except:
    print('error')

finally:
    print('all done')

>>>
error
all done
>>>
```

```python
def ask():

    while True:
        try:
            n = int(input('Enter a number: '))
        except:
            print('Please try again! \n')
            continue
        else:
            break

    print('Your number squared is: ')
    print(n**2)

ask()

>>>
Enter a number: we
Please try again! 

Enter a number: pe
Please try again! 

Enter a number: ti
Please try again! 

Enter a number: 10
Your number squared is: 
100
>>> 
```

---

<h3 id='decorators'>Decorators</h3>

```python
def hello():
    return 'hi'

print(hello())
greet = hello
print(greet())

>>>
hi
hi
>>>
```

```python
def hello(name='trk'):
    print('the hello() function was executed')

    def greet():
        return '\t this is tge greet() func inside hello'

    print(greet())

hello()

>>>
the hello() function was executed
	 this is tge greet() func inside hello
>>>
```

```python
def hello(name='trk'):
    print('the hello() function was executed')

    def greet():
        return '\t this is the greet() func inside hello'

    def welcome():
        return '\t this is welcome() inside hello '

    print(greet())
    print(welcome())
    print('this is the end of hello() function')

hello()

>>>
the hello() function was executed
	 this is the greet() func inside hello
	 this is welcome() inside hello 
this is the end of hello() function
>>>
```

```python
def hello(name='trk'):
    print('the hello() function was executed')

    def greet():
        return '\t this is the greet() func inside hello'

    def welcome():
        return '\t this is welcome() inside hello '

    print('Im going to return a function')

    if name == 'trk':
        return greet
    else:
        return welcome

my_new_func = hello('trk')

print(my_new_func())

>>>
the hello() function was executed
Im going to return a function
	 this is the greet() func inside hello
>>>
```

```python
def cool():

    def super_cool():
        return 'I am very cool!'

    return super_cool

some_func = cool()
print(some_func())

>>>
I am very cool!
>>>
```

```python
def hello():
    return 'hi trk'

def other(some_def_func):
    print('Other code runs here')
    print(some_def_func)

print(hello())
other(hello)

>>>
hi trk
Other code runs here
<function hello at 0x00F29B28>
>>>
```

```python
def new_decorator(original_func):

    def wrap_func():
        print('some extra code, before the original function')

        original_func()
        print('some extra code, after the original function')

    return wrap_func

def func_needs_decorator():
    print('I want to be decorated')

#func_needs_decorator()
decrated_func = new_decorator(func_needs_decorator)
decrated_func()

>>>
some extra code, before the original function
I want to be decorated
some extra code, after the original function
>>>
```

```python
def new_decorator(original_func):

    def wrap_func():
        print('some extra code, before the original function')

        original_func()
        print('some extra code, after the original function')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print('I want to be decorated')

func_needs_decorator()

>>>
some extra code, before the original function
I want to be decorated
some extra code, after the original function
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='generators'>Generators</h3>

```python
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(10))

>>>
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>>
```

```python
def gen_fibon(n):

    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for number in gen_fibon(10):
    print(number)
    
>>>
1
1
2
3
5
8
13
21
34
55
>>>
```

```python
def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)
    
>>>
0
1
2
>>>
```

```python
def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()

print(next(g))

>>>
0
1
2
0
>>>
```

```python
s = 'hello'

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))

>>>
h
e 
>>>
```

```python
def gensquares(N):
    for i in range(N):
        yield i**2

for x in gensquares(10):
    print(x)
    
>>>
0
1
4
9
16
25
36
49
64
81
>>>
```

```python
import random

random.randint(1,10)

def rand_num(low,high,n):

    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)
    
>>>
2
9
7
4
6
9
10
4
4
3
5
9
>>>
```

```python
s = 'hello'
s = iter(s)
print(next(s))

>>>
h
>>>
```

```python
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item>3)

for item in gencomp:
    print(item)

>>>
4
5
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='bonobo'>Bonobo</h3>

---

<a href='#boninstall'>Install</a><br>
<a href='#bonver'>Version</a><br>
<a href='#bonfirstjob'>First Job</a><br><br>

<a href='#^'>^^^</a>

---

<h4 id='boninstall'>Install</h4>

```python
#install bonobo
py -m pip install bonobo
```

<a href='#^'>^^^</a>

---

<h4 id='bonver'>Version</h4>

```python
#check version
py -m bonobo version

>>>
bonobo v.0.6.3
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='bonfirstjob'>First Job</h4>

```python
C:\path\path>py -m bonobo init first.py
INFO|0000|init: Generated first.py using template 'default'.

C:\path\path>first.py
Hello
World
 - extract in=1 out=2 [done]
 - transform in=2 out=2 [done]
 - load in=2 [done]
```

<a href='#^'>^^^</a>

---

<h3 id='db2'>DB2</h3>

<a href='#^'>^^^</a>

---

<h3 id='postgresql'>PostgreSQL</h3>

<a href='#^'>^^^</a>

---

<h3 id='raspberrypi'>Raspberry Pi</h3>

<a href='#^'>^^^</a>

---

<h3 id='kivy'>Kivy</h3>

---

<a href='#kivyinstall'>Install</a><br>

<a href='#^'>^^^</a>

---

<h3 id='tkinter'>Tkinter</h3>

* <a href='#window'>Creating window</a><br>
* <a href='#addtext'>Adding text</a><br>
* <a href='#buttons'>Buttons</a><br>
* <a href='#decbut'>Decorating buttons</a><br>
* <a href='#intbut'>Interactive buttons</a><br>
* <a href='#tk_userinput'>User input</a><br>
* <a href='#tk_frames'>Frames</a><br>
* <a href='#tk_title'>Adding a title</a><br>
* <a href='#tk_icon'>Adding an icon</a><br>
* <a href='#tk_images'>Adding images</a><br>
* <a href='#tk_defsize'>Default size of the window</a><br>
* <a href='#tk_fill'>Fill</a><br>
* <a href='#tk_usinggrid'>using grid</a><br>
* <a href='#tk_aligning'>aligning</a><br>
* <a href='#tk_spanningcolumns'>spanning columns</a><br>
* <a href='#tk_bindingfunctions'>binding functions</a><br>
* <a href='#tkfunc1'>tkinter functions1</a><br>
* <a href='#tkfunc2'>tkinter functions2</a><br>
* <a href='#clickcount'>creating a click counter</a><br>
* <a href='#eventlab'>common event labels</a><br>
* <a href='#lrclick'>left and right click</a><br>
* <a href='#lrclickcount'>left and right click counter</a><br>
* <a href='#tkoop'>creating classes OOP</a><br>
* <a href='#tkmenu'>creating menus</a><br>
* <a href='#tksubmenu'>submenus</a><br>
* <a href='#tkdraw'>drawing using canvas</a><br>
* <a href='#entins'>entry insert</a><br>
* <a href='#tkdrws'>drawings</a><br>
* <a href='#tkpaint'>creating a basic paint program</a><br>
* <a href='#tkscale'>scale</a><br>
* <a href='#tkstorescale'>storing scale inputs</a><br>
* <a href='#tktheapp'>thermostat app</a><br>
* <a href='#tkmessagebox'>messagebox</a><br>
* <a href='#tkwindowcolour'>window colour</a><br>
* <a href='#tkdycrwi'>dynamically creating widgets</a><br>
* <a href='#tkdystywi'>dynamically styling widgets</a><br>
* <a href='#tkguessgame'>guess game</a><br>
* <a href='#tkguessgamepp'>guess game++</a><br>

<a href='#^'>^^^</a>

---

<h4 id='window'>Creating window</h4>

```python
from tkinter import *

root = Tk()
root.mainloop()

>>>
G first window
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='addtext'>Adding text</h4>

```python
from tkinter import *

root = Tk()
amazing_label = Label(root,text='Amazing!')
amazing_label.pack()
root.mainloop()

>>>
G window with label Amazing
>>>
```

```python
from tkinter import *

root = Tk()
amazing_label = Label(root,text='Amazing!')
label_2 = Label(root,text='And still...')

amazing_label.pack()
label_2.pack()
root.mainloop()

>>>
G window with label Amazing and with And still
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='buttons'>Buttons</h4>

```python
from tkinter import *

root = Tk()

fun_button = Button(root,text='click me')
fun_button.pack()

root.mainloop()

>>>
simple button with click me
>>>
```

```python
from tkinter import *

root = Tk()

fun_button = Button(root,text='click me')
fun_button.pack(side=LEFT)
#fun_button.pack(side=RIGHT)
#fun_button.pack(side=TOP)
#fun_button.pack(side=BOTTOM)

root.mainloop()

>>>
the button is on the left/right/top/bottom side
>>>
```

```python
from tkinter import *

root = Tk()

lb1 = Label(root,text='lil label')
fun_button = Button(root,text='click me')

lb1.pack(side=RIGHT)
fun_button.pack(side=LEFT)

root.mainloop()

>>>
the button is on the left and the label is on the right side
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='decbut'>Decorating Buttons</h4>

```python
from tkinter import *

root = Tk()

bt1 = Button(root,text='I am a button',padx=200)
bt1.pack()

root.mainloop()

>>>
button with padding x is 200
>>>
```

```python
from tkinter import *

root = Tk()

bt1 = Button(root,text='I am a button',pady=200)
bt1.pack()

root.mainloop()

>>>
button with padding y is 200
>>>
```

```python
from tkinter import *

root = Tk()

bt1 = Button(root,text='I am a button',padx=100,pady=100,fg='blue')
bt1.pack()

root.mainloop()

>>>
button with blue text
>>>
```

```python
from tkinter import *

root = Tk()

bt1 = Button(root,text='I am a button',padx=100,pady=100,fg='blue',bg='green')
bt1.pack()

root.mainloop()

>>>
button with blue text and with green background
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='intbut'>Interactive Buttons</h4>

```python
from tkinter import *

root = Tk()

def btn():
    print('the button has been clicked')

bt1 = Button(root,text='click me',command=btn)
bt1.pack()

root.mainloop()

>>>
button with command 'button has been clicked'
>>>
```

```python
from tkinter import *

root = Tk()

def btn():
    bt1.config(text='oh no, I;ve been clicked')

bt1 = Button(root,text='click me',command=btn)
bt1.pack()

root.mainloop()

>>>
button after click will be change the text
>>>
```

```python
from tkinter import *

root = Tk()

def btn():
    bt1.config(text='oh no, Ive been clicked', fg='red')

bt1 = Button(root,text='click me',command=btn)
bt1.pack()

root.mainloop()

>>>
same as above, just with red text
>>>
```

```python
from tkinter import *

root = Tk()

def btn():
    bt1.pack(side=LEFT)

bt1 = Button(root,text='click me',command=btn)
bt1.pack()

root.mainloop()

>>>
after click moved to the left side
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tk_userinput'>User input</h4>

```python
from tkinter import *

root = Tk()

def name_submit():
    print("your name is: {}".format(e1.get()))

label1 = Label(root,text='whats your name?')
e1 = Entry(root)
btn1 = Button(root,text='submit',command=name_submit)

label1.pack()
e1.pack()
btn1.pack()

root.mainloop()

>>>
user input with name
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tk_frames'>Frames</h4>

```python
from tkinter import *

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

label1 = Label(frame1,text='Iam in frame one')
button1 = Button(frame1,text='Im frame 1 too')

label2 = Label(frame2,text='Iam in frame 22')
button2 = Button(frame2,text='Im frame 2 too')

frame1.pack()
frame2.pack(side=BOTTOM)
label1.pack(side=LEFT)
label2.pack(side=RIGHT)
button1.pack()
button2.pack()

root.mainloop()

>>>
separate the labels and buttons top and bottom, left and right
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tk_title'>Adding a title</h4>

```python
from tkinter import *

root = Tk()

root.title("window")

root.mainloop()

>>>
window title - window
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tk_icon'>Adding an icon</h4>

```python
from tkinter import *

root = Tk()

root.title("icon test")
root.iconbitmap("C:\\path\\path\\favicon.ico")

root.mainloop()

>>>
icon in the title bar
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tk_images'>Adding images</h4>

```python
from tkinter import *

root = Tk()

photo = PhotoImage(file="C:\\path\\path\\blabla.gif")
w = Label(root,image=photo)
w.pack()

root.mainloop()

>>>
open images
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tk_defsize'>Default size of the window</h4>

```python
from tkinter import *

root = Tk()

root.geometry("500x500")

root.mainloop()

>>>
creating window with 500x500
>>>
```

<h4 id='tk_fill'>Fill</h4>

```python
from tkinter import *

root = Tk()

label1 = Label(root,text='Red', bg='red')
label2 = Label(root,text='Green', bg='green')
label3 = Label(root,text='Blue', bg='blue')

label1.pack(fill=X)
label2.pack(fill=X)
label3.pack(fill=X)

root.mainloop()

>>>
3 labels red, green, blue
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tk_usinggrid'>using grid</h4>

```python
from tkinter import *

root = Tk()

mail_label = Label(root,text='mail:')
password_label = Label(root,text='pwd:')

mail_entry = Entry(root)
password_entry = Entry(root)

mail_label.grid(row=0,column=0)
mail_entry.grid(row=0,column=1)
password_label.grid(row=1,column=0)
password_entry.grid(row=1,column=1)

root.mainloop()
```

<a href='#^'>^^^</a>

---

<h4 id='tk_aligning'>aligning</h4>

```python
from tkinter import *

root = Tk()

label_1 = Label(root,text="mail:")
label_2 = Label(root,text="password:")

entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0,column=0,sticky=E)
label_2.grid(row=1,column=0)

entry_1.grid(row=0,column=1,pady=100)
entry_2.grid(row=1,column=1,ipady=200)

root.mainloop()
```

<a href='#^'>^^^</a>

---

<h4 id='tk_spanningcolumns'>spanning columns</h4>

```python
from tkinter import *

root = Tk()

check = Checkbutton(root)
label1 = Label(root,text='keep me logged in')

check.grid(row=0,column=0)
label1.grid(row=1,column=0,columnspan=2)

root.mainloop()

>>>
checkbutton config
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tk_bindingfunctions'>binding functions</h4>

```python
from tkinter import *

root = Tk()

def button_clicked(event):
    print('great click')

button1 = Button(root,text='Click me')
button1.bind('<Button-1>',button_clicked)
button1.pack()

root.mainloop()

>>>
after click - event
>>>
```

```python
from tkinter import *

root = Tk()

def button_clicked(event):
    print('great click')

def key_pressed(event):
    print('I see you key pressed')

root.bind('<Key>',key_pressed)

button1 = Button(root,text='Click me')
button1.bind('<Button-1>',button_clicked)
button1.pack()

root.mainloop()

>>>
great click
great click
great click
great click
I see you key pressed
I see you key pressed
I see you key pressed
I see you key pressed
I see you key pressed
I see you key pressed
I see you key pressed
I see you key pressed
I see you key pressed
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tkfunc1'>tkinter functions1</h4>

```python
from tkinter import *

root = Tk()

def button_clicked_a(event):
    a= 2+2
    print(a)

def button_clicked_b(event):
    b = 3+3
    print(b)

button1 = Button(root,text='2+2')
button2 = Button(root,text='3+3')

button1.bind('<Button-1>',button_clicked_a)
button2.bind('<Button-1>',button_clicked_b)

button1.pack()
button2.pack()

root.mainloop()

>>>
choose 1st button 2nd button
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tkfunc2'>tkinter functions2</h4>

```python
from tkinter import *

root = Tk()

def button_clicked_a(event):
    a= 2+2
    print(a)

def button_clicked_b(event):
    b = 3+3
    print(b)

def name_submit():
    print("your name is: {}".format(e1.get()))

def nums():
    an = int(input('number1: '))
    bn = int(input('number2: '))
    print(an + bn)
    
button1 = Button(root,text='2+2')
button2 = Button(root,text='3+3')
label1 = Label(root,text='whats your name?')
e1 = Entry(root)
button3 = Button(root,text='submit',command=name_submit)


button1.bind('<Button-1>',button_clicked_a)
button2.bind('<Button-1>',button_clicked_b)


button1.pack()
button2.pack()
button3.pack()
label1.pack()
e1.pack()

root.mainloop()

>>>
button menu
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='clickcount'>creating a click counter</h4>

```python
from tkinter import *

root = Tk()

counter = 0

def click_counter():
    global counter
    counter += 1
    button_counter.config(text=counter)

button1 = Button(root,text='click me',command=click_counter)
button_counter = Label(root,text=counter)

button1.pack()
button_counter.pack()

root.mainloop()

>>>
click counter
>>>
```

```python
from tkinter import *

root = Tk()

counter = 0

def click_p():
    global counter
    counter += 1
    button_counter.config(text=counter)

def click_m():
    global counter
    counter -= 1
    button_counter.config(text=counter)

button1 = Button(root,text='+',command=click_p)
button2 = Button(root,text='-',command=click_m)
button_counter = Label(root,text=counter)

button1.pack()
button2.pack()
button_counter.pack()

root.mainloop()

>>>
+- counter
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='eventlab'>common event labels</h4>

```python
from tkinter import *

root = Tk()

def foo(event):
    print('working just fine')

root.bind('<Key>',foo)

root.mainloop()

>>>
while typing and not clicking 

working just fine
working just fine
working just fine
working just fine
working just fine
working just fine
working just fine
working just fine
working just fine
>>>
```

```python
from tkinter import *

root = Tk()

def foo(event):
    print('working just fine')

root.bind('<Enter>',foo)

root.mainloop()

>>>
while hit the enter

working just fine
working just fine
working just fine
working just fine
>>>
```

```python
from tkinter import *

root = Tk()

def foo(event):
    print('working just fine')

root.bind('<Leave>',foo)

root.mainloop()

>>>
while mouse move leave the window
    
working just fine
working just fine
working just fine
working just fine
working just fine
working just fine
working just fine
>>>
```

```python
from tkinter import *

root = Tk()

def foo(event):
    print('working just fine')

root.bind('a',foo)

root.mainloop()

>>>
while type a 

working just fine
working just fine
working just fine
working just fine
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='lrclick'>left and right click</h4>

```python
from tkinter import *

root = Tk()

def left_click(event):
    print('you have left clicked')

def right_click(event):
    print('you have right clicked')

right_button = Button(root,text='right button')
left_button = Button(root,text='left button')

left_button.bind('<Button-1>',left_click)
right_button.bind('<Button-1>',right_click)

left_button.pack()
right_button.pack()

root.mainloop()
```

<a href='#^'>^^^</a>

---

<h4 id='lrclickcount'>left and right click counter</h4>

```python
from tkinter import *

root = Tk()
left_counter = 0
right_counter = 0

def left_click(event):
    global left_counter
    left_counter += 1
    left_label.config(text=left_counter)

def right_click(event):
    global right_counter
    right_counter += 1
    right_label.config(text=right_counter)

left_label = Label(root,text=left_counter)
right_label = Label(root,text=right_counter)

right_button = Button(root,text='right button')
left_button = Button(root,text='left button')

left_button.bind('<Button-1>',left_click)
right_button.bind('<Button-1>',right_click)

left_label.pack()
left_button.pack()
right_label.pack()
right_button.pack()

root.mainloop()
```

<a href='#^'>^^^</a>

---

<h4 id='tkoop'>creating classes OOP</h4>

```python
from tkinter import *

root = Tk()

class OneButton:

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text='click me',command=self.printMessage)
        self.printButton.pack(side=LEFT)

    def printMessage(self):
        print('congrat')

button = OneButton(root)
root.mainloop()

>>>
after click congrat
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tkmenu'>creating menus</h4>

```python
from tkinter import *

root = Tk()

my_menu = Menu(root)
root.config(menu = my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label='file',menu=file_menu)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label='edit',menu=edit_menu)

root.mainloop()

>>>
basic menu 
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tksubmenu'>submenus</h4>

```python
from tkinter import *

root = Tk()

def foo():
    print('nice')

my_menu = Menu(root)
root.config(menu = my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label='file',menu=file_menu)

file_menu.add_command(label='New notebook',command=foo)
file_menu.add_command(label='open',command=foo)
file_menu.add_separator()
file_menu.add_command(label='make a copy',command=foo)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label='edit',menu=edit_menu)

edit_menu.add_command(label='cut cells',command=foo)
edit_menu.add_command(label='copy cells',command=foo)
edit_menu.add_separator()
edit_menu.add_command(label='paste cells',command=foo)

root.mainloop()

>>>
submenus
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tkdraw'>drawing using canvas</h4>

```python
from tkinter import *

root = Tk()

canvas = Canvas(width=300,height=200)
canvas.pack()

canvas.create_line(0,0,300,200,fill='red')

root.mainloop()

>>>
red line
>>>
```

```python
from tkinter import *

root = Tk()

canvas_r = Canvas(width=100,height=100)
canvas_r.pack()

canvas_r.create_rectangle(10,10,40,40,fill='red')

root.mainloop()

>>>
red rectangle
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='entins'>entry insert</h4>

```python
from tkinter import *

root = Tk()
root.title('szo')
root.geometry('300x300')

entry = Entry(root)
entry.place(x=50,y=0)

def doc1():
    with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\MM\\PY\\FILE123\\FVT\\FVT.txt', mode='r') as d1_txt:
        d1 = d1_txt.read()
        return d1

def get_name():
    entry.insert(0, doc1())

label = Label(root,text='name: ')
label.place(x=0,y=0)

btn = Button(root, text='get name', command = lambda : get_name())
btn.place(x=100,y=100)

root.mainloop()
```

<a href='#^'>^^^</a>

---

<h4 id='tkdrws'>drawings</h4>

```python
from tkinter import *

root = Tk()

canvas = Canvas(root,width=200,height=200)
canvas.pack()
canvas.create_oval(50,50,100,100,fill='yellow')

root.mainloop()

>>>
creating a yellow oval
>>>
```

```python
from tkinter import *

root = Tk()

canvas = Canvas(root,width=200,height=200)
canvas.pack()
canvas.create_polygon(30,30,60,30,45,45)

root.mainloop()

>>>
creating a black polygon
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tkpaint'>creating a basic paint program</h4>

```python
from tkinter import *

root = Tk()

def paint_func(event):
    canvas.create_oval(event.x,event.y,event.x+1,event.y+1,fill='orange')

welcome = Label(root,text='just draw with left button',fg='yellow',bg='blue')
welcome.pack()
canvas = Canvas(root,width=200,height=200)
canvas.bind('<B1-Motion>',paint_func)
canvas.pack()

root.mainloop()

>>>
basic paint program
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tkscale'>scale</h4>

```python
from tkinter import *

root = Tk()

scale = Scale(root,from_=20,to=200,orient=HORIZONTAL)
scale.pack()

root.mainloop()

>>>
creating a scale
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tkstorescale'>storing scale inputs</h4>

```python
from tkinter import *

root = Tk()

def store_scale():
    score = scale.get()
    print(score)

    if score > 50:
        print('more than 50')


scale = Scale(root)
scale.pack()

button1 = Button(root,text='enter',command=store_scale)
button1.pack()

root.mainloop()

>>>
print out the scale input
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tktheapp'>thermostat app</h4>

```python
from tkinter import *

root = Tk()

def change_temp():
    temp = thermostat.get()

    if temp < 10:
        print('coldddd')
    elif temp > 50 and temp < 89:
        print('warning, high temp')
    elif temp > 90:
        print('upppps HOOOOOOT')

thermostat = Scale(root)
warning = Label(root,text='this is your thermostat, take care')
warning.pack()
thermostat.pack()

button1 = Button(root,text='change temp',command=change_temp)
button1.pack()

root.mainloop()

>>>
making a thermostat app
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='tkmessagebox'>messagebox</h4>

```python
from tkinter import *
from tkinter import messagebox
root = Tk()

def error_message():
    messagebox.showinfo('this is an error')

button1 = Button(root,text='donot click me',command=error_message)
button1.pack()

root.mainloop()
```

<a href='#^'>^^^</a>

---

<h4 id='tkwindowcolour'>window colour</h4>

```python
#window colour
from tkinter import *

root = Tk()

root.configure(bg='blue')

root.mainloop()
```

<a href='#^'>^^^</a>

---

<h4 id='tkdycrwi'>dynamically creating widgets</h4>

```python
#dynamically creating widgets
from tkinter import *

root = Tk()

colours = ['red','green','blue']

for colour in colours:
    button = Button(root,text=colour)
    button.pack(side=LEFT)

root.mainloop()
```

<a href='#^'>^^^</a>

---

<h4 id='tkdystywi'>dynamically styling widgets</h4>

```python
#dynamically styling widgets
from tkinter import *

root = Tk()

colour_list = ['red','green','blue','yellow','black']
country_list = ['UK', 'Portugal', 'Spain', 'US', 'Germany']

for i in range(5):
    button = Button(root,text=country_list[i],bg=colour_list[i])
    button.pack(side=LEFT)

root.mainloop()
```

<a href='#^'>^^^</a>

---

<h4 id='tkguessgame'>guess game</h4>

```python
#guess game
from tkinter import *
import random

root = Tk()

x_coord = random.randint(0,200)
y_coord = random.randint(0,200)

def guess(event):
    print('you clicked at x: {} y: {}. You are {} away from x and {} from y'
          .format(event.x,event.y,abs(event.x-x_coord),abs(event.y-y_coord)))
    if abs(event.x-x_coord) < 5 and abs(event.y-y_coord) < 5:
        print('YOU HAVE FOUND THE TREAAASUREE')
        welcome_label.config(text='you have won')

welcome_label = Label(root,text='click on the map to search for treasure')
myframe = Frame(root,bg='yellow',height=200,width=200)

myframe.bind('<Button-1>',guess)

welcome_label.pack()
myframe.pack()

root.mainloop()
```

<a href='#^'>^^^</a>

---

<h4 id='tkguessgamepp'>guess game++</h4>

```python
#guess game++
from tkinter import *
import random

root = Tk()

root.title('yar or nar')

x_coord = random.randint(0,200)
y_coord = random.randint(0,200)
button_counter = 1
counter = 1

def guess(event):
    global counter
    counter += 1
    if counter >= 10:
        global button_counter
        if button_counter == 1:
            button1 = Button(root,text='use parrot')
            button1.bind('<Button-1>',parrot)
            button1.pack()

    print('you clicked at x: {} y: {}. You are {} away from x and {} from y'
          .format(event.x,event.y,abs(event.x-x_coord),abs(event.y-y_coord)))
    if abs(event.x-x_coord) < 5 and abs(event.y-y_coord) < 5:
        print('YOU HAVE FOUND THE TREAAASUREE')
        welcome_label.config(text='you have won!Guess: {}'.format(counter))

def parrot(event):
    print('parrot search')
    global button_counter
    button_counter -= 1
    print('you clicked at x: {} y: {}. You are {} away from x and {} from y'
          .format(event.x, event.y, abs(event.x - x_coord), abs(event.y - y_coord)))
    if abs(event.x - x_coord) < 10 and abs(event.y - y_coord) < 10:
        print('YOU HAVE FOUND THE TREAAASUREE')
        welcome_label.config(text='you have won!Guess: {}'.format(counter))

welcome_label = Label(root,text='click on the map to search for treasure')
myframe = Frame(root,bg='yellow',height=200,width=200)

myframe.bind('<Button-1>',guess)

welcome_label.pack()
myframe.pack()

root.mainloop()
```

<a href='#^'>^^^</a>

---

<h3 id='processing'>Processing</h3>

<a href='#^'>^^^</a>

---




