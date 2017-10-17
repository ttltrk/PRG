
SOLOLEARN.COM - PYTHON 3 TUTORIAL
======

#### 1. BASIC CONCEPTS
  * What is Python?
  * Your first program
  * Simple operations
  * Floats
  * Other Numerical Operations
  * Strings
  * Simple Input & Output
  * String Operations
  * Type Conversion
  * Variables
  * In-Place Operators
  * Using an Editor
  * MODULE 1 QUIZ

#### 2. CONTROL STRUCTURES

  02.001. Booleans & Comparisons
  02.002. if Statements
  02.003. else Statements
  02.004. Boolean Logic
  02.005. Operator Precedence
  02.006. while Loops
  02.007. Lists
  02.008. List Operations
  02.009. List Functions
  02.010. Range
  02.011. for Loops
  02.012. A Simple Calculator
  ******. MODULE 2 QUIZ

03. FUNCTIONS  & MODULES

  03.001. Code Reuse
  03.002. Functions
  03.003. Function Arguments
  03.004. Returning from Functions
  03.005. Comments & Docstrings
  03.006. Functions as Objects
  03.007. Modules
  03.008. The Standard Library & pip
  ******. MODULE 3 QUIZ

04. EXCEPTIONS & FILES

  04.001. Exceptions
  04.002. Exception Handling
  04.003. finally
  04.004. Raising Exceptions
  04.005. Assertions
  04.006. Opening Files
  04.007. Reading Files
  04.008. Writing Files
  04.009. Working with Files
  ******. MODULE 3 QUIZ

05. MORE TYPES

  05.001. None
  05.002. Dictionaries
  05.003. Dictionary Functions
  05.004. Tuples
  05.005. List Slices
  05.006. List Comprehensions
  05.007. String Formatting
  05.008. Useful Functions
  05.009. Text Analyzer
  ******. MODULE 5 QUIZ

06. FUNCTIONAL PROGRAMMING

  06.001. Introduction
  06.002. Lambdas
  06.003. map & filter
  06.004. Generators
  06.005. Decorators
  06.006. Recursion
  06.007. Sets
  06.008. itertools
  ******. MODULE 6 QUIZ

07. OBJECT-ORIENTED PROGRAMMING

  07.001. Classes
  07.002. Inheritance
  07.003. Magic Methods & Operator Overloading
  07.004. Object Lifecycle
  07.005. Data Hiding
  07.006. Class & Static Methods
  07.007. Properties
  07.008. A Simple Game
  ******. MODULE 7 QUIZ

08. REGULAR EXPRESSIONS

  08.001. Introduction
  08.002. Simple Metacharacters
  08.003. Character Classes
  08.004. More Metacharcters
  08.005. Groups
  08.006. Special Sequences
  08.007. Email Extractions
  ******. MODULE 8 QUIZ

09. PYTHONICNESS & PACKAGING

  09.001. The Zen of Python
  09.002. PEP
  09.003. More on Function Arguments
  09.004. Tuple Unpacking
  09.005. Ternary Operator
  09.006. More on else Statements
  09.007. __main__
  09.008. Major 3rd Party Libraries
  09.009. Packages
  09.010. Packaging for Users
  ******. MODULE 9 QUIZ

=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
01. BASIC CONCEPTS
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.001. What is Python?
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Welcome to Python!

Python is a high-level programming language, with applications in numerous areas, including web programming, 
scripting, scientific computing, and artificial intelligence.

It is very popular and used by organizations such as Google, NASA, the CIA, and Disney.

Python is processed at runtime by the interpreter. There is no need to compile your program before executing it.

################################################################


Python is a:

>>>
Programming language
>>>

################################################################


Welcome to Python!

The three major versions of Python are 1.x, 2.x and 3.x. These are subdivided into minor versions, 
such as 2.7 and 3.3.
Code written for Python 3.x is guaranteed to work in all future versions. 
Both Python Version 2.x and 3.x are used currently. 
This course covers Python 3.x, but it isn't hard to change from one version to another.

Python has several different implementations, written in various languages. 
The version used in this course, CPython, is the most popular by far.

An interpreter is a program that runs scripts written in an interpreted language such as Python.

################################################################


Which of these statements is true?

>>>
CPython is an implementation of Python
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.002. Your first program
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Your First Program

Let's start off by creating a short program that displays "Hello world!".
In Python, we use the print statement to output text:

>>> print('Hello world!')
Hello world!

Congratulations! You have written your first program.

Run, save, and share your Python code on our Code Playground without installing any additional software. 
When using a computer, you will need to download and install Python from www.python.org.
Note the >>> in the code above. They are the prompt symbol of the Python console. Python is an interpreted language, 
which means that each line is executed as it is entered. Python also includes IDLE, the integrated development environment,
which includes tools for writing and debugging entire programs.

################################################################

print('Hi!')

>>>
Hi!
>>>

################################################################

Printing Text

The print statement can also be used to output multiple lines of text.
For Example:
>>> print('Hello world!')
Hello world!
>>> print('Hello world!')
Hello world!
>>> print('Spam and eggs...')
Spam and eggs...

Python code often contains references to the comedy group Monty Python. This is why the words, 
"spam" and "eggs" are often used as placeholder variables in Python where "foo" and "bar"
would be used in other programming languages.

################################################################

print('ni ni ni')

>>>
ni ni ni
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.003. Simple operations
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Simple Operations

Python has the capability of carrying out calculations.
Enter a calculation directly into the Python console, and it will output the answer.

>>> 2 + 2
4
>>> 5 + 4 - 3
6

The spaces around the plus and minus signs here are optional (the code would work without them), 
but they make it easier to read.

