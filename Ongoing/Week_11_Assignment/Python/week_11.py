# Assignment #1 -> First Sheet
# ----------------------------
import datetime
from random import randint
print(f"Random Number between 10 and 50 => {randint(10,50)}")
# Used half the range => then multiplied by two
print(f"Random Even Number between 2 and 10 => {randint(1,5)*2}")
# Same as above, but added one to make it odd.
print(f"Random Odd Number between 1 and 9 => {(randint(1,3)*2)+1}")
print(dir(randint))
print("="*150)
# ----------------------------
# Rest of Sheet 1 are in their files.
# ----------------------------
# Assignment #1 -> Second Sheet
# ----------------------------
old = datetime.datetime(2021, 6, 25)
new = datetime.datetime.now()
printold = old.strftime("%Y-%M-%d")
printnew = new.strftime("%Y-%M-%d")
print(f"Days from {printold} to {printnew} is => {(new-old).days} days.")
print("="*150)
# ----------------------------
# Assignment #2 -> Second Sheet
# ----------------------------
print(new.strftime("%Y-%M-%d"))
print(new.strftime("%b %d, %Y"))
print(new.strftime("%d - %b - %Y"))
print(new.strftime("%d / %b / %Y"))
print(new.strftime("%d / %B / %Y"))
print(new.strftime("%a, %d %B %Y"))
print("="*150)
# ----------------------------
# Assignment #1 -> Third Sheet
# ----------------------------


def reverse_string(my_str):
    my_str = reversed(my_str)
    for letter in my_str:
        yield letter


for c in reverse_string("Elzero"):
    print(c, end="")
print()
print("="*150)
# ----------------------------
# Assignment #2 -> Third Sheet
# ----------------------------


def sugardecor(func):
    def add():
        print("Sugar added from decorators.")
        func()
        print("####################")
    return add


@sugardecor
def make_tea():
    print("Tea created.")


@sugardecor
def make_coffee():
    print("Coffee created.")


make_tea()
make_coffee()
# ----------------------------
