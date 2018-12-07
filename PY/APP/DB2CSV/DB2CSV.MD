
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

### read data from DB2 and write it to a .CSV file

---

```python
import csv
import ibm_db
import datetime
import numpy as np
import pandas as pd
import sqlalchemy

def db2select():
    conn = ibm_db.pconnect("DATABASE=dbname;
                            HOSTNAME=host.com;
                            PORT=portnum;
                            PROTOCOL=TCPIP;
                            UID=user;
                            PWD=pwd;", "", "")
    sql = "SELECT * FROM temp"
    stmt = ibm_db.exec_immediate(conn, sql)
    tuple = ibm_db.fetch_tuple(stmt)
    while tuple != False:
        yield(tuple) 
        tuple = ibm_db.fetch_tuple(stmt)

def pandasFrame():
    labels = ['PersonID','LastName','FirstName','Address','City']
    df = pd.DataFrame.from_records(db2select(), columns=labels)
    df.to_csv('C:\\path\\path\\out.csv', encoding='utf-8', index=False)
    print(df)

pandasFrame()
```
