#                                          STRINGS
# --------------------------------------------------------------------------------
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
# --------------------------------------------------------------------------------
# there are integers, floats and complex numbers
# real part = .real, imaginary = .imag
# we can convert between each type by using .datatype()
# can't convert complex to anything
# --------------------------------------------------------------------------------
# arithmetic operators are the same as before with the addition of "**" and "//"