################################################################

1 + 2 + 3

>>>
6
>>>

################################################################

Simple Operations

Python also carries out multiplication and division, using an asterisk to indicate multiplication and 
a forward slash to indicate division. 

Use parentheses to determine which operations are performed first.

>>> 2 * (3 + 4)
14
>>> 10 / 2
5.0

Using a single slash to divide numbers produces a decimal (or float, as it is called in programming). 
We'll have more about floats in a later lesson.

################################################################

(4 + 8) / 2

>>>
6.0
>>>

################################################################

Simple Operations

The minus sign indicates a negative number. 
Operations are performed on negative numbers, just as they are on positive ones.
>>> -7
-7
>>> (-7 + 2) * (-4)
20

The plus signs can also be put in front of numbers, but this has no effect, and is mostly used to emphasize 
that a number is positive to increase readability of code.

################################################################

(-5 -1) * 3

>>>
-18
>>>

################################################################

Simple Operations

Dividing by zero in Python produces an error, as no answer can be calculated.

>>> 11 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

In Python, the last line of an error message indicates the error's type.
Read error messages carefully, as they often tell you how to fix a program!

################################################################

(17 + 94) / (-5 + 5)

>>>
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-3-82c284ca2d99> in <module>()
----> 1 (17 + 94) / (-5 + 5 )

ZeroDivisionError: division by zero
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.004. Floats
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Floats

Floats are used in Python to represent numbers that aren't integers. 
Some examples of numbers that are represented as floats are 0.5 and -7.8237591. 
They can be created directly by entering a number with a decimal point, or by using operations such as division on integers. 
Extra zeros at the number's end are ignored.

>>> 3/4
0.75
>>> 9.8765000
9.8765

Computers can't store floats perfectly accurately, in the same way that we can't write down the complete decimal expansion 
of 1/3 (0.3333333333333333...). Keep this in mind, because it often leads to infuriating bugs!

################################################################

Which of these will not be stored as a float?

>>>
7
>>>

################################################################

Floats

As you saw previously, dividing any two integers produces a float. 
A float is also produced by running an operation on two floats, or on a float and an integer.

>>> 8 / 2
4.0
>>> 6 * 7.0
42.0
>>> 4 + 1.65
5.65

A float can be added to an integer, because Python silently converts the integer to a float. 
However, this implicit conversion is the exception rather the rule in Python - 
usually you have to convert values manually if you want to operate on them.

################################################################

1 + 2 + 3 + 4.0 + 5

>>>
15.0
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.005. Other Numerical Operations
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Exponentiation

Besides addition, subtraction, multiplication, and division, Python also supports exponentiation, 
which is the raising of one number to the power of another. This operation is performed using two asterisks.

>>> 2**5
32
>>> 9 ** (1/2)
3.0

################################################################

(1 + 3)  ** 2

>>>
16
>>>

################################################################

Quotient & Remainder

To determine the quotient and remainder of a division, use the floor division and modulo operators, respectively. 
Floor division is done using two forward slashes.
The modulo operator is carried out with a percent symbol (%). 
These operators can be used with both floats and integers.

This code shows that 6 goes into 20 three times, and the remainder when 1.25 is divided by 0.5 is 0.25.

>>> 20 // 6
3
>>> 1.25 % 0.5
0.25

################################################################

