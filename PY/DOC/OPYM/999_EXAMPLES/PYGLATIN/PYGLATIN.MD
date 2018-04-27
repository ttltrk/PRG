
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD) - [Examples/Apps](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/999_EXAMPLES/EXAM.MD) - [Pyg]()

---

### Pyg Latin

---

```python
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg    
    new_word = new_word[1:len(new_word)]
    print (new_word)
        
else:
    print ('empty')

>>>
Enter a word: def
efday
>>>
```

---
