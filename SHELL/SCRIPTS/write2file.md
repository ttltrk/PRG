
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

### Shell - write to file (DB2)

```sh
db2 connect to <DB_NAME> user <user_name> using <pwd>
db2 -x "select blablabla" | while read var1 ; do
	C1=$var1
	destdir=/home/path/path/filename.txt
	for i in "$C1"
	do
	 echo "$i"
	 echo "$i" >> "$destdir"
	done
done
```
