
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD)

---

### Python OOP

---

```python
Class Dog(object):

    #Class Object Attribute
    species = "mammal"

    def __init__(self, breed, name, color):
        self.breed = breed
        self.name = name
        self.color = color

sam = Dog(breed="Lab", name = "Sammy", color = "black")

george = Dog(breed="pit", name = "George", color = "white")

print(sam.name, george.name)
print("Sam species = " + sam.species)
print("Sam color = " + sam.color)
print("George color = " + george.color)

>>>
('Sammy', 'George')
Sam species = mammal
Sam color = black
George color = white
>>>
```

---

[JV](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/OOP/OOP.MD)

---
