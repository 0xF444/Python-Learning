#                                          STRINGS
# len() --> length of a string
# strip() --> removes ALL spaces or a specific character if specified as an argument
# lstrip() --> same as strip() but from the left side only
# rstrip() --> same as rstrip() but from the right side only
# title() --> captializes any start of a string and any character next to a number
# capitalize() --> captializes any start of a string
# zfill() --> fills a given numeric string to the given argument
# upper() --> captializes a given string
# lower() --> makes the given string small
# --------------------------------------------------------------------------------
# split() --> returns a "list" of each string by the given argument: serprator and a max split
# rsplit() --> starts delisting from the end (right) and is the same as split()
# center() --> starts to center the original given string by a total number around a given character
# count() --> counts how many of a given string argument, can take a start and an end
# swapcase() --> swaps the cases of each character
# startswith() --> checks if the string starts with the argument, returns bool, can take a start and an end
# endswith() --> same as startswith() but with the end
# --------------------------------------------------------------------------------
# index() --> finds the index of a substring, can take a start and an end
# find() --> same as index but gives -1 when the substring is not found
# rjust() --> fills the character to the right to given the width, can take a specific character
# ljust() --> same as rjust() but does it to the left
# splitlines() --> returns lines in a list
# expandtabs() --> expands tabs "\t" and controls them with the given argument
# istitle() --> checks if its a title, returns bool
# isspace() --> checks if its a space, returns bool
# islower() --> checks if its lower, returns bool
# isupper() --> checks if its upper, returns bool
# isidentifier() --> checks if its a valid variable name, returns bool
# isalpha() --> if it's an alphabetical character
# isalnum --> if it's an alphabetical OR a numerical character
# replace() --> takes an old value and replaces it with a new value, can be counted
# join() --> joins a list or a tuple into a string by a given string
# --------------------------------------------------------------------------------
# %s = string placeholder, %d = decimal placeholder, %f float placeholder: LIKE C
# Controlling floating point number: %.xf
# Truncate String %.xs
# OLD WAY
# --------------------------------------------------------------------------------
# {} is the place holder and we use .format(), :d or :s or :f/if "{}" is left empty then s
# IT IS LITERALLY THE SAME AS THE OLD WAY ONLY MINOR DIFFERENCES IN SYNTAX
# {:_} seperates each 3 numbers with a _
# {n} where n is the index of entries in .format() can organize what order
# format in newer versions: we add f to the beginning {variable name}
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                       NUMBERS
# there are integers, floats and complex numbers
# real part = .real, imaginary = .imag
# we can convert between each type by using .datatype()
# can't convert complex to anything
# --------------------------------------------------------------------------------
# arithmetic operators are the same as before with the addition of "**" and "//"
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                           LISTS
# enclosed by []
# append() --> appends an element to a given list lastly: TREATS AN ELEMENT LIST AS ONE ELEMENT
# extend() --> extends elements to a given list: each element at its own
# remove() --> removes the first occurence of an element
# sort() --> sorts list's element numerically or alphabetically, can take a "reversed" argument
# reverse() --> reverses the elements only
# clear() --> empties a list
# copy() --> returns a shallow copy, does not care about the main list
# count() --> counts the occurence of an element
# index() --> returns the index of the argument if found in the list
# insert() --> inserts an object at the given (index - 1)
# pop() --> removes and returns item at index, iterates the list indefinitely
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                          TUPLES
# enclosed by ()
# same as lists, but cannot be changed
# to assign one element tuple we add a ","
# can concatenate any tuple into one tuple
# can repeat strings, lists or tuples by "*"
# count() --> counts the occurnece of an element
# index() --> the index of first occurence of an element
# destructing --> we can copy a tuple element by element to variables and we can ignore certain elements by "_"
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                           SETS
# enclosed by {}
# they're not in order, nor indexed (inaccessable through index)
# cannot be indexed nor sliced
# can only take "Immutable" elements:(Numbers, Strings, Tuples)
# Each item is unique (if the same elements exists within two places, only one stays)
# clear() --> clears the entire set
# union() --> unifies two or more sets in one set, can also be done by "|"
# add() --> adds a new element to the set
# copy() --> takes a shallow copy (does not the affect the original set)
# remove() --> removes an existing element (errors if element does not exist)
# discard() --> can remove an existing or nonexisting element
# pop() --> returns a random element from the set
# update() --> unifies the set itself with its previous entries plus another set, much like union()
# difference() --> returns the elements that are not in the argument (a-b)
# difference_update() --> is the same as difference() BUT ITERATES THE ORIGINAL SET AND UPDATES IT WITH THE DIFFERENCE ONLY
# intersection() --> returns whats common between two sets
# intersection_update() --> same as intersection() but updates the original set with the intersection ONLY
# symmetric_difference() --> returns the elements that do not exist in BOTH sets
# symmetric_difference_update*() --> same as symmetric_difference() but updates with the result of that function
# issuperset() --> returns bool, checks if all the elements of a set exists within another set (part of)
# issubset() --> opposite of issuperset(), checks if the given set is part of an other set
# isdisjoint() --> checks if two sets have nothing in common
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                  DICTIONARY
# enclosed by {} but each element has its own line/ key:value
# key must be immutable
# value can have any datatype
# dict keys MUST be unique
# you access elements using the key, not the index or by using .get(key)
# keys() --> prints all keys
# values() --> prints all values
# 2D dict: a value can also contain a dict
# clear() --> clears all keys
# update() --> updates a dict with a key and a value, note: you can assign new key:value to dict using =
# copy() --> takes a shallow copy of a dict
# setdefault() --> tries the find the value of the key and prints, if the key is not found, it sets it to the given default key argument
# popitem() --> returns the last added item
# items() --> returns the items of a dict in a list and each element of that list is a tuple of (key,value), it also follows the original dict
# fromkeys() --> must be surpassed by "dict" then takes "a" as key iterable and "b" as value
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
