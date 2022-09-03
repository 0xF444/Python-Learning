# File handlling
# MODES
# "a" append: open the file for appending values, creates the file if it doesn't exist
# "r" read: (is the default value) open the file for reading and gives error if the file doesn't exist
# "w" write: open the file for writing, creates the file if it doesn't exist
# "x" create: creates the file, gives an error if the file already exists
# ---------------------------------------------------------------------------------------
# open() ==> opens a file's path and returns it in a stream, requires the file and the mode
# import os is a module that contains extra handy methods and functions
# os.cwd: gets the current working directory
# os.path.abspath(__file__) returns the absolute directory of the CURRENT FILE WE'RE IN or program
# os.path.dirname(file) returns the directory in which the file is contained
# os.chdir() changes your current working directory
# we can add "r" <rowed string> to the string so it can avoid any escape sequences or commands within the string
# the read attribute gives the data of the data object NOT its content
# .name: prints the name, .mode: prints the mode, .encoding prints the encoding
# .read() can take the number of bytes (character) needed, default value is -1 (which is the entire file)
