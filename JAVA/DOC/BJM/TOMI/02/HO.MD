
---

2nd HO

---

```java
1. Definiáljunk egy-egy String változót a vezetéknévnek és a keresztnévnek. Fűzzük össze a két változót egy harmadikba.

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

```
2. Definiáljunk egy egész típust és adjunk neki értékül egy nem egész számot (pl.: 5,5). Mi történik?
3. Definiáljunk egy double és egy int típust. A double típus legyen egyenlő az int típusú változó kétszeresével.
4. A 3. feladatban létrehozott változókat most fordítva használjuk: Az int típusú változó legyen egyenlő a double típus 3,14-szeresével. Mi történik?
5. Definiáljunk egy függvényt visszatérési érték és bemeneti paraméter nélkül. Írassuk ki vele, hogy "Hello World"
6. Definiáljunk egy kiírató függvényt, aminek nincs visszatérési értéke de egy bemenő String-et vár amit a Println() függvénnyel ki tudunk iratni.
7. Legyen egy függvény ami bemenetként 2 számot és egy boolean értéket vár. Ha a boolean igaz, akkor a két számot össszeadni, ha hamis akkor pedig kivonni kell. Hogyan nevezné el a paramétereket, hogy jól olvasható legyen a függvény?
8. Definiáljon egy átalakító függvényt, ami int típusból String típust csinál. Hogyan néz ki a függvény definíciója (visszatérési érték - függvény név - paraméterek)?
9. Mi a baj a következő függvénnyel?
	private static void getLengthOfString(String whatIsLength)
	{
		int whatIsLength = 0;
		WhatIsLength = WhatIsLength.length();
		return whatIsLength;
	}
	Javítsa ki!
	
10. Mi lesz a kimenete a következő függvénynek:
		static int whatIsTheRetVal()
		{
			calculatedIntResult = 2;
			++calculatedIntResult;
			return calculatedIntResult++;
		}
11. Definiáljunk egy függvényt ami kiírja a paramétereként kapott számot majd megnöveli azt egyel. Mielőtt a függvény végrehajtása befejeződik, hívja meg saját magát a megnövelt paraméter értékkel. Mi lesz a futás eredménye?
12. Definiáljunk egy függvényt ami visszaadja a 2 paramétere közül a nagyobbat.
13. Definiáljuk az osztás függvényt, ami 0-val való osztás esetén hibaértéket ad vissza
14. Implementáljuk az alábbi függvények tartalmát, hogy minden változó kombinációra helyes értéket adjon vissza:
		- AND: boolean getAndLogicResult(boolean a, boolean b, boolean c);
		- OR: boolean getOrLogicResult(boolean a, boolean b, boolean c, boolean d);
		- NOT: boolean getNotLogicResult(boolean a);
15. Hozzunk létre egy függvényt, ami meghatározza, hogy a paraméterként kapott szöveg, hosszabb-e mint a második paraméterként megkapott limit.
16. Implementáljuk le az osztályozó függvényt, ami bemenetként 4 paramétert vár az alábbi szintaxissal:
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
17. Implementáljon egy függvényt ami a bemeneti paraméterről eldönti, hogy páros-e vagy páratlan és az eredményt írja ki a képernyőre.
18. Mi lesz a program futásának eredménye?
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
19. Hozzuk létre az alábbi függvényt:
		static int getResult()
		{
			return (4294967300);
		}
	Milyen visszajelzést ad az Eclipse? Miért?
20. Készítsük el a void swap(int number1, int number2) függvényt ami megcseréli a két paraméter értékét. Írassa ki az eredeti és az új értékeit is a paramétereknek.
21. Számoljuk ki a számok összegét 1-től 100-ig, úgy, hogy csupán egyetlen függvényt használjunk fel az összegzéshez, ami az alábbi szintaxissal rendelkezik:
		/**
		 * @param number1
		 * 		First number in the summary
		 * @return
		 * 		Summary result from number1 to 100
		 */
		public int summary(int number1);
	Ne adja össze a számokat egyesével!
22. Számolja ki a Fibonacci-számsorozat első X elemét egyetlen függvény segítségével. A számsorozat első két eleme ismert: 0 és 1 
23. Ha egy falu népessége jelenleg X és minden évben Y%-al csökken a népesség, akkor mikorra fog teljesen elnéptelenedni a falu? Implmenetáljon erre egy algoritmust.
24. Definiáljuk a swap() függvényt. Hozzunk létre két változót a main()-ben, majd hívjuk meg a swap() függvényt majd a swap() függvény lefutása után a main() függvényben ellenőrizzük le a két változó értékét. Mit látunk? Magyarázza meg az eredményt!
25. Számoljuk meg az "i" betűk számát az alábbi String-ben: "This is a String":
		- Ha van benne "i" betű, akkor írjuk ki a pontos darabszámot
		- Ha nincs benne "i" betű, akkor azt írjuk ki, hogy a keresett betű az adott szövegben nem megtalálható
 ```
 
 ---