7%(5 // 2)

>>>
1
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.006. Strings
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Strings

If you want to use text in Python, you have to use a string. 
A string is created by entering text between two single or double quotation marks. 

When the Python console displays a string, it generally uses single quotes. 
The delimiter used for a string doesn't affect how it behaves in any way.

>>> "Python is fun!"
'Python is fun!'
>>> 'Always look on the bright side of life'
'Always look on the bright side of life'

################################################################

"Hello world"

>>>
'Hello world'
>>>

################################################################

Strings

Some characters can't be directly included in a string. For instance, double quotes can't be directly included 
in a double quote string; this would cause it to end prematurely. 

Characters like these must be escaped by placing a backslash before them. 
Other common characters that must be escaped are newlines and backslashes.
Double quotes only need to be escaped in double quote strings, and the same is true for single quote strings.

>>> 'Brian\'s mother: He\'s not the Messiah. He\'s a very naughty boy!'
'Brian's mother: He's not the Messiah. He's a very naughty boy!'

\n represents a new line.

Backslashes can also be used to escape tabs, arbitrary Unicode characters, 
and various other things that can't be reliably printed. These characters are known as escape characters.

################################################################

"\""

>>>
'"'
>>>

################################################################

Newlines

Python provides an easy way to avoid manually writing "\n" to escape newlines in a string. 
Create a string with three sets of quotes, and newlines that are created by pressing Enter are automatically escaped for you.

>>> """Customer: Good morning.
Owner: Good morning, Sir. Welcome to the National Cheese Emporium."""

'Customer: Good morning.\nOwner: Good morning, Sir. Welcome to the National Cheese Emporium.'

As you can see, the \n was automatically put in the output, where we pressed Enter.

################################################################

"""First line 
second line"""
'First line \n second line'

>>>
'First line \n second line'
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.007. Simple Input & Output
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Output

Usually, programs take input and process it to produce output.
In Python, you can use the print function to produce output. This displays a textual representation of something to the screen.

>>> print(1 + 1)
2
>>> print("Hello\nWorld!")
Hello
World!

When a string is printed, the quotes around it are not displayed.

################################################################

print('print("print")')

>>>
print("print")
>>>

################################################################

Input

To get input from the user in Python, you can use the intuitively named input function. 
The function prompts the user for input, and returns what they enter as a string (with the contents automatically escaped).

>>> input("Enter something please: ")
Enter something please: This is what\nthe user enters!

'This is what\\nthe user enters!'

The print and input functions aren't very useful at the Python console, which automatically does input and output. 
However, they are very useful in actual programs.

################################################################

var = input("Enter a number:")

print(var)

>>>
Enter a number:5
5
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.008. String Operations
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Concatenation

As with integers and floats, strings in Python can be added, using a process called concatenation, 
which can be done on any two strings. 
When concatenating strings, it doesn't matter whether they've been created with single or double quotes.

>>> "Spam" + 'eggs'
'Spameggs'

>>> print("First string" + ", " + "second string")

First string, second string

################################################################

"Hello " + 'world'

>>>
'Hello world'
>>>

################################################################

Concatenation

Even if your strings contain numbers, they are still added as strings rather than integers. 
Adding a string to a number produces an error, as even though they might look similar, they are two different entities.

>>> "2" + "2"
'22'
>>> 1 + '2' + 3 + '4'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

In future lessons, only the final line of error messages will be displayed, 
as it is the only one that gives details about the type of error that has occurred.

################################################################

Which line of code produces an error?

'5' + 6

>>>
TypeError                                 Traceback (most recent call last)
<ipython-input-4-cfde8aeadc63> in <module>()
----> 1 '5' + 6

TypeError: must be str, not int
>>>

################################################################

String Operations

Strings can also be multiplied by integers. This produces a repeated version of the original string. 
The order of the string and the integer doesn't matter, but the string usually comes first.

Strings can't be multiplied by other strings. Strings also can't be multiplied by floats, even if the floats are whole numbers.

>>> print("spam" * 3)
spamspamspam

>>> 4 * '2'
'2222'

>>> '17' * '87'
TypeError: can't multiply sequence by non-int of type 'str'

>>> 'pythonisfun' * 7.0
TypeError: can't multiply sequence by non-int of type 'float'

################################################################

print(3 * '7')

>>>
777
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.009. Type Conversion
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Type Conversion

In Python, it's impossible to complete certain operations due to the types involved. For instance, 
you can't add two strings containing the numbers 2 and 3 together to produce the integer 5, 
as the operation will be performed on strings, making the result '23'.

The solution to this is type conversion. 
In that example, you would use the int function.

>>> "2" + "3"
'23'
>>> int("2") + int("3")
5

In Python, the types we have used so far have been integers, floats, and strings. 
The functions used to convert to these are int, float and str, respectively.

################################################################

int("3" + "4")

>>>
34
>>>

################################################################

Type Conversion

Another example of type conversion is turning user input (which is a string) to numbers (integers or floats), 
to allow for the performance of calculations.

>>> float(input("Enter a number: ")) + float(input("Enter another number: "))
Enter a number: 40
Enter another number: 2
42.0

################################################################

float("210" * int(input("Enter a number:" )))

>>>
Enter a number:2
210210.0
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.010. Variables
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Variables

Variables play a very important role in most programming languages, and Python is no exception. 
A variable allows you to store a value by assigning it to a name, which can be used to refer to the value later in the program. 

To assign a variable, use one equals sign. Unlike most lines of code we've looked at so far, 
it doesn't produce any output at the Python console.

>>> x = 7
>>> print(x)
7
>>> print(x + 3)
10
>>> print(x)
7
Try It Yourself

You can use variables to perform corresponding operations, just as you did with numbers and strings. 
As you can see, the variable stores its value throughout the program.

################################################################

spam = "eggs"
print(spam * 3)

>>>
eggseggseggs
>>>

################################################################

Variables

Variables can be reassigned as many times as you want, in order to change their value. 
In Python, variables don't have specific types, so you can assign a string to a variable, 
and later assign an integer to the same variable.

>>> x = 123.456
>>> print(x)
123.456
>>> x = "This is a string"
>>> print(x + "!")

This is a string!

################################################################

x = 5
y = 7

print(x + y)

>>>
12
>>>

################################################################

Variable Names

Certain restrictions apply in regard to the characters that may be used in Python variable names. 
The only characters that are allowed are letters, numbers, and underscores. Also, they can't start with numbers.
Not following these rules results in errors.

>>> this_is_a_normal_name = 7

>>> 123abc = 7
SyntaxError: invalid syntax

>>> spaces are not allowed
SyntaxError: invalid syntax

Python is a case sensitive programming language. Thus, Lastname and lastname are two different variable names in Python.

################################################################

Which of these is a valid variable name in Python?

>>>
A_VARIABLE_NAME
>>>

################################################################

Variables

Trying to reference a variable you haven't assigned to causes an error. 
You can use the del statement to remove a variable, which means the reference from the name to the value is deleted, 
and trying to use the variable causes an error. Deleted variables can be reassigned to later as normal.

>>> foo = "a string"
>>> foo
'a string'
>>> bar
NameError: name 'bar' is not defined
>>> del foo
>>> foo
NameError: name 'foo' is not defined

You can also take the value of the variable from the user input.
>>> foo = input("Enter a number: ")
Enter a number: 7
>>> print(foo)
7

The variables foo and bar are called metasyntactic variables, meaning that they are used as placeholder names in 
example code to demonstrate something.

################################################################

spam = 2
eggs = 3
del spam
eggs = 4
spam = 5

print(spam * eggs)

>>>
20
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.011. In-Place Operators
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

In-Place Operators

In-place operators allow you to write code like 'x = x + 3' more concisely, as 'x += 3'. 
The same thing is possible with other operators such as -, *, / and % as well.

>>> x = 2
>>> print(x)
2
>>> x += 3
>>> print(x)
5

################################################################

x = 4
x *= 3

print(x)

>>>
12
>>>

################################################################

In-Place Operators

These operators can be used on types other than numbers, as well, such as strings.
>>> x = "spam"
>>> print(x)
spam

>>> x += "eggs"
>>> print(x)
spameggs

Many other languages have special operators such as '++' as a shortcut for 'x += 1'. Python does not have these.

################################################################

x = "a"
x *= 3

print(x)

>>>
aaa
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.012. Using an Editor
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Using an Editor

So far, we've only used Python with the console, entering and running one line of code at a time. 
Actual programs are created differently; many lines of code are written in a file, 
and then executed with the Python interpreter. 

In IDLE, this can be done by creating a new file, entering some code, saving the file, and running it. 
This can be done either with the menus or with the keyboard shortcuts Ctrl-N, Ctrl-S and F5. 

Each line of code in the file is interpreted as though you entered it one line at a time at the console.

x = 7
x = x + 2
print(x)

Python source files have an extension of .py
You can run, save, and share your Python codes on our Code Playground, without installing any additional software.
Reference this lesson if you need to install the software on your computer.

################################################################

Which lines are executed when a Python file is run?

>>>
Every line
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
******. MODULE 1 QUIZ
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

spam = "7"
spam = spam + "0"
eggs = int(spam) + 3

print(float(eggs))

>>>
73.0
>>>

################################################################

word = input("Enter a word: ")

print(word + ' shop')

>>>
Enter a word: cheese
cheese shop
>>>

################################################################

x = 5
y = x + 3
y = int(str(y) + "2")

print(y)

>>>
82
>>>

################################################################

x = 4
x += 5

print(x)

>>>
9
>>>

################################################################

x = 3
num = 17

print(num % x)

>>>
2
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
02. CONTROL STRUCTURES
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
02.001. Booleans & Comparisons
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Booleans

Another type in Python is the Boolean type. There are two Boolean values: True and False.
They can be created by comparing values, for instance by using the equal operator ==.

>>> my_boolean = True
>>> my_boolean
True
>>> 2 == 3
False
>>> "hello" == "hello"
True

Be careful not to confuse assignment (one equals sign) with comparison (two equals signs).

################################################################

What are the two Boolean values in Python?

>>>
True and False
>>>

################################################################

Comparison

Another comparison operator, the not equal operator (!=), evaluates to True if the items being compared aren't equal,
and False if they are.

>>> 1 != 1
False
>>> "eleven" != "seven"
True
>>> 2 != 10
True

################################################################

What is the output of this code?
>>> 7 != 8

>>>
True
>>>

################################################################

Comparison

Python also has operators that determine whether one number (float or integer) is greater than or smaller than another. 
These operators are > and < respectively.

>>> 7 > 5
True
>>> 10 < 10
False

################################################################

What is the output of this code?
>>> 7 > 7.0

>>>
False
>>>

################################################################

Comparison

The greater than or equal to, and smaller than or equal to operators are >= and <=.
They are the same as the strict greater than and smaller than operators, except that they return True when comparing equal numbers.

>>> 7 <= 8
True
>>> 9 >= 9.0
True

Greater than and smaller than operators can also be used to compare strings lexicographically 
(the alphabetical order of words is based on the alphabetical order of their component letters).

################################################################

What is the output of this code?
>>> 8.7 <= 8.70

>>>
True
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
02.002. if Statements
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

if Statements

You can use if statements to run code if a certain condition holds. 
If an expression evaluates to True, some statements are carried out. Otherwise, they aren't carried out. 
An if statement looks like this:

if expression:
   statements

Python uses indentation (white space at the beginning of a line) to delimit blocks of code. 
Other languages, such as C, use curly braces to accomplish this, but in Python indentation is mandatory; 
programs won't work without it. As you can see, the statements in the if should be indented.

################################################################

What part of an if statement should be indented?

>>>
The statements within it
>>>

################################################################

if Statements

Here is an example if statement:

if 10 > 5:
   print("10 greater than 5")

print("Program ended")

The expression determines whether 10 is greater than five. Since it is, the indented statement runs, 
and "10 greater than 5" is output. Then, the unindented statement, which is not part of the if statement, 
is run, and "Program ended" is displayed. 

Result:

>>>
10 greater than 5
Program ended
>>>

Notice the colon at the end of the expression in the if statement.
As the program contains multiple lines of code, you should create it as a separate file and run it.

################################################################

What is the output of this code?

spam = 7
if spam > 5:
   print("five")
if spam > 8:
   print("eight")
   
>>>
five
>>>
   
################################################################

if Statements

To perform more complex checks, if statements can be nested, one inside the other.
This means that the inner if statement is the statement part of the outer one. 
This is one way to see whether multiple conditions are satisfied. 

For example:

num = 12
if num > 5:
   print("Bigger than 5")
   if num <=47:
      print("Between 5 and 47")

Result:

>>>
Bigger than 5
Between 5 and 47
>>>

################################################################

What is the output of this code?

num = 7
if num > 3:
   print("3")
   if num < 5:
      print("5")
      if num ==7:
         print("7")

>>>
3
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
02.003. else Statements
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

else Statements

An else statement follows an if statement, and contains code that is called when the if statement evaluates to False. 
As with if statements, the code inside the block should be indented.

x = 4
if x == 5:
   print("Yes")
else:
   print("No")

Result:
>>> 
No
>>>

################################################################

What is the result of this code?

if 1 + 1 == 2:
   if 2 * 2 == 8:
      print("if")
   else:
      print("else")
      
>>>
else
>>>

################################################################

else Statements

You can chain if and else statements to determine which option in a series of possibilities is true.

For example:

num = 7
if num == 5:
  print("Number is 5")
else: 
  if num == 11:
    print("Number is 11")
  else:
    if num == 7:
      print("Number is 7")
    else: 
      print("Number isn't 5, 11 or 7")

Result:

>>>
Number is 7
>>> 

################################################################

Fill in the blanks to compare the variables and output the corresponding text:

x = 10
y = 20
  
if x > y:
   print("if statement")  
else:
   print("else statement")
   
>>>
else statement
>>>

################################################################

elif Statements

The elif (short for else if) statement is a shortcut to use when chaining if and else statements.
A series of if elif statements can have a final else block, which is called if none of the if or elif expressions is True.

For example:

num = 7
if num == 5:
   print("Number is 5")
elif num == 11:
   print("Number is 11")
elif num == 7:
   print("Number is 7")
else:
   print("Number isn't 5, 11 or 7")

Result:

>>>
Number is 7
>>>

In other programming languages, equivalents to the elif statement have varying names, including else if, elseif or elsif.

################################################################

A shorter option for an "else if" statement is:

>>>
elif
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
02.004. Boolean Logic
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Boolean Logic

Boolean logic is used to make more complicated conditions for if statements that rely on more than one condition. 
Python's Boolean operators are and, or, and not. 
The and operator takes two arguments, and evaluates as True if, and only if, both of its arguments are True. 
Otherwise, it evaluates to False.

>>> 1 == 1 and 2 == 2
True
>>> 1 == 1 and 2 == 3
False
>>> 1 != 1 and 2 == 2
False
>>> 2 < 1 and 3 >  6
False

Python uses words for its Boolean operators, whereas most other languages use symbols such as &&, || and !.

################################################################

What is the result of this code?

if (1 == 1) and (2 + 2 > 3):
  print("true")
else:
  print("false")

>>>
true
>>>

################################################################

Boolean Or

The or operator also takes two arguments. It evaluates to True if either (or both) of its arguments are True, 
and False if both arguments are False.

>>> 1 == 1 or 2 == 2
True
>>> 1 == 1 or 2 == 3
True
>>> 1 != 1 or 2 == 2
True
>>> 2 < 1 or 3 >  6
False

################################################################

Fill in the blanks to print "Welcome".

age = 15
money = 500

if age > 18 or money > 100:
   print("Welcome")
   
>>>
Welcome
>>>

################################################################

Boolean Not

Unlike other operators we've seen so far, not only takes one argument, and inverts it. 
The result of not True is False, and not False goes to True.

>>> not 1 == 1
False
>>> not 1 > 7
True

You can chain multiple conditional statements in an if statement using the Boolean operators.

################################################################

What is the result of this code?

if not True:
   print("1")
elif not (1 + 1 == 3):
   print("2")
else:
   print("3")
   
>>>
2
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
02.005. Operator Precedence
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Operator Precedence

Operator precedence is a very important concept in programming. It is an extension of the mathematical idea 
of order of operations (multiplication being performed before addition, etc.) to include other operators, 
such as those in Boolean logic. 

The below code shows that == has a higher precedence than or:

>>> False == False or True
True
>>> False == (False or True)
False
>>> (False == False) or True
True

Python's order of operations is the same as that of normal mathematics: parentheses first, 
then exponentiation, then multiplication/division, and then addition/subtraction.

################################################################

What is the result of this code?

if 1 + 1 * 3 == 6:
   print("Yes")
else:
   print("No")

>>>
No
>>>

################################################################

Operator Precedence

The following table lists all of Python's operators, from highest precedence to lowest.

OP            DESC

**            Exponentiation (raise to the power)
~+-           Complement, unary + and minus (method names for the last two are +@ and -@) 
*/%//         multiply, divide, modulo and floor division
+ -           addition and subtraction
>> <<         right and left bitwise shift
&             Bitwise 'AND'
^ |           Bitwise exclusive 'OR' and regular 'OR'
<= <> >=      Comparison operators
<> == !=      Equality operators
= %= /= //=   Assignment oerators
-= += *= **=
is is not     Identity operators
in not in     Membership operators
not or and    Logical operators



################################################################

What is the result of this code?

x = 4
y= 2

if not 1 + 1 == y or x == 4 and 7 == 8:
  print("Yes")
elif x > y:
  print("No")
  
>>>
No
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
02.006. while Loops
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

while Loops

An if statement is run once if its condition evaluates to True, and never if it evaluates to False. 
A while statement is similar, except that it can be run more than once. The statements inside it are repeatedly executed, 
as long as the condition holds. Once it evaluates to False, the next section of code is executed. 
Below is a while loop containing a variable that counts up from 1 to 5, at which point the loop terminates.

i = 1
while i <=5:
   print(i)
   i = i + 1

print("Finished!")

Result:

>>>
1
2
3
4
5
Finished!
>>>

The code in the body of a while loop is executed repeatedly. This is called iteration.

################################################################

How many numbers does this code print?

>>>
4
>>>

i = 3
while i>=0:
   print(i)
   i = i - 1
   
>>>
3
2
1
0
>>>
   
################################################################

while Loops

The infinite loop is a special kind of while loop; it never stops running. Its condition always remains True. 

An example of an infinite loop:

while 1==1:
  print("In the loop") 

This program would indefinitely print "In the loop". 
You can stop the program's execution by using the Ctrl-C shortcut or by closing the program.

################################################################

Fill in the blanks to create a loop that increments the value of x by 2 and prints the even values.

x = 0
while x <=20:
    print(x)
    x += 2
    
>>>
0
2
4
6
8
10
12
14
16
18
20
>>>

################################################################

break

To end a while loop prematurely, the break statement can be used. 
When encountered inside a loop, the break statement causes the loop to finish immediately.

i = 0
while 1==1:
  print(i)
  i = i + 1
  if i >= 5:
    print("Breaking")
    break

print("Finished")

Result:

>>>
0
1
2
3
4
Breaking
Finished
>>>

Using the break statement outside of a loop causes an error.

################################################################

How many numbers does this code print?

>>>
3
>>>

i = 5
while True:
  print(i)
  i = i - 1
  if i <= 2:
    break

>>>
5
4
3
>>>

################################################################

continue

Another statement that can be used within loops is continue. 
Unlike break, continue jumps back to the top of the loop, rather than stopping it.

i = 0
while True:
   i = i +1
   if i == 2:
      print("Skipping 2")
      continue
   if i == 5:
      print("Breaking")
      break
   print(i)

print("Finished")

Result:

>>>
1
Skipping 2
3
4
Breaking
Finished
>>>

Basically, the continue statement stops the current iteration and continues with the next one.
Using the continue statement outside of a loop causes an error.

################################################################

Which statement ends the current iteration and continues with the next one?

>>>
continue
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
02.007. Lists
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Lists

Lists are another type of object in Python. They are used to store an indexed list of items. 
A list is created using square brackets with commas separating items.
The certain item in the list can be accessed by using its index in square brackets.

For example:

words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

Result:

>>>
Hello
world
!
>>>

The first list item's index is 0, rather than 1, as might be expected.

################################################################

What is the result of this code?

nums = [5, 4, 3, 2, 1]
print(nums[1])

>>>
4
>>>


################################################################

Lists

An empty list is created with an empty pair of square brackets.

empty_list = []
print(empty_list)

Result:

>>>
[]
>>>

Most of the time, a comma won't follow the last item in a list. However, 
it is perfectly valid to place one there, and it is encouraged in some cases.

################################################################

How many items are in this list?
[2,]

a = [2,]
print(len(a))

>>>
1
>>>

################################################################

Lists

Typically, a list will contain items of a single item type, but it is also possible to include several different types. 
Lists can also be nested within other lists.

number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

Result:

>>>
0
[1, 2, 3]
3
>>>

Lists of lists are often used to represent 2D grids, as Python lacks the multidimensional arrays that would be used 
for this in other languages.

################################################################

Fill in the blanks to create a list and print its 3rd element.

list = [42, 55, 67]
print(list[2])

>>>
67
>>>

################################################################

Lists

Indexing out of the bounds of possible list values causes an IndexError. 
Some types, such as strings, can be indexed like lists. Indexing strings behaves as though you are 
indexing a list containing each character in the string. 

For other types, such as integers, indexing them isn't possible, and it causes a TypeError.

str = "Hello world!"
print(str[6])

Result:

>>>
w
>>>

################################################################

Which line of code will cause an error?

num = [5, 4, 3, [2], 1]
print(num[0])
print(num[3][0])
print(num[5])

>>>
Line 4
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
02.008. List Operations
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

List Operations

The item at a certain index in a list can be reassigned.

For example:

nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

Result:

>>>
[7, 7, 5, 7, 7]
>>>

################################################################

What is the result of this code?

nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3])

