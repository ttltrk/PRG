
PYTHON - dataquest.io
======

### Section 1 - Python Basics

1. Programming and data science
2. Arithmetic Operators
3. Variables
4. Data Types
5. The Type Function
6. Using a List to Store Multiple Values
7. Creating Lists With Values
8. Comments
9. Accessing Elements in a List
10. Instructions
11. Slicing Lists
12. Next Steps

### Section 2 - Files and Loops

13. Overview
14. Opening Files
15. Reading In Files
16. Splitting
17. Loops
18. Practice - Loops
19. List of Lists
20.

Programming and Data Science 
------

```python
print(1288)
print(639)
print(1288 + 639)
```

```
1288
639
1927
```

Arithmetic Operators
------

```python
#average
(749+371+828+503+1379)/5
```

```
766.0
```

Variables
------

```python
albuquerque = 749
anaheim = 371
anchorage = 828
arlington = 503
atlanta = 1379

print(anaheim)
```

```
371
```

Data Types
------

```python
atlanta_string = "Atlanta"
atlanta_float = 1379.5

print(atlanta_string, atlanta_float)
```

```
Atlanta 1379.5
```

The Type Function
------

```python
atlanta_string = "Atlanta"

print(type(atlanta_string))
```

```
<class 'str'>
```

Using a List to Store Multiple Values
------

```python
cities = []
crime_rates = []

cities.append("Albuquerque")
cities.append("Anaheim")
cities.append("Anchorage")
cities.append("Arlington")
cities.append("Atlanta")

crime_rates.append(749)
crime_rates.append(371)
crime_rates.append(828)
crime_rates.append(503)
crime_rates.append(1379)

print(cities)
print(crime_rates)
```

```
['Albuquerque', 'Anaheim', 'Anchorage', 'Arlington', 'Atlanta']
[749, 371, 828, 503, 1379]
```

Creating Lists with Values
------

```python
crime_rates = [749, 371, 828, 503, 1379]

print(crime_rates)
```

```
[749, 371, 828, 503, 1379]
```

Comments
------

```python
# a list

crime_rates = [749, 371, 828, 503, 1379] # a list
print(crime_rates)
```

```
[749, 371, 828, 503, 1379]
```

Accessing Elements in a List
------

```python
# Select the third element from the list cities and assign to the variable anchorage_str.
# Select the third element from the list crime_rates and assign to the new variable anchorage_cr.

cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]

anchorage_str = cities[2] 
anchorage_cr = crime_rates[2] 
```

```

```

--------------------------------------------------------------------------

### 10. INSTRUCTIONS

```python
# Add the lengths of the cities and crime_rates list objects and assign the sum to two_sum.

cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]
# Add your code here.

two_sum = len(cities) + len(crime_rates)
```

```

```

--------------------------------------------------------------------------

### 11. SLICING LISTS

```python
cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]

cities_slice = cities[1:4]
ending_index = len(crime_rates)
cr_slice = crime_rates[3:ending_index]
```

```

```

--------------------------------------------------------------------------

### 14. OPENING FILES

```
Use the open() function to create a File object.
The name of the file to open is "crime_rates.csv". Access the file in read mode ("r").
Assign this File object to the variable f.
```

```python
a = open("test.txt", "r")
print(a)

f = open("crime_rates.csv", "r")
print(f)
```

```
<_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
<_io.TextIOWrapper name='crime_rates.csv' mode='r' encoding='UTF-8'>
```

--------------------------------------------------------------------------

### 15. READING IN FILES

```
Run the read() method on the File object f to return the string representation of crime_rates.csv.
Assign the resulting string to a new variable named data.
```

```python
f = open("crime_rates.csv", "r")
data = f.read()
print(data)
```

```
Albuquerque,749
Anaheim,371
Anchorage,828
Arlington,503
Atlanta,1379
Aurora,425
...
```

--------------------------------------------------------------------------

### 16. SPLITTING

```
Split the string object data on the new-line character "\n", and store the result in a variable named rows. - 
Then, use the print() function to display the first five elements in rows.
```

```python
# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()

rows = data.split('\n')
print(rows)
```

```
['john', 'plastic', 'joe']
['How much wood', 'can a woodchuck chuck', 'if a woodchuck', 'could chuck wood?']
['Albuquerque,749', 'Anaheim,371', 'Anchorage,828', 'Arlington,503', 
'Atlanta,1379', 'Aurora,425', 'Austin,408', 'Bakersfield,542', 'Baltimore,1405'...
```

--------------------------------------------------------------------------

### 18. PRACTICE - LOOPS

```
The variable ten_rows contains the first 10 elements in rows.
Write a for loop that:
iterates over each element in ten_rows
uses the print() function to display each element
```

```python
ten_rows = rows[0:10]

for nums in rows:
    print(ten_rows)
```

```
['Albuquerque,749', 'Anaheim,371', 'Anchorage,828', 'Arlington,503', 'Atlanta,1379', 
'Aurora,425', 'Austin,408', 'Bakersfield,542', 'Baltimore,1405', 'Boston,835']
['Albuquerque,749' ...
```

--------------------------------------------------------------------------

### 19. List of Lists

```
splits each element in three_rows (which contains the first three elements from rows) on the comma delimiter (,)
appends the resulting list (split_list) to a new list we create (final_list)
displays the final list using the print() function
```

```python
three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])
```

```
 row
 split_list
 three_rows
 final_list
```

--------------------------------------------------------------------------


