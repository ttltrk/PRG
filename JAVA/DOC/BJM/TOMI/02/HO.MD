
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [course manuals](https://github.com/ttltrk/PRG/blob/master/COUR_MAN.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/CM/JT.MD) - [Java - PT](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/JJ.MD) - [2nd-3rd](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/2nd.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/JT/JT.MD) - [Java](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/OJM.MD)

---

### 2nd and 3rd HO

---

1. Definiáljunk egy-egy String változót a vezetéknévnek és a keresztnévnek. 
Fűzzük össze a két változót egy harmadikba.

```java
//Java result
package pogrammingPackage;
public class Programming {
	public static void main(String []args){
        
		String n1 = "ttl ";
		String n2 = "trk";
		String n3 = n1+n2;
		
		System.out.println(n3);
         		  
  }

}

>>>
ttl trk
>>>
```

```python
#Python result
a = "ttl "
b = "trk"
print(a+b)

>>>
ttl trk
>>>
```

---

2. Definiáljunk egy egész típust és adjunk neki értékül egy nem egész számot 
(pl.: 5,5). Mi történik?

```java
//Java result
public class HelloWorld{
     public static void main(String []args){
         
         int i = 5.5;
         
        System.out.println(i);
     }
}

>>>
HelloWorld.java:5: error: incompatible types: possible lossy conversion from double to int
         int i = 5.5;
                 ^
1 error
>>>
```

---

3. Definiáljunk egy double és egy int típust. A double típus legyen egyenlő az int típusú változó kétszeresével.

```java
//Java result
public class HelloWorld{

     public static void main(String []args){
         
         int i = 5;
         double d = 2*i;
         
        System.out.println(i);
        System.out.println(d);
     }
}

>>>
5
10.0
>>>
```

```python
#Python result
a = 5
b = 2.0
print(a*b)

>>>
10.0
>>>
```

---

4. A 3. feladatban létrehozott változókat most fordítva használjuk: Az int típusú változó legyen egyenlő a double típus 3,14-szeresével. Mi történik?

```java
//Java result
public class HelloWorld{

     public static void main(String []args){
         
        double d = 10.0;
        int i = 3.14*d;
        
        System.out.println(i);
        System.out.println(d);
     }
}

>>>
HelloWorld.java:6: error: incompatible types: possible lossy conversion from double to int
        int i = 3.14*d;
                    ^
1 error
>>>
```

```python
#Python result
a = 10.0
b = 3.14
print(a*b)

>>>
31.400000000000002
>>>
```

---

5. Definiáljunk egy függvényt visszatérési érték és bemeneti paraméter nélkül. Írassuk ki vele, hogy "Hello World"

```java
//Java result
package pogrammingPackage;

public class Programming {
  public static void main(String []args){
        
	  func_null();
	    
    }
	
    private static void func_null() {
    	System.out.println("hello world");
	  
  }

}

>>>
hello world
>>>
```

```java
public class HelloWorld{

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
package pogrammingPackage;

public class Programming {
  public static void main(String []args){
        
	  System.out.println(func_null());
	  
    }
	
    private static String func_null() {
    	return ("hello world");
	  
  }

}

>>>
hello world
>>>
```

```java
package pogrammingPackage;

public class Programming {
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

```python 
#Python result

def no():
  print("hello world")
  
no()

>>>
hello world
>>>
```

---

6. Definiáljunk egy kiírató függvényt, aminek nincs visszatérési értéke de egy bemenő String-et vár amit a Println() függvénnyel ki tudunk iratni.

```java
//Java result
package pogrammingPackage;

public class Programming {
public static void main(String []args){
        
	    String a = "hello world";
		
		func_null(a);
         
    }
	
    private static void func_null(String a) {
    	System.out.println(a);
	  
  }

}


>>>
hello world
>>>
```

```java
package pogrammingPackage;

public class Programming {
public static void main(String []args){
        
	    String a = "hello world";
	    String b = "xyz";
		
	    System.out.println(a);
	    func_null(b);
         
    }
	
    private static void func_null(String param1) {
    	System.out.println(param1);
	  
  }

}

>>>
hello world
xyz
>>>
```

```java
package pogrammingPackage;

public class Programming {
public static void main(String []args){
        
	    String a = "hello world";
	    String b = "xyz";
		String c = a+b;
		a = a+b;
		
	    System.out.println(a);
	    func_null(b);
	    func_null("abc");
	    func_null(c);
         
    }
	
    private static void func_null(String param1) {
    	System.out.println(param1);
	  
  }

}

>>>
hello worldxyz
xyz
abc
hello worldxyz
>>>
```

```python
#Python result
#variables
a = "hello world"
b = "xyz"
c = 5
d = 7

#functions
def pr(par1):
  print(par1)
  
def ps(par1, par2):
  return (par1+par2)

def ms(par1,par2):
  return (par1-par2)

#STDOUT
pr(a)
pr(b)
print(ps(c,d))
print(ms(c,d))

>>>
hello world
xyz
12
-2
>>>
```

---

7. Legyen egy függvény ami bemenetként 2 számot és egy boolean értéket vár. Ha a boolean igaz, akkor a két számot össszeadni, ha hamis akkor pedig kivonni kell. Hogyan nevezné el a paramétereket, hogy jól olvasható legyen a függvény?

```java
//Java result
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

```python
#Python result
a = 20
b = 4
c = True
d = False

def no(p1,p2,p3):
  if (p3 == True):
    print(p1+p2)
  else:
    print(p1-p2)
  
no(a,b,c)
no(a,b,d)

>>>
24
16
>>>
```

---

8. Definiáljon egy átalakító függvényt, ami int típusból String típust csinál. Hogyan néz ki a függvény definíciója (visszatérési érték - függvény név - paraméterek)?

```java
package pogrammingPackage;
public class Programming {
	public static void main(String []args){
        
		String number = "10";
		int res = Integer.parseInt(number);		
		
		System.out.println(func(res));
		
	  }
		
	  private static int func(int result) {
		  return result;
	  
  }

}


>>>
10
>>>
```

---

9. Mi a baj a következő függvénnyel?

NR
!!

```java
	private static void getLengthOfString(String whatIsLength)
	{
		int whatIsLength = 0;
		WhatIsLength = WhatIsLength.length();
		return whatIsLength;
	}
```
	Javítsa ki!

```java
public class Programming {
	public static void main(String []args){
        
	  getLengthOfString(int whatIsLength)
		
	  }
		
	  private static void getLengthOfString(int whatIsLength)
	
	{
		int whatIsLength = 0;
		WhatIsLength = WhatIsLength.length();
		return whatIsLength;
	}

}
```

---

10. Mi lesz a kimenete a következő függvénynek:

NR

```java
		static int whatIsTheRetVal()
		{
			calculatedIntResult = 2;
			++calculatedIntResult;
			return calculatedIntResult++;
		}
```

```java

```

---

11. Definiáljunk egy függvényt ami kiírja a paramétereként kapott számot majd megnöveli azt egyel. Mielőtt a függvény végrehajtása befejeződik, hívja meg saját magát a megnövelt paraméter értékkel. Mi lesz a futás eredménye?

```java
package pogrammingPackage;
public class Programming {
public static void main(String []args){
        
		int p1 = 10;
		
		func(p1);
         
    }
	
    private static void func(int param1) {
	  
    	System.out.println(++param1);
    	func(param1);
    	
        }

	  
  }

>>>
10827
10828
10829
10830
Exception in thread "main" java.lang.StackOverflowError
	at sun.nio.cs.UTF_8$Encoder.encodeLoop(UTF_8.java:691)
	at java.nio.charset.CharsetEncoder.encode(CharsetEncoder.java:579)
	at sun.nio.cs.StreamEncoder.implWrite(StreamEncoder.java:271)
	at sun.nio.cs.StreamEncoder.write(StreamEncoder.java:125)
>>>
```

---

12. Definiáljunk egy függvényt ami visszaadja a 2 paramétere közül a nagyobbat.

```java
public class HelloWorld{

    public static void main(String []args){
        
		int a = 2, b = 3, c = 4, d = 5;
		
		System.out.println(func(a, b));
		System.out.println(func(d, c));
         
    }
	
    private static int func(int param1, int param2) {
	  if (param1 > param2)
	    return param1;
	  else
		return param2;
    }
     
}

>>>
3
5
>>>
```

---

13. Definiáljuk az osztás függvényt, ami 0-val való osztás esetén hibaértéket ad vissza

```python
p1 = 10
p2 = 5

def div():
  if (p1/p2 == 2):
    print("gut")
  else:
    print("err")
    
div()

>>>
gut
>>>
```

```python
p1 = 10
p2 = 6

def div():
  if (p1/p2 == 2):
    print("gut")
  else:
    print("err")
    
div()

>>>
err
>>>
```

```java
public class HelloWorld{
	public static void main(String []args){
        
		int param1 = 10;
		int param2 = param1/0;
		String param3 = "err";
		
		System.out.println(func(param1, param2, param3));
         
    }
	
    private static int func(int param1, int param2, String param3) {
	  if (param2 == 0)
	    return param3;
	  
        }

}

>>>
HelloWorld.java:14: error: incompatible types: String cannot be converted to int
	    return param3;
	           ^
1 error
>>>
```

```java
public class HelloWorld{
	public static void main(String []args){
        
		int param1 = 10;
		
		System.out.println(func(param1));
         
    }
	
    private static int func(int param1) {
	  return param1/0;
	  
        }

}

>>>
Exception in thread "main" java.lang.ArithmeticException: / by zero
	at HelloWorld.func(HelloWorld.java:11)
	at HelloWorld.main(HelloWorld.java:6)
>>>
```

---

14. Implementáljuk az alábbi függvények tartalmát, hogy minden változó kombinációra helyes értéket adjon vissza:

```
		- AND: boolean getAndLogicResult(boolean a, boolean b, boolean c);
		- OR: boolean getOrLogicResult(boolean a, boolean b, boolean c, boolean d);
		- NOT: boolean getNotLogicResult(boolean a);
```

NR !!!

```java
public class Programming {
  public static void main(String []args){
      
      int elso = 1;
      int masodik = 2;
      int harmadik = 3;
      int negyedik = 4;
      
	  getAndLogicResult(elso, masodik, harmadik);

    }
	
    private static boolean getAndLogicResult(boolean a, boolean b, boolean c) {
    	if ((b > a) AND (a<c)) == true;
    	  System.out.println("true");
    	else
    	  System.out.println("false");
    	
	  
  }
  
    
}
```

---

15. Hozzunk létre egy függvényt, ami meghatározza, hogy a paraméterként kapott szöveg, hosszabb-e mint a második paraméterként megkapott limit.

NR

```java

```

---

16. Implementáljuk le az osztályozó függvényt, ami bemenetként 4 paramétert vár az alábbi szintaxissal:

NR

```java

/**
		 * 
		 * @param lowerPointOfHighLevel
		 * 		If this point has achieved, then the Skill Level is High
		 * @param lowerPointOfMidLevel
		 * 		If this point has achieved, then the Skill Level is Medium
		 * @param lowerPointOfLowLevel
		 * 		If this point has achieved, then the Skill Level is only Low
		 * @param actualPoint
		 * 		Actual point of the Student
		 * @return
		 * 		Defined Values
		 * 			3 := High
		 * 			2 := Medium
		 * 			1 := Low - Get Fired
		 */
		static int getSkillLevel(int minPointOfHighLevel, int minPointOfMidLevel, int minPointOfLowLevel, int actualPoint); 

```

---

17. Implementáljon egy függvényt ami a bemeneti paraméterről eldönti, hogy páros-e vagy páratlan és az eredményt írja ki a képernyőre.

NR

```java
public class Programming {
  public static void main(String []args){
      
      int a = 1;
      int b = 2;
        
	  func_par_par(a);
	  func_par_par(b);
	    
    }
	
    private static void func_par_par(int num) {
    	if ((num%2)==0)
    	  System.out.println("paros");
    	else
    	  System.out.println("paratlan");
    	
	  
  }

}

>>>
paratlan
paros
>>>
```

---

18. Mi lesz a program futásának eredménye?

NR

```java
		public static void main(String[] args)
		{	
			String s1 = "Computer Science";
			int x = 307;
			String s2 = s1 + " " + x;
			String s3 = s2.substring(10,17);
			String s4 = "is fun";
			String s5 = s2 + s4;
			
			System.out.println("s1: " + s1);
			System.out.println("s2: " + s2);
			System.out.println("s3: " + s3);
			System.out.println("s4: " + s4);
			System.out.println("s5: " + s5);
		}

>>>
s1: Computer Science
s2: Computer Science 307
s3: cience 
s4: is fun
s5: Computer Science 307is fun
>>>
```

---

19. Hozzuk létre az alábbi függvényt:

NR

```java
		static int getResult()
		{
			return (4294967300);
		}
	Milyen visszajelzést ad az Eclipse? Miért?

```

---

20. Készítsük el a void swap(int number1, int number2) függvényt ami megcseréli a két paraméter értékét. Írassa ki az eredeti és az új értékeit is a paramétereknek.

NR

```java

```

---

21. Számoljuk ki a számok összegét 1-től 100-ig, úgy, hogy csupán egyetlen függvényt használjunk fel az összegzéshez, ami az alábbi szintaxissal rendelkezik:

NR

```java
		/**
		 * @param number1
		 * 		First number in the summary
		 * @return
		 * 		Summary result from number1 to 100
		 */
		public int summary(int number1);
	Ne adja össze a számokat egyesével!


```

---

22. Számolja ki a Fibonacci-számsorozat első X elemét egyetlen függvény segítségével. A számsorozat első két eleme ismert: 0 és 1 

```java
package pogrammingPackage;

  public class Programming {
    public static void main(String args[]){    
      
      int n1=0,n2=1,n3,i,count=10;    
      System.out.print(n1+" "+n2);    
      
      for(i=2; i<count; ++i){    
        n3=n1+n2;    
        System.out.print(" "+n3);    
        
        n1=n2;    
        n2=n3;    
    } 	  
  }
}

>>>
0 1 1 2 3 5 8 13 21 34
>>>
```

---

23. Ha egy falu népessége jelenleg X és minden évben Y%-al csökken a népesség, akkor mikorra fog teljesen elnéptelenedni a falu? Implmenetáljon erre egy algoritmust.

NR

```java

```

---

24. Definiáljuk a swap() függvényt. Hozzunk létre két változót a main()-ben, majd hívjuk meg a swap() függvényt majd a swap() függvény lefutása után a main() függvényben ellenőrizzük le a két változó értékét. Mit látunk? Magyarázza meg az eredményt!

NR

```java

```

---

25. Számoljuk meg az "i" betűk számát az alábbi String-ben: "This is a String":
		- Ha van benne "i" betű, akkor írjuk ki a pontos darabszámot
		- Ha nincs benne "i" betű, akkor azt írjuk ki, hogy a keresett betű az adott szövegben nem megtalálható

```java

```
 
 ---