>>>
2
>>>

################################################################

List Operations

Lists can be added and multiplied in the same way as strings.

For example:

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

Result:

>>>
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>>

Lists and strings are similar in many ways - strings can be thought of as lists of characters that can't be changed.

################################################################

Fill in the blanks to create a list, reassign its 2nd element and print the whole list.

nums = [33, 42, 56]
nums[1] = 22
print(nums)

################################################################

List Operations

To check if an item is in a list, the in operator can be used. 
It returns True if the item occurs one or more times in the list, and False if it doesn't.

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

Result:

>>>
True
True
False
>>>

The in operator is also used to determine whether or not a string is a substring of another string.

################################################################

What is the result of this code?

nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
  print(nums[3])
else:
  print(nums[4])
  
>>>
7
>>>

################################################################

List Operations

To check if an item is not in a list, you can use the not operator in one of the following ways:

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)
Try It Yourself

Result:

>>>
True
True
False
False
>>>

################################################################

Fill in the blanks to print "Yes" if the list contains 'z':

letters = ['a', 'b', 'z']
if "z" in letters:
  print("Yes")
  
>>>
Yes
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
02.009. List Functions
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

List Functions

Another way of altering lists is using the append method. This adds an item to the end of an existing list.

nums = [1, 2, 3]
nums.append(4)
print(nums)

