
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [course manuals](https://github.com/ttltrk/PRG/blob/master/COUR_MAN.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/CM/JT.MD) - [Programozzteis](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/PT.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/JT/JT.MD) - [Java](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/OJM.MD)

---

<h3 id='^'>JAVA PT</h3>

---

* <a href='#1st'>1st</a>
* [2nd-3rd-4th](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/2nd.MD)
* <a href='#5th'>5th</a>
* [6th](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/06/06.MD)
* <a href='#7th'>7th</a>
---

<h3 id='1st'>1st</h3>

Hello World

```java
/**
 * 
 */
package pogrammingPackage;

/**
 * @author attilatorok
 *
 */
public class Programming {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println(2+3);
		System.out.println(2-3);
		System.out.println(2-3.5);
		System.out.println((50/10)/5);
		
		System.out.println(
				(2+3) +" "+ (2-3) +" "+ (1+1)
				);
		
	}

}

>>>
5
-1
-1.5
1
5 -1 2
>>>
```

<a href='#^'>^^^</a>

1.01

```java
/**
 * Szabja testre az Eclipse nézetét: Csak a "Console" és az 
 * "Outline" ablakokat tartsa meg valamint adja hozzá a "Search View"-t
 */

use the ```minimize``` button

window --> show view
```

<a href='#^'>^^^</a>

1.02

```java
/**
 * Mit lát az Outline View-ban? Hogyan tud fájlon belül keresni?
 */

package + class

expand, collapse
```

<a href='#^'>^^^</a>

1.03

```java
/**
 * Jelenítse meg hexadecimálisan a 255-t egy beépített függvény segítségével
 */

package pogrammingPackage;
public class Programming {
	public static void main(String[] args) {
		String hexa_1;
		String hexa_2;
		String hexa_3;
		
		int num_1 = 200;
		int num_2 = 250;
		int num_3 = 255;
		
		hexa_1 = Integer.toHexString(num_1);
		hexa_2 = Integer.toHexString(num_2);
		hexa_3 = Integer.toHexString(num_3);
		
		System.out.println(hexa_1);
		System.out.println(hexa_2);
		System.out.println(hexa_3);
		
	}

}

>>>
c8
fa
ff
>>>
```

<a href='#^'>^^^</a>

1.04

```java
/**
 * Adjon meg logikai relációt számok között és írassa ki annak eredményét:
 * 5 > 3
 * 3 > 3
 * 3 >= 3
 * 1 < 2
 * 8 <= 4
 * 0 != 15
 * 9 == 9
 * 5 == 7
 * Mikor mi az eredmény?
 */

package pogrammingPackage;
public class Programming {
	public static void main(String[] args) {
		  boolean res1 = (5 > 3);
		  boolean res2 = (3 > 3);
		  boolean res3 = (3 >= 3);
		  boolean res4 = (1 < 2);
		  boolean res5 = (8 <= 4);
		  boolean res6 = (0 != 15);
		  boolean res7 = (5 == 7);
		  boolean res8 = (9 == 9);
		  
		  System.out.println("1st result (5 > 3) = "+res1);
		  System.out.println("2nd result (3 > 3) = "+res2);
		  System.out.println("3rd result (3 >= 3) = "+res3);
		  System.out.println("4th result (1 < 2) = "+res4);
		  System.out.println("5th result (8 <= 4) = "+res5);
		  System.out.println("6th result (0 != 15) = "+res6);
		  System.out.println("7th result (5 == 7) = "+res7);
		  System.out.println("8th result (9 == 9) = "+res8);
		
	}

}

>>>
1st result (5 > 3) = true
2nd result (3 > 3) = false
3rd result (3 >= 3) = true
4th result (1 < 2) = true
5th result (8 <= 4) = false
6th result (0 != 15) = true
7th result (5 == 7) = false
8th result (9 == 9) = true
>>>
```

<a href='#^'>^^^</a>

1.05

```java
/**
 * Minek a rövidítése a JRE és mit jelent? Mi az a JVM?
 */

JRE

The Java Runtime Environment (JRE) is a set of software tools for development 
of Java applications. It combines the Java Virtual Machine (JVM), 
platform core classes and supporting libraries.

JRE is part of the Java Development Kit (JDK), but can be downloaded separately. 
JRE was originally developed by Sun Microsystems Inc., 
a wholly-owned subsidiary of Oracle Corporation. 

Also known as Java runtime.

JVM

A Java virtual machine (JVM) is an abstract computing machine that enables a computer 
to run Java programs as well as programs written in other languages and compiled 
to Java bytecode. There are three notions of the JVM: specification, implementation, and instance. 
```

<a href='#^'>^^^</a>

1.06

```java
/**
 * Melyik JRE Package-ben van benne a System println függvénye?
 * 
 */

JRE System Library --> rt.jar --> java.io --> PrintStream.class --> println()
```

<a href='#^'>^^^</a>

1.07

```java
/**
 * Írjon az "err" console-ra ha a hexadecimálisan megjelnített 255 nem egyenlő 0xDE-vel
 */

package pogrammingPackage;
public class Programming {
	public static void main(String[] args) {
		String hexa = Integer.toHexString(255);
		if (hexa.equals("0xDE"))
		  System.out.println("err");
		else
		  System.out.println("gut, gut");
		
	}

}

>>>
gut, gut
>>>
```

<a href='#^'>^^^</a>

1.08

```java
/**
 * Definiáljuk a pi-t egy változóba a main függvényben
 */

package pogrammingPackage;
public class Programming {
	public static void main(String[] args) {
		double pi = 3.14;	
				
		System.out.println(pi);
		
	}

}

>>>
3.14
>>>
```

<a href='#^'>^^^</a>

1.09

```java
/**
 * Definiáljunk egy szöveges változót ami a következőt tárolja: 
 * "Value of the "pi" approximately: [valueOfPI]" a main függvényben
 */

package pogrammingPackage;
public class Programming {
	public static void main(String[] args) {
		String val = "Value of the \"pi\" approximately: [valueOfPI]";	
				
		System.out.println(val);
		
	}

}

>>>
Value of the "pi" approximately: [valueOfPI]
>>>
```

<a href='#^'>^^^</a>

1.10

```java
/**
 * Hozzuk létre a számokat 1-től 5-ig, tároljuk le azokat változókba, 
 * majd hozzunk létre egy 6. változó az előző számok összegének tárolására
 * 
 */

package pogrammingPackage;
public class Programming {
	public static void main(String[] args) {
		int one = 1;
		int two = 2;
		int three = 3;
		int four = 4;
		int five = 5;
		int six;
		
		six = (one+two+three+four+five);
				
		System.out.println(six);
		
	}

}

>>>
15
>>>
```

<a href='#^'>^^^</a>

1.11

```java
/**
 * Használjuk fel a 3. feladatban létrehozott változókat,
 * de most az alapérték legyen 6-tól 10-ig
 */
```

<a href='#^'>^^^</a>

1.12

```java
/**
 * Inicializáljunk egy változót úgy, hogy egy függvény visszatérési értékét vegye fel
 * 
 */

package pogrammingPackage;
public class Programming {
	public static void main(String []args){
        int y;
        y = 5*5;
        
        int x = y;
        System.out.print(x);
     }
}

>>>
25
>>>
```

<a href='#^'>^^^</a>

1.13

```java
/**
 * Hozzunk létre egy int változót keződérték nélkül. 
 * Növeljük meg az értékét 3-mal. Nézzük meg a futás eredményét.
 */

package pogrammingPackage;
public class Programming {
	public static void main(String []args){
        int y;
        y = y + 3;        
        System.out.print(y);
     }
}

>>>
Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
	The local variable y may not have been initialized

	at pogrammingPackage.Programming.main(Programming.java:5)
>>>
```

<a href='#^'>^^^</a>

1.14

```java
/**
 * Hozzunk létre egy függvényt ami visszaadja a pi értékét
 */

package pogrammingPackage;
public class Programming {
	public static void main(String []args){
        System.out.print(Math.PI);
     }
}

>>>
3.141592653589793
>>>
```

<a href='#^'>^^^</a>

1.15

```java
/**
 * Hozzunk létre egy függvényt ami kiírja dátum formátumba a paraméterként 
 * megkapott [year], [month], [day] változókat. * 
 */

package pogrammingPackage;
import java.util.Date;
public class Programming {
	   public static void main(String args[]) {
		      Date date = new Date();
		      System.out.println(date.toString());
		}
}

>>>
Sat Apr 28 22:08:43 CEST 2018
>>>
```

<a href='#^'>^^^</a>

1.16

```java
/**
 * Hozzunk létre 3 függvényt, paraméter és visszatérési érték nélkül. 
 * Mindegyik függvény tartalmazzon egy kiírató utasítást az első és
 * az utolsó utasításaként, hogy a futása elkezdődött illetve a futása befejeződött. 
 * Hívják meg a függvények egymást. Mi lesz a kimenete a programnak?
 */

```

<a href='#^'>^^^</a>

---

<h3 id='234'>2nd, 3rd, 4th</h3>

Basic Variables

```java
int a = 1
double b = 2.2
String c = "abc"
boolean d = true
```

<a href='#^'>^^^</a>

Function/method

```java
package test;
public class test {
    public static void main(String[] args) {
		
    int a = 2, b = 3;
		
     System.out.println(func(a, b));
         
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
3
>>>
```

<a href='#^'>^^^</a>

234.01

```java
/**
 * Definiáljunk egy-egy String változót a vezetéknévnek és a keresztnévnek. 
 * Fűzzük össze a két változót egy harmadikba.
 */

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

<a href='#^'>^^^</a>
 
234.02
 
```java
/**
 * Definiáljunk egy egész típust és adjunk neki értékül egy nem egész számot 
 * (pl.: 5,5). Mi történik?
 */

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

<a href='#^'>^^^</a>

234.03
 
```java
/**
 * Definiáljunk egy double és egy int típust. 
 * A double típus legyen egyenlő az int típusú változó kétszeresével.
 */

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

<a href='#^'>^^^</a>

234.04

```java
/**
 * A 3. feladatban létrehozott változókat most fordítva használjuk:
 * Az int típusú változó legyen egyenlő a double típus 3,14-szeresével. Mi történik?
 * 
 */

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

<a href='#^'>^^^</a>

234.05

```java
/**
 * Definiáljunk egy függvényt visszatérési érték és bemeneti paraméter nélkül. 
 * Írassuk ki vele, hogy "Hello World"
 */

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

<a href='#^'>^^^</a>

234.06

```java
/**
 * Definiáljunk egy kiírató függvényt, aminek nincs visszatérési 
 * értéke de egy bemenő String-et vár amit a Println() függvénnyel ki tudunk iratni.
 */
 
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

<a href='#^'>^^^</a>

234.07

```java
/**
 * Legyen egy függvény ami bemenetként 2 számot és egy boolean értéket vár. 
 * Ha a boolean igaz, akkor a két számot össszeadni, ha hamis akkor pedig kivonni kell. 
 * Hogyan nevezné el a paramétereket, hogy jól olvasható legyen a függvény?
 */

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

<a href='#^'>^^^</a>

234.08

```java
/**
 * Definiáljon egy átalakító függvényt, ami int típusból String típust csinál. 
 * Hogyan néz ki a függvény definíciója (visszatérési érték függvény név - paraméterek)?
 */

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

<a href='#^'>^^^</a>

234.09


```java
/**
 * Mi a baj a következő függvénnyel?
 */
```

```java
private static void getLengthOfString(String whatIsLength)
{
	int whatIsLength = 0;
	WhatIsLength = WhatIsLength.length();
	return whatIsLength;
}
```

```java
package pogrammingPackage;
public class Programming {
public static void main(String []args){
		
		String a = "a";
		String b = "bb";
		String c = "ccc";
        
	  System.out.println(getLengthOfString(a));
	  System.out.println(getLengthOfString(b));
	  System.out.println(getLengthOfString(c));
		
	  }
		
	  private static int getLengthOfString(String WhatIsLength)
	
	{
		int whatIsLength = 0;
		whatIsLength = WhatIsLength.length();
		return whatIsLength;
	}

}

>>>
1
2
3
>>>
```

<a href='#^'>^^^</a>

234.10

```java
/**
 * Mi lesz a kimenete a következő függvénynek:
 */
```

234.10.01

```java
static int whatIsTheRetVal()
{
	calculatedIntResult = 2;
	++calculatedIntResult;
	return calculatedIntResult++;
}
```

234.10.02

```java
static int whatIsTheRetVal()
{
	calculatedIntResult = 2;
	++calculatedIntResult;
	return ++calculatedIntResult;
}
```

```java
package pogrammingPackage;
public class Programming {public static void main(String []args){
		
        
		System.out.println(whatIsTheRetVal_1());
		System.out.println(whatIsTheRetVal_2());
		
	  }
	  
	static int whatIsTheRetVal_1()
	{
		int calculatedIntResult = 2;
		++calculatedIntResult;
		return ++calculatedIntResult;
	}
		
	static int whatIsTheRetVal_2()
	{
		int calculatedIntResult = 2;
		++calculatedIntResult;
		return calculatedIntResult++;
	}
	
}

>>>
4
3
>>>
```

<a href='#^'>^^^</a>

234.11

```java
/**
 * Definiáljunk egy függvényt ami kiírja a paramétereként kapott számot 
 * majd megnöveli azt egyel. Mielőtt a függvény végrehajtása befejeződik, 
 * hívja meg saját magát a megnövelt paraméter értékkel. Mi lesz a futás eredménye?
 */
 
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

<a href='#^'>^^^</a>

234.12

```java
/**
 * Definiáljunk egy függvényt ami visszaadja a 2 paramétere közül a nagyobbat.
 */

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

<a href='#^'>^^^</a>

234.13

```java
/**
 * Definiáljuk az osztás függvényt, ami 0-val való osztás esetén hibaértéket ad vissza
 * 
 */
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

<a href='#^'>^^^</a>

234.14

```java
/**
 * Implementáljuk az alábbi függvények tartalmát, 
 * hogy minden változó kombinációra helyes értéket adjon vissza:
 */

AND: boolean getAndLogicResult(boolean a, boolean b, boolean c);
OR: boolean getOrLogicResult(boolean a, boolean b, boolean c, boolean d);
NOT: boolean getNotLogicResult(boolean a);
```

<a href='#^'>^^^</a>

234.15

```java
/**
 * 
 * 
 */

```

<a href='#^'>^^^</a>

234.16

```java
/**
 * 
 * 
 */

```

<a href='#^'>^^^</a>

234.17

```java
/**
 * 
 * 
 */

```

<a href='#^'>^^^</a>

234.18

```java
/**
 * 
 * 
 */

```

<a href='#^'>^^^</a>

234.19

```java
/**
 * 
 * 
 */

```

<a href='#^'>^^^</a>

234.20

```java
/**
 * 
 * 
 */

```

<a href='#^'>^^^</a>

234.21

```java
/**
 * 
 * 
 */

```

<a href='#^'>^^^</a>

234.22

```java
/**
 * 
 * 
 */

```

<a href='#^'>^^^</a>

234.23

```java
/**
 * 
 * 
 */

```

<a href='#^'>^^^</a>

234.24

```java
/**
 * 
 * 
 */

```

<a href='#^'>^^^</a>

234.25

```java
/**
 * 
 * 
 */

```

<a href='#^'>^^^</a>

---

<h3 id='5th'>5th</h3>

5.01

```java
/**
 * Írassa ki az alábbi összehasonlítás eredményét: Ha 5 kisebb egyenlő mint 3 akkor "5<=3" egyébként "5>3" 
 */

public class HelloWorld{

     public static void main(String[] args) {
         
        int a = 5;
        
		if (a<=3)
		  System.out.println("5<=3");
		else
		  System.out.println("5>3");
		  
	}

}

>>>
5>3
>>>
```

<a href='#^'>^^^</a>

5.02

```java
/**
 * Negálja meg a fenti feltételt és úgy írassa ki az eredményét. 
 * Negálás után melyik ág futott le?
 */
 
public class HelloWorld{

     public static void main(String[] args) {
        
        int a = 5;
        
		if (!(a<=3))
		  {
		  System.out.println("5<=3");
		  }
		else
		  {
		  System.out.println("5>3");
		  }
		
	}

}

>>>
5<=3
>>>
```

<a href='#^'>^^^</a>

5.03

```java
/**
 * Implementáljon le egy függvényt ami az alábbi logikai kifejezés igazság értékét 
 * adja vissza, legyen A, B és C egy boolean bementi paramétere a függvénynek: 
 * ((!(!A && B)) || C) Mely A, B és C értékek esetén ad TRUE eredményt a függvény?
 */

boolean A = true;
boolean B = false;
boolean C = true;
```

<a href='#^'>^^^</a>

5.04

```java
/**
 * Implementáljon egy függvényt, ami két boolean paramétert vár 
 * és az OR logikai igazságtáblát valósítja meg, de csak az AND 
 * és a Negálás logikai műveletét használhatja.
 */

!(a && b) ≡ !a || !b
!(a || b) ≡ !a && !b
```

<a href='#^'>^^^</a>

5.05

```java
/**
 * Most implementáljon le egy hasonló függvényt, ami az AND 
 * logikai igazsságtáblát valósítja meg, de csak az OR és 
 * a Negálás logikai műveletét használhatja.
 */

!(a && b) ≡ !a || !b
!(a || b) ≡ !a && !b
```

<a href='#^'>^^^</a>

5.06

```java
/**
 * Implementáljon le egy függvényt, ami String-ként kap egy számot 
 * valamint int-ként is kap egy számot és visszaadja a kisebbet.
 */
 
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

<a href='#^'>^^^</a>

5.07

```java
/**
 * Implementálja le a következő logikai vizsgálatot a 
 * lehető legkevesebb feltétel vizsgálattal: Ha a paraméterül kapott szám kisebb mint 5, 
 * akkor írassuk ki, hogy "Param is smaller than 5", egyébként írassuk ki, hogy 
 * "Param is higher or equal than 5". Ha 10-től kisebb akkor írassuk ki, hogy 
 * "Param is smaller than 10", egyébként írassuk ki, hogy "Param is higher or equal than 10".
 */
 
public class HelloWorld{
     public static void main(String[] args) {

        int a = 11;
        
		if (a < 5) 
		  System.out.println("Param is smaller than 5 and Param is smaller than 10");
		else if (a >= 5 && a < 10)
		  System.out.println("Param is higher or equal than 5 and Param is smaller than 10");
		else
		  System.out.println("Param is higher or equal than 10");  
		
	}

}

>>>
Param is higher or equal than 10
>>> 
```

<a href='#^'>^^^</a>

---

<h3 id='6th'>6th</h3>

6.01

```java
/**
 * 
 * 
 */

```

<a href='#^'>^^^</a>

6.02

```java
/**
 * 
 * 
 */

```

<a href='#^'>^^^</a>

6.03

```java
/**
 * 
 * 
 */

```

<a href='#^'>^^^</a>

---

<h3 id='7th'>7th</h3>

* [OOP](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/07/OOP/JOOP/JOOP.MD)

7.01

```java
/**
 * Hozzunk létre egy Teszt Osztályt!
 */

```

<a href='#^'>^^^</a>

7.02

```java
/**
 * Definiáljunk a Teszt Osztályban hét darab String attribútumot, amely a hét napjaitt
 * fogja tartalmazni.
 */

```

<a href='#^'>^^^</a>


7.03

```java
/**
 * Adjunk a Teszt Osztályhoz egy metódust, ami egy int bemenetet vár és visszaadja a hét
 * megfelelő napjához tartozó változót. (1  „Hétfő”, 2  „Kedd”, 7  „Vasárnap”)
 * Milyen String-et ad vissza a függvény, ha a bemeneti paraméter nagyobb mint 7?
 */

```

<a href='#^'>^^^</a>

7.04

```java
/**
 * Példányosítsuk a Teszt Osztályunkat, majd olvassuk ki 
 * a hét 2., 5. és 13. napját. Írassuk ki az eredményt!
 */

```

<a href='#^'>^^^</a>

7.05

```java
/**
 * Hozzuk létre a Téglalap Osztályt!
 * Legyen az attribútuma a két oldalának hossza és legyen egy kerület és egy terület számító
 * függvénye. Példányosítsunk 3 téglalapot, adjuk meg oldalainak hosszát majd számoljuk ki a
 * kerületüket és a területüket egy ciklusban.
 */

```

<a href='#^'>^^^</a>

7.06

```java
/**
 * Implementáljunk egy biggerRectangle függvényt, ami 2 bemeneti téglalap közül
 * visszaadja a nagyobbat. Keressük meg a 3 téglalap közül a legnagyobbat!
 */

```

<a href='#^'>^^^</a>

7.07

```java
/**
 * Hozzunk létre egy Négyzet Osztályt, ami tárolja az oldalának a hosszát és legyen egy-
 * egy metódusa a kerület és a terület kiszámítására
 */

```

<a href='#^'>^^^</a>

7.08

```java
/**
 * Milyen összefüggés van a Négyzet és a Téglalap Osztály között? Hogyan lehet Négyzetet
 * létrehozni Téglalap segítségével?
 */

```

<a href='#^'>^^^</a>

7.09

```java
/**
 * Hozzunk létre egy Mosógép Osztályt. A Mosógéphez vannak előre megírt mosási opciók:
 *  KisMosás
 *  KözepesMosás
 *  NagyMosás
 * Milyen típusú attribútumban érdemes tárolni ezeket az opciókat?
 * Nem, nem String-ben! Gondolkozz, mi a hátránya a String-nek?
 */

```

<a href='#^'>^^^</a>

7.10

```java
/**
 * Legyen egy Autó Osztály!
 * Definiáljuk a súly, a fogyasztás, a lóerő és a gyártási évet. 
 * Találjon ki egy függvényt, ami
 * kiszámolja az autó árát az adatok függvényében:
 * Value_Of_Car := f(weight, consumption, power, production_year);
 */

```

<a href='#^'>^^^</a>

7.11

```java
/**
 * Hozzunk létre egy Ember Osztályt. Legyen egy Neve (String) és egy TV típusú
 * attribútuma.
 */

```

<a href='#^'>^^^</a>

7.12

```java
/**
 * Példányosítsunk egy Ember és egy TV Osztályt, majd rendeljük hozzá az Ember TV
 * attribútumához a létrehozott TV példányt. Vezérelje az Ember a hozzárendelt TV-t!
 */

```

<a href='#^'>^^^</a>

7.13

```java
/**
 * Nézzen utána, majd hozza létre az Ember Osztálynak egy Konstruktorát, a Név és a TV
 * paraméterekkel.
 */

```

<a href='#^'>^^^</a>

---
