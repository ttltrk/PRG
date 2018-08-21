
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [course manuals](https://github.com/ttltrk/PRG/blob/master/COUR_MAN.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/CM/JT.MD) - [Programozzteis](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/PT.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/JT/JT.MD) - [Java](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/OJM.MD)

---

### Java - PT

---

Meetings

* [1st](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/01/1st.md)
* [2nd-3rd-4th](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/2nd.MD)
* [5th](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/05/05.MD)
* [6th](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/06/06.MD)
* [7th](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/07/07.MD)

---

 * [test sample]()

---

* [src - programozz te is](http://programozzteis.hu/)

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

1.01

```java
/**
 * Szabja testre az Eclipse nézetét: Csak a "Console" és az 
 * "Outline" ablakokat tartsa meg valamint adja hozzá a "Search View"-t
 */

use the ```minimize``` button

window --> show view
```

1.02

```java
/**
 * Mit lát az Outline View-ban? Hogyan tud fájlon belül keresni?
 */

package + class

expand, collapse
```

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

1.05

```java
/**
 * Minek a rövidítése a JRE és mit jelent? Mi az a JVM?
 */

JRE

The Java Runtime Environment (JRE) is a set of software tools for development of Java applications. It combines the Java Virtual Machine (JVM), platform core classes and supporting libraries.

JRE is part of the Java Development Kit (JDK), but can be downloaded separately. JRE was originally developed by Sun Microsystems Inc., a wholly-owned subsidiary of Oracle Corporation. 

Also known as Java runtime.

JVM

A Java virtual machine (JVM) is an abstract computing machine that enables a computer to run Java programs as well as programs written in other languages and compiled to Java bytecode. There are three notions of the JVM: specification, implementation, and instance. 
```

1.06

```java
/**
 * Melyik JRE Package-ben van benne a System println függvénye?
 * 
 */

JRE System Library --> rt.jar --> java.io --> PrintStream.class --> println()
```

1.07

```java
/**
 * 
 * 
 */


```

1.08

```java
/**
 * 
 * 
 */


```

1.09

```java
/**
 * 
 * 
 */


```

1.10

```java
/**
 * 
 * 
 */


```

1.11

```java
/**
 * 
 * 
 */


```

1.12

```java
/**
 * 
 * 
 */


```

1.13

```java
/**
 * 
 * 
 */


```

1.14

```java
/**
 * 
 * 
 */


```

1.15

```java
/**
 * 
 * 
 */


```

1.16

```java
/**
 * 
 * 
 */


```

---