>>>
[1, 2, 3, 4]
>>>

The dot before append is there because it is a method of the list class. Methods will be explained in a later lesson.

################################################################

What is the result of this code?

words = ["hello"]
words.append("world")
print(words[1])

>>>
world
>>>

################################################################

List Functions

To get the number of items in a list, you can use the len function.

nums = [1, 3, 5, 2, 4]
print(len(nums))

Result:

>>>
5
>>>

Unlike append, len is a normal function, rather than a method. This means it is written before the list it is being called on, 
without a dot.

################################################################

What is the result of this code?

letters = ["a", "b", "c"]
letters.append("d")
print(len(letters))

>>>
4
>>>

################################################################

List Functions

The insert method is similar to append, except that it allows you to insert a new item at any position in the list, 
as opposed to just at the end.

words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)

Result:

>>>
['Python', 'is', 'fun']
>>>

################################################################

What is the result of this code?

nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(len(nums))

>>>
7
>>>

################################################################

List Functions

The index method finds the first occurrence of a list item and returns its index.
If the item isn't in the list, it raises a ValueError.

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('z'))

Result:

>>>
2
0
ValueError: 'z' is not in list
>>> 

There are a few more useful functions and methods for lists. 
max(list): Returns the list item with the maximum value
min(list): Returns the list item with minimum value
list.count(obj): Returns a count of how many times an item occurs in a list
list.remove(obj): Removes an object from a list
list.reverse(): Reverses objects in a list

