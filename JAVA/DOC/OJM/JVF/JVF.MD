
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
* [if..else](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/IF/IF.MD)
* [for](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/FOR/FOR.MD)
* [while](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/WHILE/WHILE.MD)
* [do..while]()
* [functions/methods](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/FUN/FUN.MD)
* [oop](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/OOP/OOP.MD)

---

* [Programozzteis](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/PT.MD)
* [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD)

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

### Java for

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

---

### Java while

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

---

### Java Functions / Methods

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

---

### Java OOP

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

---


