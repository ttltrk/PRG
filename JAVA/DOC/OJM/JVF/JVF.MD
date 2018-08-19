
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/JT/JT.MD) - [Java](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/OJM.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JM/JM.MD)

---

### Java Flash

---

* [binarys](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/BIN/BIN.MD)
* [numbers]()
* [strings](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/STR/STR.MD)
* [variables](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/VAR/VAR.MD)

---

* [if..else](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/IF/IF.MD)
* [for](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/FOR/FOR.MD)
* [while](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/WHILE/WHILE.MD)
* [do..while]()

---

* [functions/methods](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/FUN/FUN.MD)
* [oop](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/OOP/OOP.MD)

---

[PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD)

---

### Java binarys

```
128 - 64 - 32 - 16 - 8 - 4 - 2 - 1
1   -  0 -  0 -  1 - 1 - 0 - 1 - 1
128 +  0 +  0 + 16 + 8 + 0 + 2 + 1 = 155

10011011 = 8 bit
```

```
Convert Binary to Decimal

B = Binary
D = Decimal

1B = 1D //1 bit
10B = 2D //2 bits
1111B = 15D //4 bits
10011011B = 155D //8 bits = 1 byte
```

```
8 bit = 1 byte
1000 byte = 1k byte
1000 kbyte = 1 mbyte
1000 mbyte = 1 gbyte
1000 gbyte = 1 tbyte
```

---

### Java strings

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

### Java variables

```java
int a, b, c;         
int a = 10, b = 10;  
byte B = 22;         
double pi = 3.14159; 
char a = 'a';        
String a = "hello";
boolean a = true, b = false;
```

```java
package test;
public class test {
	public static void main(String[] args) {
        
		System.out.println(Short.MAX_VALUE);
	    System.out.println(Integer.MAX_VALUE);
	    System.out.println(Long.MAX_VALUE);
	    System.out.println(Double.MAX_VALUE);

	 }
}

>>>
32767
2147483647
9223372036854775807
1.7976931348623157E308
>>>
```

---

### Java if..else

```java
public class Test {

   public static void main(String args[]) {
      int x = 30;

      if( x == 10 ) {
         System.out.print("Value of X is 10");
      }else if( x == 20 ) {
         System.out.print("Value of X is 20");
      }else if( x == 30 ) {
         System.out.print("Value of X is 30");
      }else {
         System.out.print("This is else statement");
      }
   }
}

>>>
Value of X is 30
>>>
```

---