################################################################

Drag and drop from the options below to add 'z' to the end of the list and print the list's length.

list.append ('z')
print(len(list))

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
02.010. Range
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Range

The range function creates a sequential list of numbers.
The code below generates a list containing all of the integers, up to 10.

numbers = list(range(10))
print(numbers)

Result:
>>>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>

The call to list is necessary because range by itself creates a range object, 
and this must be converted to a list if you want to use it as one.

################################################################

What is the result of this code?

nums = list(range(5))
print(nums[0])
print(nums[1])
print(nums[4])

>>>
0
1
4
>>>

################################################################

Range

If range is called with one argument, it produces an object with values from 0 to that argument. 
If it is called with two arguments, it produces values from the first to the second.

For example:

numbers = list(range(3, 8))
print(numbers)

print(range(20) == range(0, 20))

Result:

>>>
[3, 4, 5, 6, 7]

True
>>>

################################################################

What is the result of this code?

nums = list(range(5, 8))
print(len(nums))

>>>
3
>>>

################################################################

Range

range can have a third argument, which determines the interval of the sequence produced. This third argument must be an integer.

numbers = list(range(5, 20, 2))
print(numbers)

Result:

>>>
[5, 7, 9, 11, 13, 15, 17, 19]
>>>

################################################################

What is the result of this code?

