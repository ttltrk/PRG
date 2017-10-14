

### PYTHON - Teach your kids to code

----------------------------------------------------------------------

SECTION 1 - Getting your programming environment

001. Welcome and introduction
002. Installing Python 3.6 and getting started
003. Installing Python 3.6 on WIN
004. Writing your first program in Python 
005. Running and modifying programs in Python
006. NiceHexSpiral.py
007. What you can do now
008. Programming challenges - Practice what you've learned
009. xxx
010. xxx

SECTION 2 - Turtle graphics in Python

011. Intro to the turtle graphics in Python
012. SquareSpiral: Our first turtle program
013. Turtle on a roll: Building a widing spiral
014. Loop the loop: Creating a circle spiral
015. Adding color to your turtle drawings
016. Painting a four color spiral
017. Changing background colors
018. One variable to rule them all
019. xxx
020. xxx
021. xxx
022. xxx

SECTION 3 - Numbers and variables in Python

023. Intro to variables
024. Numbers and math in python
025. Python numbers and operators
026. Math in the Python shell
027. Syntax errors: What did you say?
028. Variables in the Python shell
029. Programming with operators
030. The real characters in Python
031. Improving our color spiral with strings

----------------------------------------------------------------------

### 4. Writing your first program in Python 

```python
# YourName.py

name = input("What's your name?\n")
print("My name is:", name)
```

```
What's your name?
trk
My name is: trk
``` 

----------------------------------------------------------------------

### 5. Running and modifying programs in Python

```python
# YourName.py

name = input("What's your name?\n")
print("My name is:", name, name, name, name, name)
```

```
What's your name?
trk
My name is: trk trk trk trk trk
``` 

----------------------------------------------------------------------

### 6. NiceHexSpiral.py

```python
# NiceHexSpiral.py
import turtle
colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange']

t=turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
```

```
GRAPHICAL OUTPUT
```

----------------------------------------------------------------------

### 8. Programming challenges - Practice what you've learned

```python
# Madlib.py

adjective = input("Please enter an adjective: ")
noun = input("Please enter a noun: ")
verb = input("Please enter a verb ending in -ed: ")

print("Your Madlib: ")
print("The", adjective, noun, verb, "over the lazy brown dog.")
```

```
Please enter an adjective: szo
Please enter a noun: ma
Please enter a verb ending in -ed: deed
Your Madlib: 
The szo ma deed over the lazy brown dog.
```

----------------------------------------------------------------------

### 12. SquareSpiral: Our first turtle program

```python
# SquareSpiral1.py

import turtle
t = turtle.Pen()
t.speed(0)              #speed up
for x in range(100):    #100 times
    t.forward(8*x)		#8* biggest
    t.left(90)			#angle 91
```

```
GRAPHICAL OUTPUT
```

----------------------------------------------------------------------

### 13. Turtle on a roll: Building a widing spiral

```python
# SquareSpiral2.py

import turtle
t = turtle.Pen()
t.speed(0)              #speed up
for x in range(100):    #100 times
    t.forward(8*x)		#8* biggest
    t.left(91)			#angle 91
```

```
GRAPHICAL OUTPUT
```

----------------------------------------------------------------------

### 14. Loop the loop: Creating a circle spiral

```python
# CircleSpiral1.py

import turtle
t = turtle.Pen()
t.speed(0)              #speed up
for x in range(100):	#100 times
    t.circle(x)			#radius x
    t.left(91)			#angle 91
```

```
GRAPHICAL OUTPUT
```

----------------------------------------------------------------------

### 15. Adding color to your turtle drawings

```python
# CircleSpiral2.py

import turtle
t = turtle.Pen()
t.speed(0)              #speed up
t.pencolor("red")		#color red
for x in range(100):	#100 times
    t.circle(x)			#radius x
    t.left(91)			#angle 91
```

```
GRAPHICAL OUTPUT
```

----------------------------------------------------------------------

### 16. Painting a four color spiral

```python
import turtle
t = turtle.Pen()
t.speed(0)              
colors = ["red", "blue", "green", "yellow"]
for x in range(100):
    t.pencolor(colors [x % 4])
    t.circle(x)		
    t.left(60)
```

```
GRAPHICAL OUTPUT
```

----------------------------------------------------------------------

### 17. Changing background colors

```python
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)              
colors = ["red", "blue", "green", "yellow"]
for x in range(100):
    t.pencolor(colors [x % 4])
    t.circle(x)		
    t.left(60)
```

```
GRAPHICAL OUTPUT
```

----------------------------------------------------------------------

### 18. One variable to rule them all

```python
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = 6
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3 /sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/100)
```

```
GRAPHICAL OUTPUT
```

----------------------------------------------------------------------

### 29. Programming with operators

```python
number_of_pizzas = eval(input("how many pizzas do you want?"))
cost_per_pizza = eval(input("how much does each pizza cost?"))

subtotal = number_of_pizzas * cost_per_pizza

tax_rate = 0.08

sales_tax = subtotal * tax_rate
total = sales_tax + subtotal

print("The total cost is $", total)
print("This includes $", subtotal, "for the pizza and")
print("$", sales_tax, "in sales tax")
```

```
how many pizzas do you want?5
how much does each pizza cost?4
The total cost is $ 21.6
This includes $ 20 for the pizza and
$ 1.6 in sales tax
```

----------------------------------------------------------------------

### 30. The real characters in Python

```python
name = input("whats is your name?")

for x in range(100):
    print(name, end = " rules! ")
```

```
whats is your name?trk
trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! trk rules! 
```

----------------------------------------------------------------------

### 31. Improving our color spiral with strings

```python
#SpiralMyName.py

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)              
colors = ["red", "blue", "green", "yellow"]

your_name = turtle.textinput("Enter your name", "What is your name?")

for x in range(100):
    t.pencolor(colors [x % 4])
    t.penup()
    t.forward(x * 4)
    t.pendown()
    t.write(your_name, font = ("Arial", int( (x+4) / 4), "bold"))	
    t.left(92)
```

```
Graph outp
```

----------------------------------------------------------------------
