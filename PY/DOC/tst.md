Type Conversion

In Python, it's impossible to complete certain operations due to the types involved. For instance, 
you can't add two strings containing the numbers 2 and 3 together to produce the integer 5, 
as the operation will be performed on strings, making the result '23'.

The solution to this is type conversion. 
In that example, you would use the int function.

```python
>>> "2" + "3"
'23'
>>> int("2") + int("3")
5
```

In Python, the types we have used so far have been integers, floats, and strings. 
The functions used to convert to these are int, float and str, respectively.
