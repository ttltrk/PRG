
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [course manuals](https://github.com/ttltrk/PRG/blob/master/COUR_MAN.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/CM/JT.MD) - [Java - PT](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/JJ.MD) - [2nd-3rd](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/2nd.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/JT/JT.MD) - [Java](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/OJM.MD)

---

### 2nd, 3rd and 4th HO

---

* [01 - 2 String osszefuzese](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/01/01.MD)
* [02 - int es double osszefuzese](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/02/02.MD)
* [03 - double int muveletek 1](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/03/03.MD)
* [04 - double int muveletek 2](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/04/04.MD)
* [05 - fuggveny hello world](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/05/05.MD)
* [06 - fuggveny kiiratasa](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/06/06.MD)
* [07 - szamok osszeadasa kieertekelese](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/07/07.MD)
* [08 - int-bol String](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/08/08.MD)
* [09 - fuggveny kijavitasa](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/09/09.MD)
* [10 - lepteto ciklus](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/10/10.MD)
* [11 - parameter megnovelese](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/11/11.MD)
* [12 - 2 parameter kozul a nagyobb](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/12/12.MD)
* [13 - osztas 0-val](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/13/13.MD)
* [14 - boolean osszehasonlitas](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/14/14.MD)
* [15 - paramaterek hosszanak osszehasonlitasa](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/15/15.MD)
* [16 - osztalyozo fuggveny](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/16/16.MD)
* [17 - modulo paros, paratlan](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/17/17.MD)
* [18 - fuggveny kiiratas](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/18/18.MD)
* [19 - fuggveny out of range](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/19/19.MD)
* [20 - void swap fuggveny](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/20/20.MD)
* [21 - szamok osszege 1-100](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/21/21.MD)
* [22 - fibonacci](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/22/22.MD)
* [23 - csokkeno nepesseg](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/23/23.MD)
* [24 - swap fuggveny](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/24/24.MD)
* [25 - charakterek szamolasa Stringben](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/02/25/25.MD)

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

NR !!

```java
package pogrammingPackage;
public class Programming {
	  public static void main(String []args){
	      
	      String test = "test";
	      int limit_1 = 3;
	      int limit_2 = 5;

	      
		  countLetters(test, limit_1);
		  countLetters(test, limit_2);

	    }
		
	    private static void countLetters(String param1, int param2) {
	    	
	    	if (param1.length() > param2)
	    	  System.out.println("ok");
	    	else
	    	  System.out.println("not ok");
	    	
		  
	  }
	  
	    
	}
>>>
ok
not ok
>>>
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

>>>
The literal 4294967299 of type int is out of range 
>>>

```

---

20. Készítsük el a void swap(int number1, int number2) függvényt ami megcseréli a két paraméter értékét. Írassa ki az eredeti és az új értékeit is a paramétereknek.

NR !!

```java
package pogrammingPackage;
public class Programming {
	  public static void main(String []args){
	      
	      int a = 1;
	      int b = 2;
	      

	      
		  swap(a, b);
		  
	    }
		
	    private static void swap(int number1, int number2) {
	      int number3 = 0;
	      System.out.println(number1 + " " + number2);
	      number3 = number1;
	      number1 = number2;
	      number2 = number3;
	      System.out.println(number1 + " " + number2);
	      
		  
	  }
	  
	    
	}
	
>>>
1 2
2 1
>>>
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

```python
lst = range(1,101)
print(sum(lst))

>>>
5050
>>>
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
