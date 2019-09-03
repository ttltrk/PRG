
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

```python
def encryption(string):
    morseDict = {"A" : '.-', "B" : '-...', "C" : '-.-.', "D" : "-..", "E" : ".", "F" : "..-.",
        "G" : "--.", "H" : "....", "I" : "..", "J" : ".---", "K" : "-.-", "L" : ".-..", "M" : "--",
        "N" : "-.", "O" : "---", "P" : ".--.", "Q" : "--.-", "R" : ".-.", "S" : "...", "T" : "-",
        "U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-", "Y" : "-.--", "Z" : "--..", "0" : "-----",
        "1" : ".----", "2" : "..--", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....",
        "7" : "--...", "8" : "---..", "9" : "----.",  " " : " "}

    # removeWhiteSpace = (string.replace(" ", ""))
    addWhiteSpace = (" ".join(string))
    searchInDict = [morseDict[x] for x in addWhiteSpace]
    listToString = ''.join(searchInDict)
    return listToString

print(encryption(""))
```
