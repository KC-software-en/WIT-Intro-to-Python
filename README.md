# Introduction to Python Programming for Beginners – Women in Tech Edition 

🐍 Welcome to the Intro to Python Workshop! This beginner-friendly repo is your launchpad into Python programming—packed with hands-on exercises, clear examples, and everything you need to start coding with confidence. 

**Note: Participants will need a free GitHub account to access the online development environment. The class code and exercises will be hosted in a GitHub repository, and a Visual Studio Code Codespace will be available for everyone – no setup required!**

## Setup & Preparation
GitHub signup [documentation](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)

GitHub Codespace setup [example](https://youtu.be/n9p25TLvCNY?si=n4xYebu6deHC-unL)

## Background
Python is an object-oriented coding language that was developed by Guido van Rossum in the late 1980s. Python is famed for its human readability making it an ideal first language to learn. From there learning other coding languages can become easier to grasp. Python is a popular progamming language today that you can find in Web Development, AI and Data Science to name a few.

You might be wondering to what does object-oriented programming (OOP) refer. Python is called an object-oriented language because it lets us group data and actions together into something called an "object" Think of an object as what you would find in the real world. For example, a cat has information such as its name, breed and age. The cat also has actions such as sleeping, meowing and scratching.

In Python you can create a class which acts as a general blueprint and name it, for example, cat. Then make objects from it, for example, Snowbell and Merv. This helps keep your code neat and easy to reuse, especially as your programs grow. Now don't worry if this sounds a bit like gibberish. OOP is a topic that is explored after you have advanced your knowledge as a beginner.

# Building Blocks of Python

## Psuedocode
Psuedocode is an informal method of stating what you want the code to do. Here you visual the task and the steps to complete it. Essentially this is the plan for an algorithm carried out by a computer. That is to say algorithms are the steps. Ensure that the algorithm has an input, output and very clear steps. Now bear in mind that this is simply planning and not the actual coding language. Psuedocode guides the comments you will document to explain the actual Python code.

E.g.

*Problem: write a program that prints "even" or "odd" depending on whether the number input is divisable by two without a remainder.*

+ Psuedocode solution (with no particular format):

    ```
    request an integer input from the user
    
    store the input in a variable named, "number"

    check that the input was an integer

    if the "number" was not an integer

        request new input

    else

        store the result as "quotient"

        divide the "number" by 2 to calculate the "quotient"

    if the "quotient" is zero

        store the "interpretation" as even

        print out "interpretation"

    else

        store the "interpretation" as odd

        print out "interpretation"
    ```

**Go to session_1_task.py and complete the psuedocode for your selected task**

+ Open your codespace.
+ Install Python if prompted by a pop-up.
+ Open the command prompt terminal (should open automatically).
+ Navigate to the directory containing the first task.
+ Run the following commands to navigate there:
    + `dir` and Enter to check your directory contains the README.md and Building Blocks of Python.
    + `cd Buil` followed by the tab button to automatically fill the directory and then press Enter.
        + if you don't have a keyboard, type the full `cd Building\ Blocks\ of\ Python/` and press Enter.
    + `dir` again and Enter to check if you can find session_1_task.py in the list of files output.
    + `code session_1_task.py` to open the file or click on the file name in the left side panel.

## Comments 

A comment is an explanation of Python code and it can be placed anywhere in a Python program. The comment is always ignored by the computer while running the code and is solely meant for the human reading the file. Write a comment in a Python program by adding a '#' at the start of the line. 

E.g. 

`# This is a comment`

There are two types of comments depending on the their placement.
If you want the comment to precede your code, refer to it as a block comment. A comment can also be placed on the same line as the code, after it, as an inline comment.

E.g.

`# This is a block comment`

`print("Hello,world")`

E.g.

`print("Hello,world") # This is an inline comment`

### Complete first sub-section of session 1 task

+ **Go to session_1_task.py and complete the comments for your selected task**

## Variables
A Python variable can be described as the location where data was stored. A variable is the name of the data that will be used to refer to the data during an algorithm. Ensure the following when naming a variable:

1. Use only lowercase letters.

1. Use snake case for longer variable names, e.g. number_of_pets, acccording to the Python Enhancement Proposals (PEP) 8 style guide. Thus, replace spaces with undercores.

1. Use a descriptive name relevant to the program algorithm created and to the value it refers.

1. A variable name may consist of letters, numbers, and underscores. However, it may only begin with either a letter or underscore.

1. A Python keyword cannot be used as variable name, e.g. print = "Sam". It was predefined and cannot be redefined by a coder. Python will pick it up as the function to which it may refer.

E.g.

`cat = "Snowball"`

Variables are useful in keeping track of different information. _From the example above, cat is the variable name which stores the cat name "Snowball" as data._ 

There are various **data types** from which you can consider using as you assign data to a variable. These can comprise:
1. Char
1. String
1. Integer
1. Float
1. Boolean

### Char

A char refers to a single character. This could be a letter, number, punctuation or special character. For example, A, 2, !, #.
You could use a char to store the grade for a student, for example, `grade = "B"; people = 3`.

### String

A string is a list of characters. For example, use it to store a name as `cat = "Snowball"`. Python detects a string with the presence of inverted commas ("").

### Integer

An integer is a whole number (i.e. no decimal or fraction included). For example, store the number of students at a career fair as `num_of_students = 56`. Python detects an integer by the presence of a whole number.

### Float
A float is a number that contains a decimal amount, for example, `cost = 14.90`. Python detects a float by the presence of a decimal point.

### Boolean
A boolean can only store one of two values - either True or False. This means that an outcome only has two possibities. Note the **capitalisation** of a boolean. Python only recognises a boolean with its capitalised value.

**Check the data type of a variable with the built-in type() function**

E.g. 

```
num_of_students = 56
print(type(num_of_students)) 
output:
<class 'int'>
```

E.g. 

```
num_of_students = "56"
print(type(num_of_students)) 
output:
<class 'str'>
```

_Take note of the above example._ You may find yourself with an error because the data type used through out your algorithm cannot perform certain actions. For example, you cannot perform mathematical operations on a number stored as a string. 
The solution? Cast your data type. This essentially means converting your data type.

These are the available casting functions:
1. int()
1. str()
1. float()

An argument is the value that the casting commands will use to act. Simply place the variable name as the argument inside the brackets. 

E.g.
```
num_of_students = "56"
int(num_of_students)
print(type(num_of_students)) 
output:
<class 'int'>
```

The above conversion will allow for addition operations, for example:

```
invited_guests = 29
plus_1_guests = "13"
total_guests = invited_guests + int(plus_1_guests)
output:
42
```


### Input and Output

Another important part of an algorithm is the **input and output**. A user sends input to the computer via a mouse, keyboard or touchpad. Output is the information a computer displays to the user after being transferred from it via a screen, printer or audio device.

Lets look at the previous algorithm to identify the input and output.

E.g.

*Problem: write a program that prints "even" or "odd" depending on whether the number input is divisable by two without a remainder.*

+ Psuedocode solution (with no particular format):

    ```
    request an integer input from the user
    
    store the input in a variable named, "number"

    check that the input was an integer

    if the "number" was not an integer

        request new input

    else

        store the result as "quotient"

        divide the "number" by 2 to calculate the "quotient"

    if the "quotient" is zero

        store the "interpretation" as even

        print out "interpretation"

    else

        store the "interpretation" as odd

        print out "interpretation"
    ```

From the above example, input is the "number" and output is "interpretation."

### **How to get input and output**

Now I am going to introduce you to a few built-in Python functions:

+ `input()`
+ `print()`

As a programmer, there may come time when you need a user's input. Place the input function in your code when you require the user to enter information with a keyboard. Store the information with a variable name to use it later in the program.

E.g.

`breed = input("What is the breed of your cat?: ")`

Notice the variable name "breed", the input function and the argument placed within the brackets. An argument is the value that the print command will use to act.

The "" in the brackets indicate that the data a user inputs will store as a string data type (i.e. a list of characters) but more on data types later.

+ _**Note that the program pauses until after the user enters information and presses Enter**_

The print function will display information to the user on a screen.

E.g.

`print(breed)` # will output the breed variable that the user entered.

E.g. 

`print("Hello, World!")` # will output the sentence in the argument.

### **_An important note on syntax_**

The way you write your code will make or break the running of a Python program. Python has syntax rules that, when you do not follow them, a syntax error raises in your terminal.

Some common syntax errors include:
+ Not closing a bracket, for example, `print("Hello, World!"`
+ Not closing the inverted commas, for example, `print("Hello, World!)`
+ Incorrect case, for example, `Print("Hello, World!")`

Python is case-sensitive so be sure to check your uppercase and lowercase letter placements.

If an error occurs and the program fails, follow up with debugging. Debugging is the process to resolve the error. The terminal will name the type of error (e.g. SyntaxError) and the line where the error occurs. This is very helpful to locate and update the code to ensure that the program runs uninterrupted.


### Resources
1. [PEP 8](https://peps.python.org/pep-0008/#introduction) style guide