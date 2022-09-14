# Assignment #1 -> Sheet 1
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []
final_string =""
for data in zip(my_list, my_tuple):
    final_string+= data[0]+data[1] # Since data contains each letter in a tuple, we can manipulate it easily
print(final_string)
print("="*150)
# Another Method
for data in zip(my_list, my_tuple):
    for letter in data:
        my_data.append(letter)
final_string2=''.join(str(l) for l in my_data)
print(final_string2)
print("="*150)
# -----------------------
# Assignment #2 -> Sheet 1
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []
for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    if item1 == 1:
        break
    else:
        my_data.append(item1)
final_string3 = ''.join(my_data)
print(final_string3)
print("="*150)
# Assignment #3 -> Sheet 1
from PIL import Image
img = Image.open(r"C:\Users\magic group\Desktop\Python-Learning\Ongoing\Week_12_Assignment\elzero-pillow.png")
newimg1 = img.crop((400,0,800,400)) # don't forget about how points and vectors move, that's how you'll understand ;)
newimg1 = newimg1.convert("L")
newimg1.save(r"C:\Users\magic group\Desktop\Python-Learning\Ongoing\Week_12_Assignment\img1.png")
newimg1.close()
newimg2 = img.crop((0,400,1200,800))
newimg2 = newimg2.convert("L")
newimg2 = newimg2.rotate(180)
newimg2.save(r"C:\Users\magic group\Desktop\Python-Learning\Ongoing\Week_12_Assignment\img2.png")
newimg2.close()
# -----------------------
# Assignment #4 -> Sheet 1
def say_hello_to(name) -> str:
    '''
    parameter: is a string that contains the name of the user
    the function greets the person happily!
    '''
    print(f"Hello {name}!")
print(say_hello_to.__doc__)
print(help(say_hello_to))
# -----------------------
# Assignment #5 -> Sheet 1
'''This module contains a function that greets people
'''
my_Friends = ["Ahmed", "Osama", "Sayed"]
def say_hello(some_peoples) -> list:
    '''Parameter: Some_Peoples is a list that contains the names that shall be greeted.
    Function: Greets the people in your list!
    '''
    for some_one in some_peoples:
        print(f"Hello {some_one}.")
say_hello(my_Friends)
# It has been linted and scored 10/10 in a seperate file.
# -----------------------

