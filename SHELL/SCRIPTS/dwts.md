
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

### Shell - cretate dir with timestamp

```sh
function dch {
	dirname="EI_NS_01"
	current_time=$(date "+%Y%m%d-%H%M%S")
	echo "Current Time: $dirname-$current_time"
	a=$dirname-$current_time
	mkdir $a
}

#call function
dch;
```
