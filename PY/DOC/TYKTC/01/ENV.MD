
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD) - [TYKTC](https://github.com/ttltrk/PRG/blob/master/PY/DOC/udemy_teach_your_kids_to_code.MD)

---

### Getting your programming environment

---

* [Welcome and introduction]()
* [Installing Python 3.6 and getting started]()
* [Installing Python 3.6 on WIN]()
* [Writing your first program in Python]()
* [Running and modifying programs in Python]()
* [NiceHexSpiral.py]()
* [What you can do now]()
* [Programming challenges - Practice what you've learned]()

---

Writing your first program in Python 

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

---
