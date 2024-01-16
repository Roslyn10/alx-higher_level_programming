0x00-python-hello_world

0. Run Python file

	* Write a Shell script that runs a Python script
	* The Python file name will be saved in the environment variable $PYFILE



1. Run inline

	* Write a Shell script that runs Python code
	* The Python code will be saved in the environment variable $PYCODE



2. Hello, print

	* Write a Python script that prints exatly "Programming is like building a multilingual puzzle , followed by a new line
	* Use the function print



3. Print integer 

* Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line. (https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py)
		* The output of the script should be:
			* the number, followed by Battery street,
			* followed by a new line
		* You are no allowed to cast the variable number into a string
		* Your code must be 3 lines long
		* YOu have to use f-strings (tips: https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) 



4. Print float

	* Complete the source code in order to print the float stored in the variable number with a precision od 2 digigts (https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py) 
		* The output of the program should be:
			* FLoat: , followed by the float with only 2 digigts
			* Followed by a new line
		* You are no allowed to cast number to string
		* You have to use f-strings


5. Print string

	* Complete the source code in order to print 3 times a string stored in the variable str, followed by its first 9 charactersn (https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py) 
		* The output of the program should be:
			* 3 times the valuse of str
			* followed by a new line
			* followed by the 9 first character of str
			* followed by a new line
		* You are not allowed to use any loops or conditional statement
		* Your program should be a maximum 5 lines long


6. Play with strings

	* Complete the source code to print Welcome to Holberton School! (https://github.com/alx-tools/0x00.py/blob/master/6-concat.py)
		* You are not allowed to use any loops or conditional statements 
		* You have to use the variables str1 and str2 in your new line of code

		* Your program shoudl be exactly 5 lines long

7. Copy - Cut - Paste

	* Complete this source code (https://github.com/alx-tools/0x00.py/blob/master/7-edges.py) 
		* You are not allowed to use any loops or condtional statements
		* Your program should be exactly 8 lines long
		* word_first3 should contain the first 3 letters of the variable word
		* word_last_2 should contain the last 2 letters of the variable word
		* middle_word should contain the value of the variable word without the first and last letters


8. Create a new sentence 

	* Complete the source code to print object-oriented programming with Python , followed by a new line
		* You are not allowed to use any loops or condtional statements
		* Your prgram should be exactly 5 lines long
		* You are not allowed to create new variables 
		* You are not allowed to use string literals


9. Easter Egg

	* Write a Python script that prints "THe Zen of Python", by Tim Peters, followed by a new line.
		* Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py) 


10. Linked list cycle 

	* Technical interview preparation:
		* You are not allowed to google anything
		* Whiteboard first
		* This task and all fututre technical interview prep tasks will include checks for the efficiency of your solution, ie, is your solution's runtime fast enough, does your solution require extra memory usae ? mallocs, etc

	* Write a funtion in C that checks if a singly linked list has a cycle in it
		* Prototype: int check_cycle(listint * list);
		* Return: 0 if there is no cycle, 1 if there is a cycle

	* Requirements: 
		* Only these functions are allowed: write, printf, putchar, puts, malloc, free

11. Hello, write

	* Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19 , followed by a new line
		* Use the function write from the sys module
		* You are not allowed to use print
		* Your script shoudl print to stderr
		* Your sript should exit with the status code 1

12. Compile

	* Write a script that compiles a Python sript file
		* The python file name will be stores in the environment variable $PYFILe
		* The output file name has to be $PYFILEc  (ex: export PYFILE=my_main.py => output filename: my_main.pyc)

13. ByteCode -> Python #1

	* Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode: 

  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE

	* https://docs.python.org/3.4/library/dis.html (Python bytecode)	
