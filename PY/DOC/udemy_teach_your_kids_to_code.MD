
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD)

---

### Teach your kids to code

---

* [Getting your programming environment](https://github.com/ttltrk/PRG/blob/master/PY/DOC/TYKTC/01/ENV.MD)
* [Turtle graphics in Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/TYKTC/02/TURTLE.MD)
* [Numbers and variables in Python]()

023. Intro to variables
024. Numbers and math in python
025. Python numbers and operators
026. Math in the Python shell
027. Syntax errors: What did you say?
028. Variables in the Python shell
029. Programming with operators
030. The real characters in Python
031. Improving our color spiral with strings

---

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
