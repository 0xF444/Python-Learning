# NUMBERS ASSIGNMENT
# --------------------
# Assignment #1
# x = 4
# y = 4.0
# z = 4+3j
# print(type(x))
# print(type(y))
# print(type(z))
# ----------------------------------------------------------------------------------
# Assignment #2
# c = 1+2j
# print(c.real)
# print(c.imag)
# ----------------------------------------------------------------------------------
# Assignment #3
# num = 10
# print("%.10f" % float(num))  #C-like way
# print("{:.10f}".format(float(num))) #New way
# ----------------------------------------------------------------------------------
# Assignment #4
# num = 159.650
# newnum = int(num)
# print(newnum)
# print(type(newnum))
# ----------------------------------------------------------------------------------
# Assignment #5
# print(100 - 115)
# print(50 * 30)
# print(21 % 4)
# print(110//11)
# print(97 // 20)
# ----------------------------------------------------------------------------------
# LISTS ASSIGNMENT
# --------------------
# Assignment #1
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# print(friends[0]) #Method One
# print(friends[-5]) #Method Two
# print(friends[4]) #Method One
# print(friends[-1]) #Method Two
# ----------------------------------------------------------------------------------
# Assignment #2
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# print(friends[0:5:2])
# print(friends[1:5:2])
# ----------------------------------------------------------------------------------
# Assignment #3
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# print(friends[1:4])
# print(friends[-2::1]) # note: starts at -2 and TAKES THE END WITH IT, UNLIKE PUTTING -1 AS AN END.
# ----------------------------------------------------------------------------------
# Assignment #4
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# friends[-2] = "Elzero"
# friends[-1] = "Elzero"
# print(friends)
# ----------------------------------------------------------------------------------
# Assignment #5
# friends = ["Osama", "Ahmed", "Sayed"]
# friends.insert(0, "Nasser")
# friends.append("Salem")
# print(friends)
# ----------------------------------------------------------------------------------
# Assignment #6
# friends = ['Nasser', 'Osama', 'Ahmed', 'Sayed', 'Salem']
# friends.pop(0) # changes the iterable
# friends.pop(0) # since 'Osama' is the new zero index element
# print(friends)
# friends.pop(-1)
# print(friends)
# ----------------------------------------------------------------------------------
# Assignment #7
# friends = ["Ahmed", "Salah"]
# employees = ["Samah", "Eman"]
# school = ["Ramy", "Shady"]
# friends.extend(employees)
# friends.extend(school)
# print(friends)
# ----------------------------------------------------------------------------------
# Assignment #8
# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# friends.sort()
# print(friends)
# friends.sort(reverse=True)
# print(friends)
# ----------------------------------------------------------------------------------
# Assignment #9
# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# print(len(friends))
# ----------------------------------------------------------------------------------
# Assignment #10
# technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
# print(technologies[-1][0])
# print(technologies[-1][-1])
# ----------------------------------------------------------------------------------
# TUPLES ASSIGNMENT
# --------------------
# Assignment #1
# name = "Omar",
# print(name[0])
# print(type(name))
# ----------------------------------------------------------------------------------
# Assignment #2
# friends = ("Osama", "Ahmed", "Sayed")
# friends = list(friends)
# friends[0] = "Elzero"
# friends = tuple(friends)
# print(friends)
# print(type(friends))
# print(len(friends))
# ----------------------------------------------------------------------------------
# Assignment #3
# nums = (1, 2, 3)
# letters = ("A", "B", "C")
# n = nums + letters
# print(n)
# print(len(n))
# ----------------------------------------------------------------------------------
# Assignment #4
# my_tuple = (1, 2, 3, 4)
# a, b, _, c = my_tuple
# print(a)
# print(b)
# print(c)
# ----------------------------------------------------------------------------------
