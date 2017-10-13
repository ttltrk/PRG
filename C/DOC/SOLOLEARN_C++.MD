
## C++ Tutorial
#### SOLOLEARN.COM

-------------------------------------

### 01. Basic Concepts

  ##### 01.001. What is C++
  ##### 01.002. Hello World!
  ##### 01.003. Getting the Tools
  ##### 01.004. Printing a Text
  ##### 01.005. Comments
  ##### 01.006. Variables
  ##### 01.007. Working with Variables
  ##### 01.008. More on Variables
  ##### 01.009. Basic Arithmetic
  ##### 01.010. Assignment and Increment Operators
  ##### 01.011. Model 1 Quiz

### 02. Conditionals and Loops

### 03. Data Types, Pointers, Arrays

### 04. Functions

### 05. Classes and Objects

### 06. More On Classes

### 07. Inheritance & Polymorphism

### 08. Templates, Exceptions and Files

### 09. Challanges

--------------------------------------------------------

### 01. BASIC CONCEPTS

##### 01.001. What is C++

Welcome to C++

C++ is a general-purpose programming language.
C++ is used to create computer programs. Anything from art applications, music players and even video games!
C++ was derived from C, and is largely based on it.

C++ is a:

```
General Purpose programming language
```

##### 01.002. Hello World!

Your First C++ Program

A C++ program is a collection of commands or statements.

Below is a simple code that has "Hello world!" as its output.

```c++
#include <iostream>
using namespace std;

int main()
{
  cout << "Hello world!";
  return 0;
}
```

--------------------------------------------------------

Let's break down the parts of the code.
#include <iostream>