nums = list(range(3, 15, 3))
print(nums[2])

>>>
9
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
02.011. for Loops
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Loops

Sometimes, you need to perform code on each item in a list. This is called iteration, 
and it can be accomplished with a while loop and a counter variable.

For example:

words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

while counter <= max_index:
   word = words[counter]
   print(word + "!")
   counter = counter + 1 

Result:

>>>
hello!
world!
spam!
eggs!
>>>

The example above iterates through all items in the list, accesses them using their indices, and prints them with exclamation marks.

################################################################

Which construct can be used to iterate through a list?

>>>
Loops
>>>

################################################################

for Loop

Iterating through a list using a while loop requires quite a lot of code, 
so Python provides the for loop as a shortcut that accomplishes the same thing.

The same code from the previous example can be written with a for loop, as follows:

words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")

Result:

>>>
hello!
world!
spam!
eggs!
>>>

The for loop in Python is like the foreach loop in other languages.

################################################################

Fill in the blanks to create a valid for loop.

letters = ['a', 'b', 'c']
for l in letters:
   print(l)
   
>>>
a
b
c
>>>

################################################################

for Loops

The for loop is commonly used to repeat some code a certain number of times. This is done by combining for loops with range objects.

for i in range(5):
  print("hello!")

Result:

>>>
hello!
hello!
hello!
hello!
hello!
>>>

You don't need to call list on the range object when it is used in a for loop, 
because it isn't being indexed, so a list isn't required.

################################################################

Fill in the blanks to create a for loop that prints only the even values in the range:

for i in range(0, 20, 2):
  print(i)
  
>>>
0
2
4
6
8
10
12
14
16
18
>>>
   
################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
02.012. A Simple Calculator
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

Creating a Calculator

This lesson is about an example Python project: a simple calculator. 
Each part explains a different section of the program. 
The first section is the overall menu. This keeps on accepting user input until the user enters "quit", so a while loop is used.

while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")

   if user_input == "quit":
      break
   elif user_input == "add":
      ...
   elif user_input == "subtract":
      ...
   elif user_input == "multiply":
      ...
   elif user_input == "divide":
      ...
   else:
      print("Unknown input")

The code above is the starting point for our program. It accepts user input, and compares it to the options in the if/elif statements.
The break statement is used to stop the while loop, in case the user inputs "quit".

################################################################

If we were to replace the break statement in the code with a 'continue', what would happen?

>>>
It would run forever
>>>

################################################################

Creating a Calculator

The next part of the program is getting the numbers the user wants to do something with. 
The code below shows this for the addition section of the calculator. Similar code would have to be written for the other sections.

elif user_input == "add":
  num1 = float(input("Enter a number: "))
  num2 = float(input("Enter another number: "))

Now, when the user inputs "add", the program prompts to enter two numbers, and stores them in the corresponding variables.
As it is, this code crashes if the user enters a non-numeric input when prompted to enter a number. 
We will look at fixing problems like this in a later module.

################################################################

Why are the calls to float necessary in the code?

>>>
To convert user input to a float
>>>

################################################################

Creating a Calculator

The final part of the program processes user input and displays it. 
The code for the addition part is shown here.

elif user_input == "add":
  num1 = float(input("Enter a number: "))
  num2 = float(input("Enter another number: "))
  result = str(num1 + num2)
  print("The answer is " + result)

We now have a working program that prompts for user input, and then calculates and prints the sum of the input.
Similar code would have to be written for the other branches (for subtraction, multiplication and division).
The output line could be put outside the if statements to omit repetition of code.

################################################################

Fill in the blanks to make the calculator work for multiplication.

elif user_input == "multiply":
  num1 = float(input("Enter a number: "))
  num2 = float(input("Enter another number: "))
  result = str(num1 * num2)
  print("The answer is " + result)

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
******. MODULE 2 QUIZ
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

What is the output of this code?

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])

>>>
8
>>>

################################################################

What does this code do?

