
Strings Methods
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/STRINGS/STRINGS.MD)

* <a href="#1">isdigit()</a>
* <a href="#2">isalpha()</a>
* <a href="#3">islower()</a>
* <a href="#4">isupper()</a>
* istitle()
* isspace()
* str.isalnum()
* count()
* len()
* title()
* capitalize()
* lower()
* upper()
* swapcase()
* center()
* zfill()
* strip()
* expandtabs()
* translate()
* replace()
* partition()
* endswith()
* startswith()
* find()
* index()
* split()
* rsplit()
* join()
* splitlines()

### <h3 id="1">isdigit()</h3>

This method returns true if all characters in the string are digits and there is at least one character, false otherwise.

```python
str = "123456";  # Only digit in this string
print(str.isdigit())

str = "123 456";  # Only digit in this string
print(str.isdigit())

str = "this is string example....wow!!!";
print(str.isdigit())

str = "this";
print(str.isdigit())

>>>
True
False
False
False
>>>   
```

### <h3 id="2">isalpha()</h3>

The method isalpha() checks whether the string consists of alphabetic characters only.

```python
str = "123456";  
print(str.isalpha())

str = "123 456";  
print(str.isalpha())

str = "this is string example....wow!!!";
print(str.isalpha())

str = "this";
print(str.isalpha())

>>>
False
False
False
True
>>>
```

### <h3 id="3">islower()</h3>

The method islower() checks whether all the case-based characters (letters) of the string are lowercase.

```python
str = "this is string example....wow!!!";
print(str.islower())

str = "this";
print(str.islower())

str = "THIS";
print(str.islower())

str = "THIS IS IT";
print(str.islower())

>>>
True
True
False
False
>>>
```

### <h3 id="4">isupper()</h3>

The method isupper() checks whether all the case-based characters (letters) of the string are uppercase.

```python
str = "this is string example....wow!!!";
print(str.isupper())

str = "this";
print(str.isupper())

str = "THIS";
print(str.isupper())

str = "THIS IS IT";
print(str.isupper())
```

* istitle()
* isspace()
* str.isalnum()
* count()
* len()
* title()
* capitalize()
* lower()
* upper()
* swapcase()
* center()
* zfill()
* strip()
* expandtabs()
* translate()
* replace()
* partition()
* endswith()
* startswith()
* find()
* index()
* split()
* rsplit()
* join()
* splitlines()
