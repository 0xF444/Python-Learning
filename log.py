# File handlling
# MODES
# "a" append: open the file for appending values, creates the file if it doesn't exist
# "r" read: (is the default value) open the file for reading and gives error if the file doesn't exist
# "w" write: open the file for writing, creates the file if it doesn't exist
# "x" create: creates the file, gives an error if the file already exists
# ---------------------------------------------------------------------------------------
# open() ==> opens a file's path and returns it in a stream, requires the file and the mode
# import os is a module that contains extra handy methods and functions
# os.getcwd(): gets the current working directory
# os.path.abspath(__file__) returns the absolute directory of the CURRENT FILE WE'RE IN or program
# os.path.dirname(file) returns the directory in which the file is contained
# os.chdir() changes your current working directory
# -------
# READ "r"
# we can add "r" <rowed string> to the string so it can avoid any escape sequences or commands within the string
# the read attribute gives the data of the file data object NOT its content
# .name: prints the name, .mode: prints the mode, .encoding prints the encoding
# .read() returns the content of the file, can take the number of bytes (characters) needed, default value is -1 (which is the entire file)
# .readline() reads a line, can take specific line characters
# .readlines() returns all the lines in a list ending with a "\n", you can limit what comes back by an attribute
# .startswith() bool function that checks if the line starts with the argument
# .close() closes the file
# -------
# WRITE "w" and APPEND "a"
# .write() is used to write content to the file, overwriting it
# .writelines(<group iterable>) can take a tuple or a list etc, it writes them to the file
# append basically writes but doesn't overwrite
# it also takes into consideration the writing cursor
# .truncate() takes a number of bytes and then returns those bytes and overwrites
# .tell() tells you where the cursor is
#! IMPORTANT NOTE: THE LINE BREAK CODE IN LINUX IS JUST ONE CHARACTER BUT IN WINDOWS IT'S TWO.
# .seek() sends the cursor to a given offset
# we need the os module for file manipulation
# os.remove(<filepath>) removes the file
# we can make the file handled in either text mode or binary mode (image)
# os.path.relpath prints the relative path
# __file__ is a variable for the path of the current file we're opening.
# os.listdir() allows you to list the directory content
# If you need to read the data again, you need to replenish the source with the same data again, meaning that you need to read the file again.
# TODO: REVISE ON FILES HANDLING AGAIN.
# ------------------------------------
# Built in functions:
# all() --> takes an iterable, returns true for all "true" values in the iterable
# any() --> takes an iterable, returns true for at least ONE "true" value in the iterable
# bin() --> returns the binary of an int
# id() --> returns the "address" of an object, each object has a unique id
# sum() --> takes an iterable and the start, prints the sum of the iterable's elements
# round() --> takes a number, and a number of digits after the decimal point, rounds the number accordingly
# range() --> takes a start, end and a step
# print() --> its default seperator is " ", we can change it by making <sep=>, we can seperate each message with a comma in a function normally
# * print can also take a second value called <end=> so we can control what the string ends up with
# abs() --> returns the absolute the value of an integer
# pow() --> takes a base, exp and mod returns base**exp or (base**exp) % mod if provided
# min() --> returns the least element, if given by hand or if they are in an iterator
# * max() --> same as min but gets you the maximum
# * slice() --> same as data slicing, requires a start and stop, can take a step [start:stop:end]
# map() --> takes a function and an iterator, basically applies the function to each element in the iterable, can be looped over and be added to a variable
# * can also take lambda function in the function argument
#! Here, we use can use lambda functions and map() to iterate over an iterable without needing to have the function in our system
# filter() --> has the same concept for map() BUT it returns the elements in the iterable that make the function true NOT THE VALUE ITSELF
#! basically, filter() is the same as map but only returns the elements that make the function TRUE
# to use reduce() we must use a module functool
# reduce() basically takes the result of the first two arguments and makes it an argument in the next iteration
# enumerate() basically accompanies each element in an iterator with a number <counter> instead of defining a seperate counter
# help() basically prints HOW to use a function
# reversed() reverses your iterable
# ------------------------------------
# a module is a file that contains multiple functions
# you can import multiple modules, create them etc
# they save your time
# random module prints random information, there is a function .random
# * to call a function from an imported module: module.function()
# to show all the functions in a module we use dir()
# to import a function from a module, use the "from" keyword
# we can use the * wildcard to import every function within the function
#! ofc when the function is imported, we can't use module.function() to call it, we then use the function itself
# to create a module, we create a file .py that contains all our functions
# sys module contains a function called path that prints out all the system paths that python looks for any modules including the path to the directory where the file is executed
# we can append a path to the pathes: sys.path.append()
# we can make an alias for the module import <module name> as <alias name>
# module is a file that contains functions, packages are MULTIPLE MODULES
# package manager for python: pip
# ------------------------------------------
# -- Modules => Install External Packages --
# ------------------------------------------
# [1] Module vs Package
# [2] External Packages Downloaded From The Internet
# [3] You Can Install Packages With Python Package Manager PIP
# [4] PIP Install the Package and Its Dependencies
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
# [6] Packages and Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# ---------------------------------------------------------------------
# to install a package: pip install <name>
# ---------------------------------------------------------------------
# DATE AND TIME: import datetime
# to print the current time: datetime.datetime.now()
# to print the current year or anything: datetime.datetime.now().year<anything>
# to print start and end of date: datetime.datetime.max datetime.datetime.min
# i think that to use the datetime module it needs to be orderized, meaning that it just follows a certain pattern for what you want
# strftime prints the time according to your format using a directive, a directive basically is a placeholder for information, much like c
# strftime.org
# an iterable is basically an object that contains data that can be "looped over"
# we can generate an "iterator" that well, iterates using the iter()
# next() --> returns the next element in the iterator
# when finished it returns a "StopIteration"
# a decorator decorates how a function is executed
# usually by defining a function with a "function argument" as its parameter then defining a nested function where all the decoration happens then executing the parameter
# if we wanted a function after decoration, we use sugar syntaxing: adding an "@" then the decorator name ABOVE the function definition
# there is a module called time from which we can import time() that saves the time of now, can be used for speed testing
# a generator when called only gives you the control and returns an iterator
# In computer science, a generator is a routine that can be used to control the iteration behaviour of a loop. All generators are also iterators. A generator is very similar to a function that returns an array, in that a generator has parameters, can be called, and generates a sequence of values
# once a value is normally generated through generator call, it doesn't start over when called again, it resumes where it last left off
# using next() we can walk through each value
# Decorator => Meta Programming, used to enchance functions' behaviour
# Decorators are used to change the "capability" of the function say: logging, test performance, caching etc
# https://strftime.org => Date Formatter
# https://www.freecodecamp.org/news/python-decorators-explained-with-examples/ => Decorators
# https://www.programiz.com/python-programming/generator => Generators
# zip() -> basically "zips" iterables with the length of the least lengthed object
# the Pillow module contains image manipulation
# Image.open(<path>) opens the image
# var.show() shows the image
# boxes can be defined as (left,upper,right,lower), the origin point is (0,0) in the upper left corner
# to convert to greyscale use .convert("L")
# A docstring is used to inform of what the function/class does, using ''' '''
# a Docstring is NOT a comment
# we can access the docstring by using the variable __doc__ or help()
# commenting is basically adding notes, while documenting is a description of a certain function/class
# pylint helps you write clearer code suitable for corporations
# pylint.exe <path of your program> to "lint" your code
# Exceptions are a runtime error reporting mechanism THAT STOPS YOUR PROGRAM IF EXECUTED
# We can create our own exception by using raise Exception() or raise ValueError, etc
# https://docs.python.org/3/library/exceptions.html => Python Exceptions
#* pip packages downloaded (to be downloaded on my linux machine): termcolor,pyfiglet,PIL(pillow),pylint
# "try" tests your code
# "except" executes its code snippet if the code snippet in "try" raises an error (ANY ERROR)
# "else" is used if there's no errors (duh lol) *might not be needed*
# "finally" executes its code snippet NO MATTER WHAT (it does not care lol)
#* we can give "except" the exception type => except <exception type>
#! the debugger is very important 
# breakpoint is a point where the debugger stops
# type hinting gives you a "hint": "-> type"