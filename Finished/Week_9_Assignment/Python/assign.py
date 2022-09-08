# Assignment #1 --> Assign.py
import os
# -----------------------
# i = 1
# while i <= 50:
#     if i == 25:
#         myFile = open(
#             fr"C:\Users\magic group\Desktop\Python-Learning\Ongoing\Week_9_Assignment\Python\special-text.txt", "w")
#     myFile = open(
#         fr"C:\Users\magic group\Desktop\Python-Learning\Ongoing\Week_9_Assignment\Python\txt{i}.txt", "w")
#     myFile.write(f"Elzero Web School => {i}")
#     i += 1
# print(os.getcwd())
# print(os.path.abspath(__file__))
# print(__file__)
# print(os.path.relpath(__file__))
# print(len(os.listdir(os.getcwd())))
# ----------------------- Windows 10

print(os.getcwd())  # Default cwd
path = os.path.dirname(__file__)  # Directory for assign.py
os.chdir(path)  # It is now the current directory
print(os.getcwd())
print(path)
# Relative path to the file with respect to the cwd is the file itself.
print(os.path.relpath(__file__))
counter = 1
while counter <= 50:
    if counter == 25:
        myFile = open(fr"{os.getcwd()}/special-text.txt", "w")
    myFile = open(fr"{os.getcwd()}/txt{counter}.txt", "w")
    myFile.write(f"Elzero Web School => {counter}")
    counter += 1
print(len(os.listdir(os.getcwd())))  # File count
# ----------------------- Linux, Ubuntu
# Assignment #2
myFile.seek(24)
myFile = open(rf"{os.getcwd()}/txt1.txt", "a")
myFile.write("\n")
myFile.write("Appended => Elzero Web School\n"*50)
# Assignment #3
myFile = open(rf"{os.getcwd()}/txt1.txt")
read_data = myFile.read()
myFile = open(rf"{os.getcwd()}/txt1.txt")
list = myFile.readlines()
print(f"Number of Lines is => {len(list)}")
word = 0
ls = 0
for item in list:
    for letter in item:
        if letter:
            word += 1
        if letter == "l":
            ls += 1
wordc = read_data.split()
print(f"Number of Words => {len(wordc)}")
print(f"Number of Characters is => {word}")
print(f"Number of \'l\' character is => {ls}")
# Assignment #4
c = 50
while c > 40:
    os.remove(fr"{os.getcwd()}/txt{c}.txt")
    c -= 1
# THIS ASSIGNMENT WAS DONE IN LINUX SO PATHES LOOK DIFFERENT FROM USUAL
