# Assignment #1
import os
i = 1
while i<=50:
    if i == 25:
            myFile=open(fr"C:\Users\magic group\Desktop\Python-Learning\Ongoing\Week_9_Assignment\Python\special-text.txt","w")
    myFile=open(fr"C:\Users\magic group\Desktop\Python-Learning\Ongoing\Week_9_Assignment\Python\txt{i}.txt","w")
    myFile.write(f"Elzero Web School => {i}")
    i+=1
print(os.getcwd())
print(os.path.abspath(__file__))
print(__file__)
counter = 0
for file in os.listdir(os.getcwd()):
    if os.path.isfile(os.getcwd()):
        counter += 1
print(counter)