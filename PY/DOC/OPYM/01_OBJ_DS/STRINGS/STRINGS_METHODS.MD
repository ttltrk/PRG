
Strings Methods
======

[[tutorialspoint.com](https://www.tutorialspoint.com/python/)]

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/STRINGS/STRINGS.MD)

* <a href="#1">isdigit()</a>
* <a href="#2">isalpha()</a>
* <a href="#3">islower()</a>
* <a href="#4">isupper()</a>
* <a href="#5">istitle()</a>
* <a href="#6">isspace()</a>
* <a href="#7">isalnum()</a>
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
str = "123456"; 
print(str.isdigit())

str = "123 456"; 
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

>>>
False
False
True
True
>>>
```

### <h3 id="5">istitle()</h3>

The method istitle() checks whether all the case-based characters in the string following non-casebased letters are uppercase and all other case-based characters are lowercase.

```python
str = "This Is String Example....Wow!!!";
print(str.istitle())

str = "This is string example....wow!!!";
print(str.istitle())

str = "This";
print(str.istitle())

str = "this";
print(str.istitle())

str = "THIS";
print(str.istitle())

>>>
True
False
True
False
False
>>>
```

### <h3 id="6">isspace()</h3>

The method isspace() checks whether the string consists of whitespace.

```python
str = "this is string example....wow!!!";
print(str.isspace())

str = "this";
print(str.isspace())

str = "THIS";
print(str.isspace())

str = "THIS IS IT";
print(str.isspace())

str = " ";
print(str.isspace())

>>>
False
False
False
False
True
>>>
```

### <h3 id="7">isalnum()</h3>

The method isalnum() checks whether the string consists of alphanumeric characters.

```python
str = "this is string example....wow!!!";
print(str.isalnum())

str = "this";
print(str.isalnum())

str = "THISisIT";
print(str.isalnum())

str = "THIS IS IT";
print(str.isalnum())

str = " ";
print(str.isalnum())

>>>
False
True
True
False
False
>>>
```

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
