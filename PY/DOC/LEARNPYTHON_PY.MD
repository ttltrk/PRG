
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD) - [Courses](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/13/COURSES.MD) - [Learnpython](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/13/04/LEARNPY.MD)

---

### Python tutorial

---

01. Learn the Basics

  01.001. Hello World!
  01.002. Variables and Types
  01.003.
  01.004.
  01.005.
  01.006.
  01.007.
  01.008.
  01.009.
  01.010.
  01.011.
  01.012.

02. Data Science Tutorials

03. Advanced Tutorials

04. Other Python Tutorials

05. Contributing Tutorials

=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
01. Learn the Basics
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.001. Hello World
=============================================================================================================

Python is a very simple language, and has a very straightforward syntax. It encourages programmers to program 
without boilerplate (prepared) code. The simplest directive in Python is the "print" directive - 
it simply prints out a line (and also includes a newline, unlike in C).

There are two major Python versions, Python 2 and Python 3. Python 2 and 3 are quite different. 
This tutorial uses Python 3, because it more semantically correct and supports newer features.

For example, one difference between Python 2 and 3 is the print statement. In Python 2, 
the "print" statement is not a function, and therefore it is invoked without parentheses. 
However, in Python 3, it is a function, and must be invoked with parentheses.

To print a string in Python 3, just write:

----------------------------------------------------------------
print("This line will be printed.")
----------------------------------------------------------------

>>>
This line will be printed.
>>>

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Indentation

Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported, 
but the standard indentation requires standard Python code to use four spaces. For example:

----------------------------------------------------------------
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")
----------------------------------------------------------------
    
>>>
x is 1.
>>>

################################################################

----------------------------------------------------------------
"""
Use the "print" command to print the line "Hello, World!".
"""

print("Goodbye, World!")
print("Hello, World!")
----------------------------------------------------------------

>>>
Goodbye, World!
Hello, World!
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.002. 01.002. Variables and Types
=============================================================================================================

Python is completely object oriented, and not "statically typed". You do not need to declare variables before using them, 
or declare their type. Every variable in Python is an object.

This tutorial will go over a few basic types of variables.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Numbers

Python supports two types of numbers - integers and floating point numbers. 
(It also supports complex numbers, which will not be explained in this tutorial).

----------------------------------------------------------------
"""
To define an integer, use the following syntax
"""

myint = 7
print(myint)
----------------------------------------------------------------

>>>
7
>>>

################################################################

----------------------------------------------------------------
"""
To define a floating point number, you may use one of the following notations
"""

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
----------------------------------------------------------------

>>>
7.0
7.0
>>>

################################################################

Strings

----------------------------------------------------------------
"""
Strings are defined either with a single quote or a double quotes.
"""

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
----------------------------------------------------------------

>>>
hello
hello
>>>

################################################################

----------------------------------------------------------------
"""
The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)
"""

mystring = "Don't worry about apostrophes"
print(mystring)
----------------------------------------------------------------

>>>
Don't worry about apostrophes
>>>

################################################################

There are additional variations on defining strings that make it easier to include things such as carriage returns, 
backslashes and Unicode characters. These are beyond the scope of this tutorial, but are covered in the Python documentation.

----------------------------------------------------------------
"""
Simple operators can be executed on numbers and strings
"""

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
----------------------------------------------------------------

>>>
3
hello world
>>>

################################################################

----------------------------------------------------------------
"""
Assignments can be done on more than one variable "simultaneously" on the same line like this
"""

a, b = 3, 4
print(a,b)
----------------------------------------------------------------

>>>
3 4
>>>

################################################################

----------------------------------------------------------------
"""
Mixing operators between numbers and strings is not supported
"""

# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)
----------------------------------------------------------------

>>>
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
    print(one + two + hello)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>

################################################################

----------------------------------------------------------------
"""
The target of this exercise is to create a string, an integer, and a floating point number. 
The string should be named mystring and should contain the word "hello". The floating point number should be named 
myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.
"""

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
----------------------------------------------------------------

>>>
String: hello
Float: 10.000000
Integer: 20
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.003.
=============================================================================================================

=============================================================================================================
01.004.
=============================================================================================================

=============================================================================================================
01.005.
=============================================================================================================

=============================================================================================================
01.006.
=============================================================================================================

=============================================================================================================
01.007.
=============================================================================================================

=============================================================================================================
01.008.
=============================================================================================================

=============================================================================================================
01.009.
=============================================================================================================

=============================================================================================================
01.010.
=============================================================================================================

=============================================================================================================
01.011.
=============================================================================================================

=============================================================================================================
01.012.
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
02.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
03.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
04.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
05.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
