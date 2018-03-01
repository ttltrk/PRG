
Strings Methods
======

[tutorialspoint.com](https://www.tutorialspoint.com/python/)

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/STRINGS/STRINGS.MD)

---

* <a href="#1">isdigit()</a>
* <a href="#2">isalpha()</a>
* <a href="#3">islower()</a>
* <a href="#4">isupper()</a>
* <a href="#5">istitle()</a>
* <a href="#6">isspace()</a>
* <a href="#7">isalnum()</a>
* <a href="#8">count()</a>
* <a href="#9">len()</a>
* <a href="#10">title()</a>
* <a href="#11">capitalize()</a>
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

---

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

### <h3 id="8">count()</h3>

The method count() returns the number of occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.

count() parameters
  * sub − This is the substring to be searched.
  * start − Search starts from this index. First character starts from 0 index. By default search starts from 0 index.
  * end − Search ends from this index. First character starts from 0 index. By default search ends at the last index.
  
```python
string = "Python is awesome, isn't it?"
substring = "is"

count = string.count(substring)

print("The count is:", count)

>>>
The count is: 2
>>>
```

```python
string = "it is it and just it"
substring = "it"

count = string.count(substring)

print("The count is:", count)

>>>
The count is: 3
>>>
```

### <h3 id="9">len()</h3>

The method len() returns the length of the string.

```python
str = "this is string example....wow!!!";
print("Length of the string: ", len(str))

str = "this is it";
print("Length of the string: ", len(str))

str = "yo";
print("Length of the string: ", len(str))

str = " ";
print("Length of the string: ", len(str))

str = "";
print("Length of the string: ", len(str))

>>>
Length of the string:  32
Length of the string:  10
Length of the string:  2
Length of the string:  1
Length of the string:  0
>>>
```

### <h3 id="10">title()</h3>

The method title() returns a copy of the string in which first characters of all the words are capitalized.

```python
str = "this is string example....wow!!!";
print(str.title())

str = "this is it";
print(str.title())

str = "yo";
print(str.title())

>>>
This Is String Example....Wow!!!
This Is It
Yo
>>>
```

### <h3 id="11">capitalize()</h3>

It returns a copy of the string with only its first character capitalized.

```python
str = "This";
print("str.capitalize() : ", str.capitalize())

str = "this";
print("str.capitalize() : ", str.capitalize())

>>>
str.capitalize() :  This
str.capitalize() :  This
>>>
```

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
