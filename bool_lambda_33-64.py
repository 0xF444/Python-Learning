#                                         BOOLEAN
# True or False
# bool() returns true or false true if anything and false if empty container or false itself.
# --------------
# bool operators
# "and" ANDs the two conditions
# "or" ORs the two conditions
# "not" reverses
# they're the same as logic statements which we know
# --------------
# Assignment operators
# they "assign" a value to a variable
# "=" normally assigns a value to a variable
# "+=" adds the old value of a variable to some different variable and assigns it to the variable
# "-=" same but subtracts
# "*=" same but multiplies
# "/=" same but divides
# "**=" same but powers (exponential)
# "%=" same but takes the modulo
# "//=" same but floor divides
# --------------
# Comparison operators
# "==" equals
# "!=" not equal
# ">" larger than
# "<" less than
# ">=" larger or equal
# "<=" smaller or equal
# ""
# --------------
# Type Conversion
# str() --> to string
# tuple() --> to tuple
# list() --> to list
# set() --> to set
# dict() --> to dict (cannot convert a string to a dict)
# as for tuples, use nested tuples (key,value)
# as for lists, use nested lists [key,value]
# as for sets, unhashable (cannot convert) as you cannot get values from a set
# --------------
# input() --> stops executing until an input is entered from stdin
# chain method --> you can chain methods by dots normally
# --------------
# short if: Condition if True | if condition | Condition if False
# membership operators: in/not in "bool operators"
# --------------
#                                                       LOOPS
# (while) loop is the same as before, but there is the additon of "else" which executes as soon as the condition goes false
# it is way different than executing after the loop's finished
# for item in iterable_object: do something, used for iterables mostly
# for can take multiple "items"
# break, continue and pass:
# continue stops the current iteration and starts at the loop again
# break exits from the loop entirely
# pass is mainly used for testing as it "passes" the loop or the if statement
# range() ==> normally starts from 0 and stops before a given number, we can give it our own range of numbers (start to finish) and also the step.
# we can use .items in dictionary to loop it using two items representing its key and value
# we can use enumerate() to get the index and also the value of a certain object (list, tuple, etc)
# "Pythonic term" ==> code that doesn't just get the syntax right but also follows the conventions of the python community which makes it easier to read and understand.
# you can unpack the arguments by using a "*", can be used for iterables when you don't know how many indices are there.
# (*parameter) can be referred to as EVERY argument given to the function, only 1 *parameter allowed
# We can assign a default value to the function parameter which is useful if no argument is given
# if we assign a default value to the FIRST parameter then all adjacent parameters MUST have a default parameter
# so if we wanted ONE default value it should be the last parameter
# (*parameter) is basically a TUPLE of the given parameters while (**parameter) is a DICTIONARY.
# (**parameter) needs a KEY and a VALUE for each argument
# (**argument) unpacks the given dict for the function to operate on
# (*parameter) unpacks a tuple, **parameter unpacks a dict.
# "global" makes a variable global through out the program, overwriting any previous global values
# recursive functions are functions that operate by calling itself over and over again.
# lambda functions are functions that are "anonymous", they are not linked to an identifier (name)
# it can be written inline without definition
# used for simple functions and is a single expression
# identifier = lambda <parameters> : <return value>
# .__name__ is used to return the type of the function
#########################################################################################