C++ offers various headers, each of which contains information needed for programs to work properly. 
This particular program calls for the header <iostream>.
The number sign (#) at the beginning of a line targets the compiler's pre-processor. 
In this case, #include tells the pre-processor to include the <iostream> header. 
The <iostream> header defines the standard stream objects that input and output data.

Fill in the blanks to include the <iostream> header:

#include <iostream>

-----------------------------------

Your First C++ Program

The C++ compiler ignores blank lines.
In general, blank lines serve to improve the code's readability and structure. 
Whitespace, such as spaces, tabs, and newlines, is also ignored, although it is used to enhance the program's visual attractiveness.

```c++
#include <iostream>
using namespace std;

int main()
{
  cout << "Hello world!";
  return 0;
}
```

In our code, the line using namespace std; tells the compiler to use the std (standard) namespace.
The std namespace includes features of the C++ Standard Library.

-----------------------------------

Fill in the blanks to use names from std namespace:
#include <iostream>
using namespace std;

-----------------------------------

Main

Program execution begins with the main function, int main().

```c++
#include <iostream>
using namespace std;

int main()
{
  cout << "Hello world!";
  return 0;
}
```

Curly brackets { } indicate the beginning and end of a function, which can also be called the function's body. 
The information inside the brackets indicates what the function does when executed.
The entry point of every C++ program is main(), irrespective of what the program does.

-----------------------------------

What is the starting point for a computer program?

>>>
Main function
>>>

-----------------------------------

Your First C++ Program

The next line, cout << "Hello world!"; results in the display of "Hello world!" to the screen.

```c++
#include <iostream>
using namespace std;

int main()
{
  cout << "Hello world!";
  return 0;
}
```

In C++, streams are used to perform input and output operations.
In most program environments, the standard default output destination is the screen. In C++, cout is the stream object used to access it. 
cout is used in combination with the insertion operator. 
Write the insertion operator as << to insert the data that comes after it into the stream that comes before.
In C++, the semicolon is used to terminate a statement. Each statement must end with a semicolon. 
It indicates the end of one logical expression.

-----------------------------------

Each instruction must end with a:

>>>
semicolon(;)
>>>

-----------------------------------

Statements

A block is a set of logically connected statements, surrounded by opening and closing curly braces.

For example:

{
  cout << "Hello world!"; 
  return 0;
}

You can have multiple statements on a single line, as long as you remember to end each statement with a semicolon. 
Failing to do so will result in an error.

-----------------------------------

Fill in the blanks to output "Hello, world!" on the screen:

cout << "Hello, world!";

-----------------------------------

Return

The last instruction in the program is the return statement. The line return 0; terminates the main() function and
causes it to return the value 0 to the calling process. A non-zero value (usually of 1) signals abnormal termination.

```c++
#include <iostream>
using namespace std;

int main()
{
  cout << "Hello world!";
  return 0;
}
```

If the return statement is left off, the C++ compiler implicitly inserts "return 0;" to the end of the main() function.
Tap Continue to learn more about functions, return, and other topics.

-----------------------------------

Rearrange the code blocks to form a valid C++ program:

int main() {
#include <iostream>
using namespace std;
int main() {
  cout << "Awesome!";
  return 0;
  }

-----------------------------------

##### 01.003. Getting the Tools

-----------------------------------

Getting the Tools

You can run, save, and share your C++ codes on our Code Playground, without installing any additional software.
Reference this lesson if you need to install the software on your computer.

You need both of the following components to build C++ programs.
1. Integrated Development Environment (IDE): Provides tools for writing source code. Any text editor can be used as an IDE.
2. Compiler: Compiles source code into the final executable program. 
There are a number of C++ compilers available. The most frequently used and free available compiler is the GNU C/C++ compiler.

Various C++ IDEs and compilers are available. We'll use a free tool called Code::Blocks, 
which includes both an IDE and a compiler, and is available for Windows, Linux and MacOS.
To download Code::Blocks, go to http://www.codeblocks.org/, Click the Downloads link, and choose "Download the binary release".
Choose your OS and download the setup file, which includes the C++ compiler (For Windows, it's the one with mingw in the name).
Make sure to install the version that includes the compiler.

-----------------------------------

Which two options do you need to write and run C++ programs?

>>>
IDE
Compiler
>>>

-----------------------------------

Getting the Tools

To create a project, open Code::Blocks and click "Create a new project" (or File->New->Project).
This will open a dialog of project templates. Choose Console application and click Go.

Go through the wizard, making sure that C++ is selected as the language.
Give your project a name and specify a folder to save it to.

Make sure the Compiler is selected, and click Finish.
GNU GCC is one of the popular compilers available for Code::Blocks.
On the left sidebar, expand Sources. You'll see your project, along with its source files. Code::Blocks 
automatically created a main.cpp file that includes a basic Hello World program (C++ source files have .cpp, .cp or .c extensions).

Click on the "Build and Run" icon in the toolbar to compile and run the program.

A console window will open and display program output.

Congratulations! You just compiled and ran your first C++ program!
You can run, save, and share your C++ codes on our Code Playground, without installing any additional software.
Reference this lesson if you need to install the software on your computer.

-----------------------------------

Which of the following is a C++ compiler?

>>>
GNU GCC
>>>

-----------------------------------

##### 01.004. Printing a Text

-----------------------------------

Your First C++ Program

You can add multiple insertion operators after cout.

cout << "This " << "is " << "awesome!";

>>>
This is awesome!
>>>

-----------------------------------

Fill in the blanks to print "I love C++":
  
cout << "I love C++";

>>>
I love C++
>>> 

-----------------------------------

New Line

The cout operator does not insert a line break at the end of the output. 
One way to print two lines is to use the endl manipulator, which will put in a line break.

#include <iostream>
using namespace std;

int main()
{
  cout << "Hello world!" << endl;
  cout << "I love programming!";
  return 0;
}

The endl manipulator moves down to a new line to print the second text.

>>>
Hello World!
I love programming!
>>>

-----------------------------------

What should be used to move to a new line?

>>>
endl
>>>

-----------------------------------

New Lines

The new line character \n can be used as an alternative to endl.
The backslash (\) is called an escape character, and indicates a "special" character.

Example:

#include <iostream>
using namespace std;

int main()
{
   cout << "Hello world! \n";
   cout << "I love programming!";
   return 0;
}

>>>
Hello world!
I love programming!
>>>

-----------------------------------

What is the symbol for moving to a new line (alternative to the endl)?

>>>
\n
>>>

-----------------------------------

New Lines

Two newline characters placed together result in a blank line.

#include <iostream>
using namespace std;

int main()
{
   cout << "Hello world! \n\n";
   cout << "I love programming!";
   return 0;
}

>>>
Hello world!

I love programming!
>>>

-----------------------------------

Fill in the blanks to print the words "hello" and "world" separated by a blank line:
  
cout << "hello \n\n";
cout << "world";

-----------------------------------

Multiple New Lines

Using a single cout statement with as many instances of \n as your program requires will print out multiple lines of text.

#include <iostream>
using namespace std;

int main()
{
   cout << " Hello \n world! \n I \n love \n programming!";
   return 0;
}

>>>
Hello
world
I
love
programming!
>>>

-----------------------------------

Fill in the blanks to print "I love C++" with each word in a new line:

cout << "I \n love \n C++";

