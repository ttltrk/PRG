
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [course manuals](https://github.com/ttltrk/PRG/blob/master/COUR_MAN.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/CM/JT.MD) - [Java - PT](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/JJ.MD) 

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/JT/JT.MD) - [Java](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/OJM.MD)

---

### Java OOP

---

A Java egy Objektum Orientált Programozási nyelv (Object Oriented Programming Language /OOP/). 
Ez egy nagyon fontos kijelentés, de mit jelent ez?
A Java úgy tekint a világra mint Objektumok (Osztályok) halmazára és a közöttük lévő interakciókra.

Objektum lehet:
* Az Auto
* Az Ember
* A Szék
* A Labda
* De még egy Webshop is
* De lehet ettől elvontabb is, például az Egész számok osztálya (Integer)
* Vagy egy Adatbázis

Az, hogy mit definiálunk egy Osztálynak, ez csak tervezési kérdés.

Nézzünk egy egyszerű elméleti példát:

Van egy Webshopom egy Kosár alkalmazással. A Kosár alkalmazásom célja, hogy különböző termékeket lehet összeválogatni, majd a végén lehet vásárolni, esetleg szerkeszteni a Kosár tartalmát. Hogyan terveznénk meg ezt a feladatot OOP megközelítéssel?

Az alábbiak szerint bontom apróbb Osztályokra a feladatot:

1. Kosár
  * Különálló Objektum
  * Tárolja a termékeket
  * Képes összegezni a kosárban lévő termékek árát
  * Lehet egy terméket eltávolítani a Kosárból
  * Lehet fizetni
  
2. Termékek
  * Minden Termék egy külön Objektum, egy külön Osztály
  
3. Weboldal
  * Felhasználói felület, amin keresztül a Kosár Osztály műveleti meghívhatóak

### Az Osztály a Java programozási nyelv legfontosabb nyelvi eleme! 

Az Osztály nem más mint egy különálló Objektum, az Objektum Orientált programozás alapja.

Egy Osztály két részből épül fel:
  * 1. Attribútumok (változók) - Az Osztály egy tulajdonságát tárolja
  * 2. Metódusok (függvények) - Az Osztály egy végrehajtható művelete

(de nem kötelező hogy legyen bármelyik is)

Például

Ember Osztály:

- Attribútumai:
  * Név
  * Telefonszám
  
- Metódusai:
  * telefonszamot_valt(uj_tsz)

### Hogyan kell létrehozni egy Osztályt a Java nyelvben?

```Class``` kulcsszóval 

```java
public class Human { 
  private String name; 
  private String phoneNumber;
  
  public void changePhoneNumber(String newPhoneNumber)
  { 
  this.phoneNumber = newPhoneNumber;
  }
}
```

Íratlan szabály:

```
1 Osztály / java fájl
```

### Példányosítás (Instantiation):

Az Osztály nem más mint egy típusdefiníció, önmagában nem értelmezhető. Az Osztályból létre kell hozni egy példányt amely valóban egy élő példánya az Osztálynak.

Például
  * az Ember Osztály egy példánya a Bajor Tamás nevű Ember
  * Egy másik példányának a neve Tóth Béla.

Az Osztály egy példányát, mindig a ```new``` kulcsszóval hozzuk létre:

```java
Human humanExample = new Human();
```

Osztály egy adott példányának saját magára való hivatkozás a saját függvényén belül:
```this``` kulcsszóval

Könnyebb megmutatni, mint elmagyarázni. Lásd a példában

---

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
