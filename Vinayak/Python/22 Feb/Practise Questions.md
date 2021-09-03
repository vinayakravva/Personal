Q1.What is dynamically typed Language?
A language is dynamically-typed if the type of a variable is checked during run-time.Common examples of dynamically-typed languages includes JavaScript, Objective-C, PHP, Python, Ruby etc.

Q2.Can tuple be used as a dictionary key in python? (True or False)
False,A tuple can be used as a key so long as all of its elements are immutable.

Q3.What is the difference between list and tuple?
The list is better for performing operations, such as insertion and deletion. 	Tuple data type is appropriate for accessing the elements.

Q4.What is type casting in Python?
type is used to check the type/class of input recieved from the user.eg.integers/float/string.

Q5.How to comment multiple lines in python?
Enter # for each line as there is no multiple lines comment in python.

Q6.What does len() do?
The len() function returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string.

Q7.What are the built-in types of python?
The principal built-in types are numerics, sequences, mappings, classes, instances and exceptions.

Cloud-amigos

3.1   What is the difference between list and tuples in Python?
   List
	1 Lists are mutable	
	2 Implication of iterations is Time-consuming	
	3 The list is better for performing operations, such as insertion and deletion.	
	4 Lists consume more memory	
	5 Lists have several built-in methods	
	6 The unexpected changes and errors are more likely to occur	
   Tuple
	1 Tuple are immutable
	2 Implication of iterations is comparatively Faster
	3 Tuple data type is appropriate for accessing the elements
	4 Tuple consume less memory as compared to the list
	5 Tuple does no have must built-in methods.
	6 In tuple, it is hard to take place.


3.2   How python  is differ from other language?
	1.python is interpreted and dynamically typed language
	2.python code does not need to compile before run
	3.python is less expensiive 

3.3   Give types of if else  statement and explain it ? 
	 There are six types of If...else statement as follows
	1.if statement
	2.if ..else statement
	3.nested if statement
	4.if...elif...else ladder
	5.shorhand if
	6.shorthand if....else
		1.if statement
		 Decision making is required when we want to execute a code only if a certain condition is satisfied
		   i = 10
		   if i <10 :
		   print(" i is less than 10") 
		   print("i am inside of if block")
		2.if ..else statement
		 Decision making is required when we want to execute a code only if a certain condition is satisfied otherwise else part will execute
			num  = int(input("enter a number:"))
			if num % 2 == 0:
			print(f"{num} ,is even") 
			else: 
			print(f"{num} ,is odd")

		3.nested if statement
		  multiple conditions are checking  in nested format otherwise else part will execute
		4.if...elif...else ladder
		  1.If the condition for if is False, it checks the condition of the next elif block and so on.
	          2.If all the conditions are False, the body of else is executed.
		5.shorhand if
		  print given code in single line
		6.shorthand if....else
		 print given code with if and else condition

3.4.   what is a set?
	1. set is a datatype in python .it is used to store data 
	 2.Example
	        my_set = {1, 2, 3}
	        print(my_set)

3.5    What are the key features of Python?
	1. Easy to code: Python is a high-level programming language. ...
	2. Free and Open Source: ...
	3. Object-Oriented Language: ...
	4. GUI Programming Support: ...
	5. High-Level Language: ...
	6. Extensible feature: ...
	7. Python is Portable language: ...
	8. Python is Integrated language

3.6   What is type conversion in Python? 
	The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion.

3.7    Is indentation required in python? 
	Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very 		important. Python uses indentation to indicate a block of code

3.8   What are the built-in type does python provides?
	Python uses five numeric types: Booleans, integers, long integers, floating-point numbers, and complex numbers. Except for Booleans, all numeric objects are signed. All numeric types are 		immutable.

3.9   what is diff between if and shorthand if ?
	1.if
	  if check true condition with multiple line code
	2.shorthand if
	   if check true condition with multiple single code

3.10  How to iterate list?
	List is equivalent to arrays in other languages, with the extra benefit of being dynamic in size. In Python, the list is a type of container in Data Structures, which is used to store      		multiple data at the same time. Unlike Sets, lists in Python are ordered and have a definite count.
	There are multiple ways to iterate over a list in Python. 
	Let’s see all the different ways to iterate over a list in Python, and performance comparison between them.
	 Method #1: Using For loop 
	 Method #2: For loop and range()
	 Method #3: Using while loop 

3.11  How to access list, tuple, dictionary, set?
	1. list[212,"pooja"]
	  Lists are one of the most powerful tools in python. They are just like the arrays declared in other languages
	2.tuple(5,0)
	  A tuple is a sequence of immutable Python objects.
	3.dictionary{name : value}
	   dictionary is similar to hash or maps in other languages. It consists of key value pairs. The value can be accessed by unique key in the dictionary.
	4.set {}
	   Sets are used to store multiple items in a single variable.

3.12  Explain Datatypes of python?
	1. Integers.
	2. Floating-Point Numbers.
	3. Complex Numbers.
	4. Strings.
	5. Boolean

3.13  how identify datatypes is string or integer in python?
	1.string
	 "" or '' is indication og string
	2.integer
	  without any symbol integer is refered

3.14  Explain in detail tuple ?with example?
	1.tuple
	 A tuple is a sequence of immutable Python objects.
	2. Example 
	   thistuple = ("apple", "banana", "cherry")
           print(thistuple)

3.15   what are types of variable in python? Explain it.
	1. variable type can be an int, float, string, char, bool and many others.
