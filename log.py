# Regular expressions are expressions that define a search pattern: remember the grep command in ubuntu?
# https://pythex.org to test our expressions
# https://www.debuggex.com/cheatsheet/regex/python for char sets
# mostly used in validations
# Regex explaination: https://regex101.com
# search() --> searchs a string for a match and returns the first match only
# findall() --> returns a list of all matches and returns an empty list if there are no matches
# to use regex: import re
# re.span() returns the position of the match
# re.string() returns the string that you're searching within
# re.group() returns the group that has the matches

import re
my_string = re.findall("[A-Z]", "OsamaElzero")
print(my_string)
