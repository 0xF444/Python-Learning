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
#
n = "Omar"
a = 20
print(f"My name is: {n} and my age is {a}")