for i in range(10):
  if not i % 2 == 0:
    print(i+1)
    
>>> 
2
4
6
8
10
>>>

################################################################

How many lines will this code print?

while False:
  print("Looping...")
  
>>>
0
>>>

################################################################

Fill in the blanks to print the first element of the list, if it contains even number of elements.

list = [1, 2, 3, 4]
if len(list) % 2 == 0:
  print(list[0])
  
>>>
1
>>>

################################################################

What does this code output?

letters = ['x', 'y', 'z']
letters.insert(1, 'w')
print(letters[2])

>>>
y
>>>

################################################################

Fill in the blanks to iterate over the list using a for loop and print its values.

list = [1, 2, 3]
  
for var in list:
  print(var)
  
>>>
1
2
3
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
03. FUNCTIONS  & MODULES
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
03.001. Code Reuse
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
03.002. Functions
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
03.003. Function Arguments
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
03.004. Returning from Functions
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
03.005. Comments & Docstrings
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
03.006. Functions as Objects
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
03.007. Modules
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
03.008. The Standard Library & pip
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
******. MODULE 3 QUIZ
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
04. EXCEPTIONS & FILES
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
04.001. Exceptions
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

################################################################

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
04.002. Exception Handling
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
04.003. finally
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
04.004. Raising Exceptions
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
04.005. Assertions
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
04.006. Opening Files
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
04.007. Reading Files
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
04.008. Writing Files
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
04.009. Working with Files
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
******. MODULE 3 QUIZ
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
05. MORE TYPES
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
05.001. None
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
05.002. Dictionaries
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
05.003. Dictionary Functions
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
05.004. Tuples
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
05.005. List Slices
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
05.006. List Comprehensions
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
05.007. String Formatting
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
05.008. Useful Functions
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
05.009. Text Analyzer
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
******. MODULE 5 QUIZ
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
06. FUNCTIONAL PROGRAMMING
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

-------------------------------------------------------------
06.001. Introduction
-------------------------------------------------------------

-------------------------------------------------------------
06.002. Lambdas
-------------------------------------------------------------

-------------------------------------------------------------
06.003. map & filter
-------------------------------------------------------------

-------------------------------------------------------------
06.004. Generators
-------------------------------------------------------------

-------------------------------------------------------------
06.005. Decorators
-------------------------------------------------------------

-------------------------------------------------------------
06.006. Recursion
-------------------------------------------------------------

-------------------------------------------------------------
06.007. Sets
-------------------------------------------------------------

-------------------------------------------------------------
06.008. itertools
-------------------------------------------------------------

-------------------------------------------------------------
******. MODULE 6 QUIZ
-------------------------------------------------------------

--------------------

-----------------------------------------------------------------------------------------
07. OBJECT-ORIENTED PROGRAMMING
-----------------------------------------------------------------------------------------

-------------------------------------------------------------
07.001. Classes
-------------------------------------------------------------

-------------------------------------------------------------
07.002. Inheritance
-------------------------------------------------------------

-------------------------------------------------------------
07.003. Magic Methods & Operator Overloading
-------------------------------------------------------------

-------------------------------------------------------------
07.004. Object Lifecycle
-------------------------------------------------------------

-------------------------------------------------------------
07.005. Data Hiding
-------------------------------------------------------------

-------------------------------------------------------------
07.006. Class & Static Methods
-------------------------------------------------------------

-------------------------------------------------------------
07.007. Properties
-------------------------------------------------------------

-------------------------------------------------------------
07.008. A Simple Game
-------------------------------------------------------------

-------------------------------------------------------------
******. MODULE 7 QUIZ
-------------------------------------------------------------

--------------------

-----------------------------------------------------------------------------------------
08. REGULAR EXPRESSIONS
-----------------------------------------------------------------------------------------

-------------------------------------------------------------
08.001. Introduction
-------------------------------------------------------------

-------------------------------------------------------------
08.002. Simple Metacharacters
-------------------------------------------------------------

-------------------------------------------------------------
08.003. Character Classes
-------------------------------------------------------------

-------------------------------------------------------------
08.004. More Metacharcters
-------------------------------------------------------------

-------------------------------------------------------------
08.005. Groups
-------------------------------------------------------------

-------------------------------------------------------------
08.006. Special Sequences
-------------------------------------------------------------

-------------------------------------------------------------
08.007. Email Extractions
-------------------------------------------------------------

-------------------------------------------------------------
******. MODULE 8 QUIZ
-------------------------------------------------------------

--------------------

-----------------------------------------------------------------------------------------
09. PYTHONICNESS & PACKAGING
-----------------------------------------------------------------------------------------

-------------------------------------------------------------
09.001. The Zen of Python
-------------------------------------------------------------

-------------------------------------------------------------
09.002. PEP
-------------------------------------------------------------

-------------------------------------------------------------
09.003. More on Function Arguments
-------------------------------------------------------------

-------------------------------------------------------------
09.004. Tuple Unpacking
-------------------------------------------------------------

-------------------------------------------------------------
09.005. Ternary Operator
-------------------------------------------------------------
09.006. More on else Statements
-------------------------------------------------------------

-------------------------------------------------------------
09.007. __main__
-------------------------------------------------------------

-------------------------------------------------------------
09.008. Major 3rd Party Libraries
-------------------------------------------------------------

-------------------------------------------------------------
09.009. Packages
-------------------------------------------------------------

-------------------------------------------------------------
09.010. Packaging for Users
-------------------------------------------------------------

-------------------------------------------------------------
******. MODULE 9 QUIZ
-------------------------------------------------------------

--------------------

-----------------------------------------------------------------------------------------
