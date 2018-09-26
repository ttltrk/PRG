
```python
import csv
import ibm_db
import datetime

conn = ibm_db.connect("DATABASE=DBNAME;HOSTNAME=HOSTNAME;PORT=PORTNUM;PROTOCOL=TCPIP;UID=DBUSER;PWD=DBPWD;", "", "")

sql1 = "SELECT * FROM blabla WHERE SOURCE_KEY='blabla'"
stmt1 = ibm_db.exec_immediate(conn, sql1)
result1 = ibm_db.fetch_both(stmt1)

sql2 = "SELECT * FROM blublu WHERE SOURCE_KEY='blublu'"
stmt2 = ibm_db.exec_immediate(conn, sql2)
result2 = ibm_db.fetch_both(stmt2)

l0 = []
l0.append(result1[0])
l0.append(result1[1])
l0.append(result1[2])
l0.append(result1[3])

l1 = []
l1.append(result2[0])
l1.append(result2[1])
l1.append(result2[2])
l1.append(result2[3])


###write the files to the .csv
with open('C:\\path\\path\\out.csv', mode='w') as output:
    csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    #csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(l0)
    csv_writer.writerow(l1)
```
