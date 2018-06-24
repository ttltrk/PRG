
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [course manuals](https://github.com/ttltrk/PRG/blob/master/COUR_MAN.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/CM/JT.MD) - [Java - PT](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/JJ.MD) - [6th meet](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/BJM/TOMI/06/06.MD) 

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/JT/JT.MD) - [Java](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/OJM.MD)

---

### Java Ciklusok

---

* [Python ciklusok](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/03_PY_ST/PY_ST.MD)

---

Mire jók a ciklusok?

Adjuk össze a számokat 0-tól 10-ig. Hogyan csinálnád?

```java
int result = 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10;
```

És ha kettesével 0-tól 10000-ig? Ezt már kicsit tovább tartana kézzel leírni…
Már az előző példa is fárasztó, ráadásul sok a hibázási (félregépelési) lehetőség. De hogyan lehetne ezt jobban csinálni?

Ismerem a peremfeltételeket:

```
a) Első szám: 0
b) Utolsó szám: 10
c) Lépésköz: 1
```

VAGY

```
a) Első szám: 0
b) Utolsó szám: 10000
c) Lépésköz: 2
```

A jó hír, hogy már mások is észrevették ezt a nehézséget, ezért létre is hoztak erre egy nyelvi elemet. Sőt rögtön létrehoztak még kettőt, 
hogy több esetet tudjanak lefedni.
A fenti formulát kicsit azonban átalakították, hogy ne csak számokra működjön a dolog. Az új megközelítésben egy ciklus addig működik, 
amíg a ciklusnak megadott feltétel IGAZ! értéket ad vissza.

Két fajta ciklus létezik és azon belül összesen három:

```
a) Elől tesztelő ciklus - A feltétel ellenőrzése a lefutás előtt megtörténik.
I. FOR Ciklus
II. WHILE Ciklus
```

```
b) Hátul tesztelő ciklus - A feltétel ellenőrzése csak a lefutás után történik meg, tehát egyszer biztosan lefut!
III. DO_WHILE Ciklus
```

---

### A FOR Ciklus

A FOR Ciklus áll a legközelebb a fenti példához, a számokkal való Ciklusokhoz. Ehhez nyelvi segítséget is kapunk, három részből áll:

```
a) INICIALIZÁCIÓ - Ciklusváltozó kezdőértékének beállítása. Csak egyszer fut le!
b) FELTÉTEL - A Feltételvizsgálat. A ciklus addig tart, amíg a feltétel IGAZ!
c) FRISSÍTÉS - Megadott változók értékének változtatása, minden újabb ciklus előtt.
```

```java
for(INITIALIZATION; CONDITION_CHECK; UPDATE)
  {
  // do something
  }
```

Nézzük meg a fenti példát:

```java
int index = 0;
int result = 0;

for(index = 0; index <= 10; index++)
  {
  result += index;
  }
```

A fenti ciklus addig fut, amíg index <= 10, tehát, amikor az index változó 11 lesz, akkor a ciklus megáll, kilép  A result változóhoz 
hozzáadott utolsó szám a 10 lesz!

---

### A WHILE Ciklus

Analóg módon működik a FOR Ciklussal, mindig átalakíthatóak egymásba! Extra magyarázat nélkül következzen a nyelvi formula:

```java
while(CONDITION_CHECK)
  {
  // do something
  }
```

Ebben az esetben a ciklusváltozó növeléséről mindig nekünk kell gondoskodnunk!

Nézzük meg itt is a fenti példánkat:

```java
int index = 0;
int result = 0;

while(index <= 10)
  {
  result += index;
  index++;
  }
```

---

### A DO_WHILE Ciklus

Nagyon hasonló a sima WHILE Ciklushoz, azonban hatalmas különbség, hogy nem Elől, hanem Hátul Tesztelő ciklus. Ez azt jelenti, hogy 
teljesen mindegy, ha a feltétel sohasem teljesülne, egyszer mindenképpen lefut a ciklus.
Én azt mondanám, hogy kezdő szinten inkább kerüljük a használatát. Egyrészről, mert amúgy sem használják túl gyakran, másodszor pedig itt 
már jobban oda kell figyelni mint egy WHILE Ciklusnál. Azért mindenképpen illik ismerni azonban elég, ha ismeri az ember, tudja hogyan 
működik.

```java
do
  {
  // do something
  } while(CONDITION_CHECK);
```

Az összeadásos példa pedig:

```java
int index = 0;
int result = 0;

do
  {
  result += index;
  index++;
  } while(index <= 10);
```

---

### Ciklusok megszakítása: ```BREAK```

Arra az esetre, ha valamilyen extra kilépési lehetőségre lenne szükség, létrehoztak egy megszakító utasítást:

```
break;
```

Ha a break utasítás meghívódik, akkor az aktuális ciklus megszakad és azonnal kilép, függetlenül az eredetileg megadott feltétel 
teljesülésétől.

Nézzünk erre egy példát. Adjuk össze a számokat 0-tól 10-ig, de 5-nél most lépjünk ki (bocsánat, kicsit erőltetett a példa):

```java
int index = 0;
int result = 0;

for(index = 0; index <= 10; index++)
  {
    result += index;
    if(index == 5)
      {
      break;
      }
  }
```

---
