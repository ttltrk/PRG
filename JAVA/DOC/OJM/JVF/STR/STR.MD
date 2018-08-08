
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/JT/JT.MD) - [Java](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/OJM.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JM/JM.MD) - [JVF](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/JVF.MD)

---

### Java strings

---

```java
package test;
public class test {
	public static void main(String[] args) {
		
		char simpleChar = 'y';
        
		System.out.println(simpleChar);

	 }
}

>>>
y
>>>
```

---

```java
package test;
public class test {
	public static void main(String[] args) {
		
		String simpleString = "hello world";
        
		System.out.println(simpleString);

	 }
}

>>>
hello world
>>>
```

---

```java
package test;
public class test {
	public static void main(String[] args) {
		
		String simpleString = "hello world";
        
		System.out.println(simpleString.charAt(4));

	 }
}

>>>
o
>>>
```

---

```java
package test;
public class test {
	public static void main(String[] args) {
		
		String simpleString = "hello world";
        
		System.out.println(simpleString.substring(2, 5));

	 }
}

>>>
llo
>>>
```

---

```java
package test;
public class test {
	public static void main(String[] args) {
		
		String simpleString = "hello world";
        
		System.out.println(simpleString.length());
		System.out.println(simpleString.equals("hello nadasd"));
		System.out.println(simpleString.equals("hello world"));

	 }
}

>>>
11
false
true
>>>
```

---

```java
package test;
public class test {
	public static void main(String[] args) {
		
		String simpleString = "hello world";
        
		System.out.println(simpleString.replaceAll("hello", "yellow"));
		
	 }
}

>>>
yellow world
>>>
```

---
