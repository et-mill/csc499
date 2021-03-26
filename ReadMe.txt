Elliot Miller - CSC 499 - Homework 3: Sort Names - Reversed - With Test
################################################

A simple script to sort a list of names, first by their length, and then alphabetically.
The script outputs the results to a user determined text file.

To run the program, open a terminal in the file location of the sort_names.py script,
call the script with arguments 'input file path', 'output file path'.

There is now functionality to choose new ways to sort your list.
by default your list will be sorted length of name(asc), then alphabetically(asc), no argument is needed/

enter one of the optional arguments after the file paths to:
 z : sort list by length of name(asc), then alphabetically(desc)
 - : sort list by length of name(desc), then alphabetically(asc)
-z : sort list by length of name(desc), then alphabetically(desc)

Example terminal command:
>python sort_names.py 'Sort Me.txt' 'Sorted Names.txt'
or
>python sort_names.py 'Sort Me.txt' 'Sorted Names.txt' -z

To test the correctness of output files:
run the sort_test.py command in the terminal
example:
>python sort_test.py

the output for the example test should be ..F, two passes and a fail.

Let me know if you have any questions, thanks for your time!
Tested on Manjaro Linux, not sure if there's any particularities with OSX file paths.
