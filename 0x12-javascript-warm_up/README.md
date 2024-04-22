0x12-javascript-warm_up

0. First constant, first print

	Write a script that prints "JavaScript is amazing":
		* You must create a constant variable called myVar with the value "JavaScript is amazing"
		* Use console.log(...) to print all output
		* Not allowed to use var

1. 3 languages

	Write a script that prints 3 lines:
		* The first line: "C is fun"
		* The second line: "Python is cool"
		* The third line: "JavaSript is amazing"
		* Use console.log to print the output
		* Not allowed to use var

2. Arguments

	Write a script that print a message depending of the number of arguments passed.
		* If no arguments are passed to the script, print "No argument"
		* If only one argument is passed to the script, print "Argument found"
		* Otherwise, print "Arguments found"
		* Use console.log(...) to print all output
		* Not allowed to use var

3. Value of my argument

	Write a script that prints the first argumment passed to it:
		* If no arguments are passed to the script, print "No argument"
		* Use console.log(...) to print all output
		* Not allowed to use var
		* Not allowed to use length

4. Create a sentence

	Write a script that prints two arguments passed to it, in the following format: "is" 
		* Use console.log(...) to print all output
		* Not allowed to use var

5. An integer

	Write a script that prints My number: <first argument converted in integer> of the first argument can be converted to an integer
		* If the argument can't be converte to an integer, print "Not a number"
		* Use console.log(...) to print all output
		* Not allowed to use var
		* Not allowed to use try/catch

6. Loop to languages

	Write a script that prints 3 lines: (like 1-multi_languages.js)but by using an array of a string and a loop
		* The first line: "C is fun"
		* The second line: "Python is cool"
		* The third line: "JavaScript is amazng"
		* Use console.log(...) to print all output
		* Not allowed to use any if/else statement
		* Only use console.log
		* Use a loop (while, for, etc)

7. I love C

	Write a script that prints x times "C is fun"
		* Where x is the first argument of the script
		* If the first argument can't be converted to an integer, print "Missing number of occurances"
		* Use console.log(...)
		* Not allowed to use var
		* Only use var
		* Only use two console.log
		* Use a loop (while, for, etc)

8. Square

	Write a script that prints a square
		* The first argument is the size of a square
		* If the first argument can't be converted to an integer, print "Missinf sixe"
		* Use the character X to print the square
		* Use console.log(...) to print all output
		* Not allowed to use var
		* Use a loop (while, for, etc)

9. Add

	Write a script that prints the addition of 2 integers
		* The first arguement is the first integer
		* The second argument is the second integer
		* Define a function with this prototype: funtion add(a, b)
		* Use console.log(...)
		* Not allowed to use var

10. Factorial

	Write a script that computes and prints a factorial
		* The first argument is integer (argument can be cast as integer) used for computing the factorial
		* Factorial of NaN is 1
		* Must be done recursively
		* Must use a function
		* Use console.log(...) to print all output
		* Not allowed to use var

11. Second biggest!

	Write a script that searces the second biggest integer in the list of arguments
		* Assume all arguments can be converted to integer
		* If no argument passed, print 0
		* If the number of arguments is 1, print 0
		* Use console.log(...) to print all output
		* Not allowed to use var

12. Object

	Update this script to replace the value 12 with 89:
		* Not allowed to use var

#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

13. Add file

	Write a function that returns the addition of 2 integers
		* The function must be visible
		* The name of the function must be add
		* Not allowed to use var
