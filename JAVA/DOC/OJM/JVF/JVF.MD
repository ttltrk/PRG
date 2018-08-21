
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/JT/JT.MD) - [Java](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/OJM.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JM/JM.MD)

###### [PRG](https://github.com/ttltrk/PRG)

---

<h3 id='^'>Java Flash</h3>

---

* <a href='#binarys'>binarys</a>
* <a href='#numbers'>numbers</a>
* <a href='#strings'>strings</a>
* <a href='#variables'>variables</a>
* <a href='#ifelse'>if..else</a>
* <a href='#for'>for</a>
* <a href='#while'>while</a>
* <a href='#dowhile'>do..while</a>
* <a href='#functions/methods'>functions/methods</a>
* <a href='#oop'>oop</a>

---

* [Programozzteis](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/PT.MD)
* [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD)

---

<h3 id='binarys'>Java binarys</h3>

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

<a href='#^'>^^^</a>

---

<h3 id='numbers'>Java numbers</h3>

<a href='#^'>^^^</a>

---

<h3 id='strings'>Java strings</h3>

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

<a href='#^'>^^^</a>

---

<h3 id='variables'>Java variables</h3>

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

<a href='#^'>^^^</a>

---

<h3 id='ifelse'>Java if..else</h3>

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

<a href='#^'>^^^</a>

---

<h3 id='for'>Java for</h3>

```java
public class HelloWorld{

     public static void main(String []args){
         
        int index = 0;
        int result = 0;

        for(index = 0; index <= 4; index++)
          {
          System.out.println("Hello World");
          } 
        
     }
}

>>>
Hello World
Hello World
Hello World
Hello World
Hello World
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='while'>Java while</h3>

```java
public class HelloWorld{

     public static void main(String []args){
         
        int index = 0;
        int result = 0;
          
        while(index <= 4)
          {
          System.out.println("Hi World");
          index++;
          }
        
     }
}

>>>
Hi World
Hi World
Hi World
Hi World
Hi World
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='dowhile'>Java do while</h3>

<a href='#^'>^^^</a>

---

<h3 id='functions/methods'>Java Functions / Methods</h3>

```java
public static int methodName(int a, int b) {
   // body
}
```

```java
package test;
public class test {
    public static void main(String []args){
        
	int a = 10, b = 3, c = 2, d = 1;
		
	System.out.println(func(a, b));  
	System.out.println(func(c, d));    


	}
		
	private static int func(int param1, int param2) {
	    int res = 0;
	      
	    if (param1 > param2) {
	        res = param1; 
	    } else {
	        res = param2; 
	    } return res;
		  
        }
			
}

>>>
10
2
>>>
```

```java
package test;
public class test {
    public static void main(String []args){
	    
	    func_null();
	    System.out.println(func_pull());
		    
	    }
		
	    private static void func_null() {
	      System.out.println("hello world");
	    }
	     
	    private static String func_pull() {
	      return ("hw");
	    }
}

>>>
hello world
hw
>>>
```

```java
package test;
public class test {
	public static void main(String []args){
		  
	    System.out.println(func_null().length());
			  
	    }
			
	    private static String func_null() {
	      return ("hello world");
			  
	    }

}

>>>
11
>>>
```

```java
package test;
public class test {
    public static void main(String []args){
        
	int param1 = 3, param2 = 2;
	boolean param3 = false, param4 = true;
		
	System.out.println(func(param1, param2, param3));
	System.out.println(func(param1, param2, param4));

         
        }
	
        private static int func(int param1, int param2, boolean param3) {
	      int res = 0;        	
        	
              if (param3 == true) {
	          res = param1+param2;
              } else {
	          res = param1-param2;
              } return res;
        }

}

>>>
1
5
>>>
```

```java
package test;
public class test {
	public static void main(String[] args) {
        
	String a = "13";
	int b = Integer.parseInt(a), c = 12, d = 14;
	        
	System.out.println(func(b,c));
	System.out.println(func(b,d));

	        
	}
			
	private static int func(int first, int second) {
	    int res = 0; 
			  
	    if (first>second) {
	        res = first;
	    } else {
		res = second;	      
	    } return res;

        }

}

>>>
13
20
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='OOP'>Java OOP</h3>

```java
class Calculation {
   int z;
	
   public void addition(int x, int y) {
      z = x + y;
      System.out.println("The sum of the given numbers:"+z);
   }
	
   public void Subtraction(int x, int y) {
      z = x - y;
      System.out.println("The difference between the given numbers:"+z);
   }
}

public class My_Calculation extends Calculation {
   public void multiplication(int x, int y) {
      z = x * y;
      System.out.println("The product of the given numbers:"+z);
   }
	
   public static void main(String args[]) {
      int a = 20, b = 10;
      My_Calculation demo = new My_Calculation();
      demo.addition(a, b);
      demo.Subtraction(a, b);
      demo.multiplication(a, b);
   }
}

>>>
The sum of the given numbers:30
The difference between the given numbers:10
The product of the given numbers:200
>>>
```

<a href='#^'>^^^</a>

---


