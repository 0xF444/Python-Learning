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
