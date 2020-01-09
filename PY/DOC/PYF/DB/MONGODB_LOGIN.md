
## MongoDB LOGIN

- [freecodecamp](https://www.freecodecamp.org/news/learn-mongodb-a4ce205e7739/)
- [w3school](https://www.w3schools.com/python/python_mysql_getstarted.asp)

---

## creating or accessing a new db


```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
```

---

## checking the actual dbs


```python
print(myclient.list_database_names())
```

    ['admin', 'config', 'local', 'mydatabase', 'trkDB']
    

---

## create a collection and insert in to it with - insert_one()


```python
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(mydb.list_collection_names())

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
```

    ['customers']
    The collection exists.
    

---

## Return the _id field

- The insert_one() method returns a InsertOneResult object, which has a property, inserted_id, that holds the id of the inserted document.


```python
mydict = { "name": "Peter", "address": "Lowstreet 27" }

x = mycol.insert_one(mydict)

print(x.inserted_id)
```

    5e16de4ff324dec4ce365abc
    

---

## Insert Multiple Documents with - insert_many()

- To insert multiple documents into a collection in MongoDB, we use the insert_many() method.
- The first parameter of the insert_many() method is a list containing dictionaries with the data you want to insert



```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
```

    [ObjectId('5e16de97f324dec4ce365abe'), ObjectId('5e16de97f324dec4ce365abf'), ObjectId('5e16de97f324dec4ce365ac0'), ObjectId('5e16de97f324dec4ce365ac1'), ObjectId('5e16de97f324dec4ce365ac2'), ObjectId('5e16de97f324dec4ce365ac3'), ObjectId('5e16de97f324dec4ce365ac4'), ObjectId('5e16de97f324dec4ce365ac5'), ObjectId('5e16de97f324dec4ce365ac6'), ObjectId('5e16de97f324dec4ce365ac7'), ObjectId('5e16de97f324dec4ce365ac8'), ObjectId('5e16de97f324dec4ce365ac9')]
    

---

## Insert Multiple Documents, with Specified IDs

- If you do not want MongoDB to assign unique ids for you document, you can specify the _id field when you insert the document(s).


```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
```


    ---------------------------------------------------------------------------

    BulkWriteError                            Traceback (most recent call last)

    <ipython-input-10-03266ccbb8a6> in <module>
         22 ]
         23 
    ---> 24 x = mycol.insert_many(mylist)
         25 
         26 #print list of the _id values of the inserted documents:
    

    ~\Anaconda3\lib\site-packages\pymongo\collection.py in insert_many(self, documents, ordered, bypass_document_validation, session)
        756         blk = _Bulk(self, ordered, bypass_document_validation)
        757         blk.ops = [doc for doc in gen()]
    --> 758         blk.execute(write_concern, session=session)
        759         return InsertManyResult(inserted_ids, write_concern.acknowledged)
        760 
    

    ~\Anaconda3\lib\site-packages\pymongo\bulk.py in execute(self, write_concern, session)
        509                 self.execute_no_results(sock_info, generator)
        510         else:
    --> 511             return self.execute_command(generator, write_concern, session)
        512 
        513 
    

    ~\Anaconda3\lib\site-packages\pymongo\bulk.py in execute_command(self, generator, write_concern, session)
        347 
        348         if full_result["writeErrors"] or full_result["writeConcernErrors"]:
    --> 349             _raise_bulk_write_error(full_result)
        350         return full_result
        351 
    

    ~\Anaconda3\lib\site-packages\pymongo\bulk.py in _raise_bulk_write_error(full_result)
        138         full_result["writeErrors"].sort(
        139             key=lambda error: error["index"])
    --> 140     raise BulkWriteError(full_result)
        141 
        142 
    

    BulkWriteError: batch op errors occurred


---

## find_one()


```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.find_one()

print(x)
```

    {'_id': ObjectId('5e148647828172d398da0873'), 'name': 'John', 'address': 'Highway 37'}
    

---

## find_all()


```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find():
  print(x)
```

    {'_id': ObjectId('5e148647828172d398da0873'), 'name': 'John', 'address': 'Highway 37'}
    {'_id': ObjectId('5e148826828172d398da0874'), 'name': 'John', 'address': 'Highway 37'}
    {'_id': ObjectId('5e15aa9061a398c276bbe800'), 'name': 'John', 'address': 'Highway 37'}
    {'_id': ObjectId('5e16d386f324dec4ce365aba'), 'name': 'John', 'address': 'Highway 37'}
    {'_id': ObjectId('5e16de31f324dec4ce365abb'), 'name': 'John', 'address': 'Highway 37'}
    {'_id': ObjectId('5e16de4ff324dec4ce365abc'), 'name': 'Peter', 'address': 'Lowstreet 27'}
    {'_id': ObjectId('5e16de97f324dec4ce365abe'), 'name': 'Amy', 'address': 'Apple st 652'}
    {'_id': ObjectId('5e16de97f324dec4ce365abf'), 'name': 'Hannah', 'address': 'Mountain 21'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac0'), 'name': 'Michael', 'address': 'Valley 345'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac1'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac2'), 'name': 'Betty', 'address': 'Green Grass 1'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac3'), 'name': 'Richard', 'address': 'Sky st 331'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac4'), 'name': 'Susan', 'address': 'One way 98'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac5'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac6'), 'name': 'Ben', 'address': 'Park Lane 38'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac7'), 'name': 'William', 'address': 'Central st 954'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac8'), 'name': 'Chuck', 'address': 'Main Road 989'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac9'), 'name': 'Viola', 'address': 'Sideway 1633'}
    {'_id': 1, 'name': 'John', 'address': 'Highway 37'}
    {'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
    {'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
    {'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
    {'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
    {'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
    {'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
    {'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
    {'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
    {'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
    {'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
    {'_id': 12, 'name': 'William', 'address': 'Central st 954'}
    {'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
    {'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
    

---

## Return Only Some Fields - find()

- The second parameter of the find() method is an object describing which fields to include in the result.
- This parameter is optional, and if omitted, all fields will be included in the result.


```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)
```

    {'name': 'John', 'address': 'Highway 37'}
    {'name': 'John', 'address': 'Highway 37'}
    {'name': 'John', 'address': 'Highway 37'}
    {'name': 'John', 'address': 'Highway 37'}
    {'name': 'John', 'address': 'Highway 37'}
    {'name': 'Peter', 'address': 'Lowstreet 27'}
    {'name': 'Amy', 'address': 'Apple st 652'}
    {'name': 'Hannah', 'address': 'Mountain 21'}
    {'name': 'Michael', 'address': 'Valley 345'}
    {'name': 'Sandy', 'address': 'Ocean blvd 2'}
    {'name': 'Betty', 'address': 'Green Grass 1'}
    {'name': 'Richard', 'address': 'Sky st 331'}
    {'name': 'Susan', 'address': 'One way 98'}
    {'name': 'Vicky', 'address': 'Yellow Garden 2'}
    {'name': 'Ben', 'address': 'Park Lane 38'}
    {'name': 'William', 'address': 'Central st 954'}
    {'name': 'Chuck', 'address': 'Main Road 989'}
    {'name': 'Viola', 'address': 'Sideway 1633'}
    {'name': 'John', 'address': 'Highway 37'}
    {'name': 'Peter', 'address': 'Lowstreet 27'}
    {'name': 'Amy', 'address': 'Apple st 652'}
    {'name': 'Hannah', 'address': 'Mountain 21'}
    {'name': 'Michael', 'address': 'Valley 345'}
    {'name': 'Sandy', 'address': 'Ocean blvd 2'}
    {'name': 'Betty', 'address': 'Green Grass 1'}
    {'name': 'Richard', 'address': 'Sky st 331'}
    {'name': 'Susan', 'address': 'One way 98'}
    {'name': 'Vicky', 'address': 'Yellow Garden 2'}
    {'name': 'Ben', 'address': 'Park Lane 38'}
    {'name': 'William', 'address': 'Central st 954'}
    {'name': 'Chuck', 'address': 'Main Road 989'}
    {'name': 'Viola', 'address': 'Sideway 1633'}
    


```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find({},{ "address": 0 }):
  print(x)
```

    {'_id': ObjectId('5e148647828172d398da0873'), 'name': 'John'}
    {'_id': ObjectId('5e148826828172d398da0874'), 'name': 'John'}
    {'_id': ObjectId('5e15aa9061a398c276bbe800'), 'name': 'John'}
    {'_id': ObjectId('5e16d386f324dec4ce365aba'), 'name': 'John'}
    {'_id': ObjectId('5e16de31f324dec4ce365abb'), 'name': 'John'}
    {'_id': ObjectId('5e16de4ff324dec4ce365abc'), 'name': 'Peter'}
    {'_id': ObjectId('5e16de97f324dec4ce365abe'), 'name': 'Amy'}
    {'_id': ObjectId('5e16de97f324dec4ce365abf'), 'name': 'Hannah'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac0'), 'name': 'Michael'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac1'), 'name': 'Sandy'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac2'), 'name': 'Betty'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac3'), 'name': 'Richard'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac4'), 'name': 'Susan'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac5'), 'name': 'Vicky'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac6'), 'name': 'Ben'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac7'), 'name': 'William'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac8'), 'name': 'Chuck'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac9'), 'name': 'Viola'}
    {'_id': 1, 'name': 'John'}
    {'_id': 2, 'name': 'Peter'}
    {'_id': 3, 'name': 'Amy'}
    {'_id': 4, 'name': 'Hannah'}
    {'_id': 5, 'name': 'Michael'}
    {'_id': 6, 'name': 'Sandy'}
    {'_id': 7, 'name': 'Betty'}
    {'_id': 8, 'name': 'Richard'}
    {'_id': 9, 'name': 'Susan'}
    {'_id': 10, 'name': 'Vicky'}
    {'_id': 11, 'name': 'Ben'}
    {'_id': 12, 'name': 'William'}
    {'_id': 13, 'name': 'Chuck'}
    {'_id': 14, 'name': 'Viola'}
    

---

## Filter the Result

- When finding documents in a collection, you can filter the result by using a query object.
- The first argument of the find() method is a query object, and is used to limit the search.


```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
```

    {'_id': ObjectId('5e16de97f324dec4ce365ac6'), 'name': 'Ben', 'address': 'Park Lane 38'}
    {'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
    

---

## Advanced Query

- To make advanced queries you can use modifiers as values in the query object.
- E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}:


```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$gt": "S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
```

    {'_id': ObjectId('5e16de97f324dec4ce365ac0'), 'name': 'Michael', 'address': 'Valley 345'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac3'), 'name': 'Richard', 'address': 'Sky st 331'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac5'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac9'), 'name': 'Viola', 'address': 'Sideway 1633'}
    {'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
    {'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
    {'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
    {'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
    

---

## Filter With Regular Expressions



```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
```

    {'_id': ObjectId('5e16de97f324dec4ce365ac3'), 'name': 'Richard', 'address': 'Sky st 331'}
    {'_id': ObjectId('5e16de97f324dec4ce365ac9'), 'name': 'Viola', 'address': 'Sideway 1633'}
    {'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
    {'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
    

---


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
