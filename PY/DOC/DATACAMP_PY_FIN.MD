[Importing & Managing Financial Data in Python](https://www.datacamp.com/courses/importing-managing-financial-data-in-python)
======

### Importing Stock Listing Data
  * Reading, Inspecting and cleaning data from csv files
  * Import Stock Listing info from the NASDAQ
  * How to fix the Data Import?
  * Read data using .read_csv() with adequate parsing arguments
  * Read data from Excel worksheets
  

### Importing Financial Data

### Summarizing Your Data

### Aggregating and Describing

Importing Stock Listing Data
------

### Reading, Inspecting and cleaning data from csv files

#### Import and clean data
  * Ensure that pd.DataFrame() is same as csv source file
  * Stock Exchange listings: amex-listings.csv
  
#### How Panda stores data
  * Each column has its own data format stored in dtype
  * dtype affects calculation and visualization
  
  pandas dtype: object, int64, float64, datetime64
  
### Import stock listing info from the NASDAQ

In this video, you learned how to use the pd.read_csv() function to import data from a csv file 
containing companies listed on the AmEx Stock Exchange into a pandas DataFrame. You can apply this same knowledge 
to import listing information in csv files from other stock exchanges.

The next step is to ensure that the contents of the DataFrame accurately reflect the meaning of your data. 
Two essential methods to understand your data are .head(), which displays the first five rows of your data by default, 
and .info(), which summarizes elements of a DataFrame such as content, data types, and missing values.

In this exercise, you will read the file nasdaq-listings.csv with data on companies listed on the NASDAQ and then diagnose issues 
with the imported data. You will fix these issues in the next exercise.

```python
"""
Load pandas as pd.
Use pd.read_csv() to load the file nasdaq-listings.csv into the variable nasdaq.
Use .head() to display the first 10 rows of the data. Which data type would you expect pandas 
to assign to each column? 
What symbol is used to represent a missing value?
Use .info() to identify dtype mismatches in the DataFrame summary. Specifically, 
are there any columns that should have a more appropriate type?
"""


>>>

>>>
```




