# Regular expressions are expressions that define a search pattern: remember the grep command in ubuntu?
# https://pythex.org to test our expressions
# https://www.debuggex.com/cheatsheet/regex/python for char sets
# mostly used in validations
# TODO Regex explaination: https://regex101.com
# search() --> searchs a string for a match and returns the first match only
# findall() --> returns a list of all matches and returns an empty list if there are no matches
# to use regex: import re
# re.span() returns the position of the match
# re.string() returns the string that you're searching within
# re.group() returns the group that has the matches
# re.split() returns a list that contains the string with each match splitted, can also take a maxsplit
# re.sub() replaces each match with anything that we want, can also take a max replace
#! each of these commands take (pattern,string,max,flags)
# groups in regular expressions are pretty important
# re.group(<group number>) returns the group that got matched
# re.groups() returns all the groups that got matched
# * re flags: IGNORECASE (case insensitive), VERBOSE (allows commenting within the regular expression), DOTALL (since "." matches everything but the newline, this allows to match the newline as well), MULTILINE (default is it searchs from the start of the line the end of the line, this allows to search all lines)
# ----------------
# an object consists of attributes: things that "define" the object; and also consists of methods: what the object DOES
# a class can be defined as a blueprint/object constructor
# class instantiate means to create an instance of your object
# class keyword is used to define classes, class names are usually written in PascalCase (UpperCamelCase)
# each time you create an object from class, python uses a method called __init__ (stands for initialize)
# any method that starts and ends with an underscore is called a dunder/magic method
# * we define our first method in our class called __init__ with a MUST parameter called self (current instance of the object)
# self can be anything
# to create an object we use new()
# syntax
# class Name:
#     Constructor => Does the instantation (Creates instance from a class)
#     Each instance is a seperate object
#     def __init__(self, other data) -> None:
#         body of function
# to know which variable is under which class we use __class__
# the self parameter points at the newly created object? => the self parameter points at the current instance in which the object has taken from
# we can add attributes to the constructor so that each time we make an object out of the class it comes predefined with it
# also, we can use this information so that every object of the class has a specific data for each instance
# each attribute with the self. is now some sort of data
# with each object created we can find these attributes by using "dir"
# so instance attributes are defined within the constructor (the __init__ function) which makes sense because of the init name as parameters
# as for methods, it must have self as a parameter so that it points at the current instance of the class
# again: to create attributes we define them within the __init__ function as parameters and we use "self" to refer to the object that will be taken from the class
# methods are defined as the __init__ function with the exception of having self as a parameter
# other methods can access the class itself, its parameters, or other methods
#!!!!!!!! a class attribute is shared throughout EVERY OBJECT CREATED, unlike instance attribute which is unique to each instance
# class attributes are defined outside the __init__ but within the class
# * __init__ function is usually referred to as the constructor
# class attributes are accessed by classname.()
# class methods are within the class, marked by a decorator @classmethod
# it MUST take the "cls" parameter unlike the "self" parameter to indicate its a class method NOT an instance method
#! note that any method created within the class must take ATLEAST ONE PARAMETER DEFINING ITS TYPE
# to point to anything within the class within the class method we use cls now.
# * in reality, when instance methods are called, python does this in the background classname.method(<the name of the object>) where the name of the object is a parameter called self
# static methods do not take parameters necessarily, to create a static method the method must be succeded by the decorator @staticmethod
# we use static methods to relate to the class? static methods CANNOT ACCESS either the instance stuff or the class stuff
# so instance methods can modify class/instance attributes but static methods cannot modify any of those
# as for class methods: they can access class attributes or methods only BUT NOT THE INSTANCES
#! MAYBE THE TERMS "INSTANCE" "CLASS" "STATIC" ARE SOMEWHAT RELATED TO THE "PUBLIC" AND "PRIVATE" FROM OTHER LANGUAGES!
#! THE "PRIVACY" OF EACH METHOD OR ATTRIBTUE
# magic methods:
# __init__ is always called automatically when an object is created
# __class__ returns which class the instance belongs to
#! variables are actually instances of classes because datatypes are actually classes
# __str__ returns human readable output
# normally when we print an instance of a class we get unreadable stuff, __str__ runs if we print the class itself
# __len__ is called when len() is used on the instance, an exception is raised if there's no __len__ and len() is used on the instance
# * don't forget that you can access instance attributes by using the name of the instance and the dot operator
# inheritance:
