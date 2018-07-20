
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [course manuals](https://github.com/ttltrk/PRG/blob/master/COUR_MAN.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Java Tech](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/JT/JT.MD) - [Java](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/OJM.MD) - [courses](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/CM/JT.MD)

---

### Learn Java (codecademy)

---

01. Introduction to Java

	01.001. Introduction to Java
	
		01.001.0001. What's your name?
		01.001.0002. Data Types I: int
		01.001.0003. Data Types II: boolean
		01.001.0004. Data Types III: char
		01.001.0005. Variables
		01.001.0006. Whitespace
		01.001.0007. Comments
		01.001.0008. Math I
		01.001.0009. Math II	
		01.001.0010. Relational Operators
		01.001.0011. Equality Operators
		01.001.0012. Generalizations
	
02. Conditionals and Control Flow

	02.001. Conditionals and Control Flow
	
		02.001.0001. Decisions
		02.001.0002. Boolean Operators: &&
		02.001.0003. Boolean Operators: ||  
		02.001.0004. Boolean Operators: !
		02.001.0005. Boolean Operators: Precedence
		02.001.0006. If Statement
		02.001.0007. If-Else Statement
		02.001.0008. If-ElseIf-Else Statement
		02.001.0009. Ternary Conditional
		02.001.0010. Switch Statement
		02.001.0011. Generalizations		
	
03. Object-Oriented Java

	03.001. Object-Oriented Java
	
04. Data Structures

	04.001. Data Structures

=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
01. 01. Introduction to Java
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
01.001. Introduction to Java
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

01.001.0001. What's your name?

Java is a programming language designed to build secure, powerful applications that run across multiple operating systems, 
including Linux, Mac OS X, and Windows. The Java language is known to be flexible, scalable, and maintainable.

We will begin with the fundamentals of Java programming: data types, arithmetic, and operators. 
We’ll learn a few concepts that you can apply to the programs you create. By the end of the course, 
you’ll be familiar with the basic building blocks of a Java program.

################################################################

----------------------------------------------------------------
/*
Let's get started by getting to know each other.

On line 4, type your name within double quotes between the parentheses like this:
*/


System.out.println("Gilberto");
Click Run to run the code.

public class YourName {
	public static void main(String[] args) {

		System.out.println("trk");

	}
}
----------------------------------------------------------------

>>>
trk
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

01.001.0002. Data Types I: int

Great job! You've already learned how to print text.

Creating more useful Java programs will likely require you to work with several additional types of data. 
Let's explore a few of them.

The first data type we will use is int.

int is short for integer, which are all positive and negative numbers, including zero.
This number could represent the number of visits a website has received or the number of programming languages you know.
The int data type only allows values between -2,147,483,648 and 2,147,483,647.

################################################################

----------------------------------------------------------------
/*
Type any whole number in between the parentheses of System.out.println();

int data types do not need to be typed within quotes, so you can avoid using quotes this time.
*/

public class DataTypes {
	public static void main(String[] args) {

		System.out.println(83);

	}
}
----------------------------------------------------------------

>>>
83
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

01.001.0003. Data Types II: boolean

Fantastic! You just printed an int data type.

The next data type we will use is the boolean.

A boolean is a data type that can only be either true or false.

################################################################

----------------------------------------------------------------
/*
Type either true or false between the parentheses of System.out.println(); to print a boolean value.
*/

public class DataTypesB {
	public static void main(String[] args) {

		System.out.println(true);

	}
}
----------------------------------------------------------------

>>>
true
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

01.001.0004. Data Types III: char

Perfect. Let's look at one more Java data type: char.

The char data type is used to represent single characters. That includes the keys on a keyboard that are used to produce text.

char is short for character and can represent a single character.
All char values must be enclosed in single quotes, like this: 'G'.

################################################################

----------------------------------------------------------------
/*
In between the parentheses of System.out.println(); type any single character of your choice. Make sure it's enclosed in single quotes!
*/

public class DataTypesC {
	public static void main(String[] args) {

		System.out.println('s');

	}
}
----------------------------------------------------------------

>>>
s
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

01.001.0005. Variables

The int, boolean, and char are fundamental data types of Java that we will see again later in the course.

Another important feature of Java (and of many programming languages) is the ability to store values using variables.

A variable stores a value.
In Java, all variables must have a specified data type.
We can assign a variable to a specified data type, like this:

int myLuckyNumber = 7;

The variable myLuckyNumber now stores the value 7 as an int type.

A semicolon ; is also used to end all Java single code statements. 
We will cover statements that should not end in a semicolon later in this course.

################################################################

----------------------------------------------------------------
/*
1.
Set the int variable myNumber equal to the value 42.
2.
Set the boolean variable isFun equal to true.
3.
Set the char variable movieRating equal to 'A'.
*/

public class Variables {
	public static void main(String[] args) {

		int myNumber = 42;
		boolean isFun = true; 
		char movieRating = 'A'; 

	}
}
----------------------------------------------------------------

>>>

>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

01.001.0006. Whitespace

Before we explore what we can do with variables, let’s learn how to keep code organized in Java.

Whitespace is one or more characters (such as a space, tab, enter, or return) that do not produce a visible mark or text. 
Whitespace is often used to make code visually presentable.

Java will ignore whitespace in code, but it is important to know how to use whitespace to structure code well. 
If you use whitespace correctly, code will be easier for you and other programmers to read and understand.

################################################################

----------------------------------------------------------------
/*
The given code is poorly formatted. Place System.out.println(isFormatted); on line 5 so that it is easier to read.
*/

public class WhiteSpace {
	public static void main(String[] args) {

		boolean isFormatted = false;
    System.out.println(isFormatted);

	}
}
----------------------------------------------------------------

>>>
false
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

01.001.0007. Comments

################################################################

A comment is text you want Java to ignore. Comments allow you to describe code or keep notes.

By using comments in the Java code, you may help yourself and even other programmers understand 
the purpose of code that a comment refers to.

In Java, there are two styles of comments: single line comments and multi-line comments.

Single line comments are one line comments that begin with two forward slashes:

// I'm a single line comment!

Multi-line comments are generally longer comments that can span multiple lines. They begin with /* and end with */ . Here's an example:

/*

Hello, 
Java! 

*/

----------------------------------------------------------------
/*
1.
The statement on line 4 prints out Noise!. Ask Java to ignore it by commenting it out. 
Place two forward slashes (//) at the beginning of line 4.
2.
Write a multi-line comment that begins anywhere after the single line comment you just wrote.
Again, the comment can say anything you like.
*/
---------------------------------------------

public class Comments {
	public static void main(String[] args) {

		//System.out.println("Noise!");
		
/*
szo
hi
*/
		
	}
}
----------------------------------------------------------------

>>>

>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

01.001.0008. Math I

Now let's try arithmetic in Java. You can add, subtract, multiply, and divide numbers and store them in variables like this:

int sum = 34 + 113;
int difference = 91 - 205;
int product = 2 * 8; 
int quotient = 45 / 3;

################################################################

----------------------------------------------------------------
/*
Set the int variable myNumber equal to the product of two numbers.
*/

public class Arithmetic {
	public static void main(String[] args) {

		int myNumber = 5 * 5;
		System.out.println(myNumber);

	}
}
----------------------------------------------------------------

>>>
25
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

01.001.0009. Math II

Good work! Let's explore one more special math operator known as modulo.

The modulo operator - represented in Java by the % symbol - returns the remainder of dividing two numbers.
For example, 15 % 6 will return the value of 3, because that is the remainder left over after dividing 15 by 6.

################################################################

----------------------------------------------------------------
/*
Use the modulo operator to set the variable myRemainder equal to 2. You can use any two numbers that return a remainder value of 2.
*/

public class Modulo {
	public static void main(String[] args) {

		int myRemainder = 10 % 4;
		System.out.println(myRemainder);

	}
} 
----------------------------------------------------------------

>>>
2
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

01.001.0010. Relational Operators

It looks like you're getting the hang of this! Let's explore another set of useful operators available in Java known 
as relational operators.

Relational operators compare data types that have a defined ordering, like numbers 
(since numbers are either smaller or larger than other numbers).

Relational operators will always return a boolean value of true or false.

Here are a few relational operators:

< : less than.
<=: less than or equal to.
>: greater than.
>=: greater than or equal to.

A relational operator is placed between the two operands (the terms that you want to compare using the relational operator). 
The result of a relational operation is printed out in the following statement:

System.out.println(5 < 7);

The example above will print out true because the statement "5 is less than 7" is true.

################################################################

----------------------------------------------------------------
/*
Use one of the relational operators above to compare any two integers.
*/

public class RelationalOperators {
	public static void main(String[] args) {

		System.out.println(7 > 3);

	}
}
----------------------------------------------------------------

>>>
true
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

01.001.0011. Equality Operators

You may have noticed that the relational operators did not include an operator for testing "equals to". 
In Java, equality operators are used to test equality.

The equality operators are:

==: equal to.
!=: not equal to.
Equality operators do not require that operands share the same ordering. 
For example, you can test equality across boolean, char, or int data types. 
The example below combines assigning variables and using an equality operator:

char myChar = 'A';
int myInt = -2;
System.out.println(myChar == myInt);

The example above will print out false because the value of myChar ('A') is not the same value as myInt ('-2').

################################################################

----------------------------------------------------------------
/*
Use any equality operator to directly compare two Boolean values. Do not declare any variables.
*/

public class EqualityOperators {
	public static void main(String[] args) {

		System.out.println(true != false);

	}
}
----------------------------------------------------------------

>>>
true
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

01.001.0012. Generalizations

Congratulations! You've learned some of the building blocks of Java programming. What can we generalize so far?

Data Types are int, boolean, and char.
Variables are used to store values.
Whitespace helps make code easy to read for you and others.
Comments describe code and its purpose.
Arithmetic Operators include +, -, *, /, and %.
Relational Operators include <, <=, >, and >=.
Equality Operators include == and !=.

A full understanding of these concepts is key to understanding the remainder of the Java course. Let's keep going!

################################################################

----------------------------------------------------------------
/*
1.
Write a single line comment anywhere you want. It can be anything! (Make sure it starts with //)
2.
Set the boolean variable isComplete to true.
3.
Set the int variable awesomeLevel equal to 121.
4.
Set the int variable epicLevel equal to awesomeLevel multiplied by 2.
5.
Uncomment the last line so that the console prints out the value of epicLevel.
*/

public class Generalizations {
	public static void main(String[] args) {

    //sl comment

		boolean isComplete = true;
		int awesomeLevel = 121;
		int epicLevel = awesomeLevel * 2;		
		System.out.println(epicLevel);
		

	}
}
----------------------------------------------------------------

>>>
242
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
02. Conditionals and Control Flow
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

=============================================================================================================
02.001. Conditionals and Control Flow
=============================================================================================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

02.001.0001. Decisions

So far, we've explored primitive data types and Java syntax. As we've seen, 
Java programs follow the instructions we provide them, such as printing values to the console.

We can also write Java programs that can follow different sets of instructions depending on the values 
that we provide to them. This is called control flow. In this lesson, we'll learn how to use control flow in our programs.

################################################################

----------------------------------------------------------------
/*
Take a look at the code in the editor. If it looks confusing to you right now, don't worry! After this lesson, 
you'll be able to read and write Java programs that use control flow.

Click Run to run the code.
*/

public class Conditionals {
	public static void main(String[] args) {


		if (1 < 4 && 0 > 5) {

			System.out.println("You ordered a cup of hot, mint tea.");

		} else if (21 <= 19 || 17 >= 28) {
			
			System.out.println("You ordered freshly squeezed orange juice!");

		} else if ( !(true == true) ) {

			System.out.println("You ordered hot cocoa!");

		} else {

			System.out.println("You ordered a cup of Java!");

		}

		char answerChoice = 'C';

		switch (answerChoice) {

			case 'A': System.out.println("You answered: " + answerChoice + ". Please try again.");
								break; 

			case 'B': System.out.println("You answered: " + answerChoice + ". Please try again.");
								break;

			case 'C': System.out.println("You answered: " + answerChoice + ". That is correct!");
								break;

			case 'D': System.out.println("You answered: " + answerChoice + ". Please try again.");
								break;

			default:
				System.out.println("Please select a valid answer choice.");

		}


	}
}
----------------------------------------------------------------

>>>
You ordered a cup of Java!
You answered: C. That is correct!
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

02.001.0002. Boolean Operators: &&

Let's look at a set of operators that let us use control flow in our programs. These operators are called Boolean operators.

There are three Boolean operators that we will explore. Let's start with the first one: and.

The and operator is represented in Java by &&.
It returns a boolean value of true only when the expressions on both sides of && are true.
For example, the code below shows one outcome of the Boolean operator &&:

// The following expression uses the "and" Boolean operator
System.out.println(true && true); // prints true
The code below shows the rest of the possible outcomes of the Boolean operators: &&:

// The following expressions use the "and" Boolean operator
System.out.println(false && false); // prints false
System.out.println(false && true); // prints false
System.out.println(true && false); // prints false
We can also use the Boolean operator && with Boolean expressions such as the following:

System.out.println(2 < 3 && 4 < 5);
The example above will print out true because the statements "2 is less than 3" and "4 is less than 5" are both true.

################################################################

----------------------------------------------------------------
/*
Use the && operator and any two Boolean expressions of your choice between the parentheses of System.out.println();
in order to print out a value of true or false to the console.
*/

public class And {
	public static void main(String[] args) {

		System.out.println(true && true);
		
	}
}
----------------------------------------------------------------

>>>
true
>>>

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

02.001.0003.

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

02.001.0004.

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

02.001.0005.

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

02.001.0006.

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

02.001.0007.

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

02.001.0008.

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

02.001.0009.

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

02.001.0010.

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

02.001.0011.

################################################################

################################################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
03. 03. Object-Oriented Java
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
04. 04. Data Structures
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


