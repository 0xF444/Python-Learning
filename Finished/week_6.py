# Assignment #1
# -------------
num1 = input("Please enter your first number.\n").strip()
num2 = input("Please enter your second number.\n").strip()
op = input("Please enter your operation.\n").strip()
print(f"Your operation is ({num1} {op} {num2}).\n")
num1 = int(num1)
num2 = int(num2)
if op == "+":
    print(f"Result is {num1+num2}.\n")
elif op == "-":
    print(f"Result is {num1-num2}.\n")
elif op == "*":
    print(f"Result is {num1*num2}.\n")
elif op == "/":
    print(f"Result is {num1/num2}.\n")
elif op == "%":
    print(f"Result is {num1%num2}.\n")
else:
    print("Invalid operation.\n")
# -------------
# Assignment #2
# -------------
age = 17
print("App is suitable for you.\n") if age > 16 else print(
    "App is not suitable for you.\n")
# -------------
# Assignment #3
# -------------
age = input("Please enter your age in years.\n").strip()
age = int(age)

if age > 10 and age < 100:
    print("#"*80)
    print(" You can enter the first letter or full name of the time unit. ".center(80, "#"))
    print("#" * 80)
    print("If you choose to insert the small letter, please insert it capitalized. (except for minutes)\n")
    time = input("Please enter the time unit.\n").strip().capitalize()
    if time == "Months" or time == "M":
        print(f"Your age in months is {age*12}.\n")
    elif time == "Weeks" or time == "W":
        print(f"Your age in weeks is {age*12*4:,}.\n")
    elif time == "Days" or time == "D":
        print(f"Your age in days is {age*12*4*7:,}.\n")
    elif time == "Hours" or time == "H":
        print(f"Your age in hours is {age*12*4*7*24:,}.\n")
    elif time == "Minutes" or time == "m":
        print(f"Your age in minutes is {age*12*4*7*24*60:,}.\n")
    elif time == "Seconds" or time == "S":
        print(f"Your age in seconds is {age*12*4*7*60*60:,}.\n")
    else:
        print("Invalid time unit, please try again.\n")
else:
    print("Age out of range, please try again.\n")
# Assignment #4
# -------------
countries = ["Egypt", "Palestine", "Syria",
             "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
country = input("Please enter your country.\n").strip().capitalize()
if country in countries:
    print(
        f"Your country is eligible for a discount and the new price is ${price - discount}.\n")
else:
    print(
        f"Your country is not eligible for a discount and the price is ${price}.\n")
# -------------
