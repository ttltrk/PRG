
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD)

###### [PY](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [JV](https://github.com/ttltrk/PRG/blob/master/JAVA/JAVA.MD) - [C](https://github.com/ttltrk/PRG/blob/master/C/C.MD) - [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD) - [SH](https://github.com/ttltrk/ELSE/blob/master/M/UX/UX.MD) - [PL](https://github.com/ttltrk/PRG/blob/master/PERL/PL.MD) - [DS](https://github.com/ttltrk/ELSE/blob/master/DATA/DS/DS.MD) - [DO](https://github.com/ttltrk/ELSE/blob/master/DOCKER/DOCKER/DOCKER.MD) || [ENG](https://github.com/ttltrk/ELSE/blob/master/LAN/ENG/LE.MD) - [DE](https://github.com/ttltrk/ELSE/blob/master/LAN/GER/DUO_GER.MD) - [SP](https://github.com/ttltrk/ELSE/blob/master/LAN/SP/SP.MD) - [FR](https://github.com/ttltrk/ELSE/blob/master/LAN/FR/FR.MD) - [TR](https://github.com/ttltrk/ELSE/blob/master/LAN/TR/TR.MD) - [LA](https://github.com/ttltrk/ELSE/blob/master/LAN/LATIN/LATIN.MD) - [ESP](https://github.com/ttltrk/ELSE/blob/master/LAN/ESP/ESP.MD) || [Tools](https://github.com/ttltrk/ELSE/blob/master/M/TOOLS/TOOLS.MD)

---

<h3 id='^'>Java</h3>

---

* <a href='#hw'>hello world</a></br>
* <a href='#userinput'>user input</a></br>
* <a href='#functions'>functions</a></br>
* <a href='#ifelse'>if-else</a></br>
* <a href='#for'>for</a></br>
* <a href='#while'>while</a><br>

---

<h3 id='hw'>hello world</h3>

```java
public class ttt {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}

>>>
Hello World
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='userinput'>User input</h3>

```java
import java.util.Scanner;  // Import the Scanner class

public class ttt {
    public static void main(String []args){
        Scanner myObj = new Scanner(System.in);  // Create a Scanner object
        System.out.println("Enter username");

        String userName = myObj.nextLine();  // Read user input
        System.out.println("Username is: " + userName);  // Output user input
    }
}

>>>
Enter username
trk
Username is: trk
>>>
```

```java
import java.util.Scanner;  // Import the Scanner class

public class ttt {
    public static void main(String []args){
        Scanner myObj = new Scanner(System.in);  // Create a Scanner object
        System.out.println("Enter username");
        System.out.println("Enter age");


        String userName = myObj.nextLine();  // Read user input
        String userAge = myObj.nextLine();  // Read user input

        System.out.println("Username is: " + userName);  // Output user input
        System.out.println("User age is: " + userAge);  // Output user input

    }
}

>>>
Enter username
Enter age
trk
36
Username is: trk
User age is: 36
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='functions'>functions</h3>

```java
public class ttt {
    public static void main(String []args){
        int param1 = 3, param2 = 2;
        boolean param3 = false;
        
        System.out.println(first(param1, param2, param3));        
    }
    
    private static int first(int param1, int param2, boolean param3) {
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

```java
public class ttt {
    public static void main(String []args){
        int param1 = 4, param2 = 2;
        boolean param3 = false;
        
        second(param1, param2, param3);        
    }
    
    private static void second(int param1, int param2, boolean param3) {
        if (param3 == true)
            System.out.println(param1+param2);
        else
            System.out.println(param1-param2);
    }
}

>>>
2
>>>
```

<a href='#^'>^^^</a>

---

