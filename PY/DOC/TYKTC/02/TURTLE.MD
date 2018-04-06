
---

### Turtle graphics in Python

---

* [Intro to the turtle graphics in Python]()
* [SquareSpiral: Our first turtle program]()
* [Turtle on a roll: Building a widing spiral]()
* [Loop the loop: Creating a circle spiral]()
* [Adding color to your turtle drawings]()
* [Painting a four color spiral]()
* [Changing background colors]()
* [One variable to rule them all]()

---

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

---
