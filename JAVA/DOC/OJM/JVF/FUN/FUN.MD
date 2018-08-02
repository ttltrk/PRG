
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/JT/JT.MD) - [Java](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/OJM.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JM/JM.MD) - [JVF](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/JVF.MD)

---

### Java Functions / Methods

---

```java
public static int methodName(int a, int b) {
   // body
}
```

---

```java
package test;
public class test {
    public static void main(String []args){
        
	int a = 10, b = 3, c = 2, d = 1;
		
	System.out.println(func(a, b));  
	System.out.println(func(c, d));    


	}
		
	private static int func(int param1, int param2) {
	    int res;
	      
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

---

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

---

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

---

```java
package pogrammingPackage;

public class Programming {
  public static void main(String []args){
        
		int param1 = 3, param2 = 2;
		boolean param3 = false;
		
		System.out.println(func(param1, param2, param3));
         
    }
	
    private static int func(int param1, int param2, boolean param3) {
	  if (param3 == true)
	    return param1+param2;
	  else
	    return param1-param2;	  
  }

}

>>>
1
>>>
```

---

```java
public class HelloWorld{
    public static void main(String[] args) {
        
    int a = 12;
    String b = "13";
    int c = Integer.parseInt(b);
        
    System.out.println(func(a,c));
        
    }
		
    private static int func(int first, int second) {
		  
      int retVal = 0; 
		  
      if (first<second)
        retVal = first;
      else
	 retVal = second;	      
	   return retVal;

	}

}

>>>
12
>>>
```

---

```java
package test;

public class test {
	public static void main(String[] args) {
		
		int a = 6, b = 12;
		
		System.out.println(func(a, b)); 
		
	    }
		
		private static int func(int n1, int n2) {
			   int min;
			   if (n1 > n2)
			      min = n2;
			   else
			      min = n1;

			   return min; 
			}

	}
	
>>>
6
>>>
```

---

[PY](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/FUN/FUN.MD)

---
