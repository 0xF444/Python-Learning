# Assignment #1
values = (0, 1, 2)

if any(values):

    my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

    print("Good")

else:

    print("Bad")
print("#"*80)
# My_var will exist = 0
# First condition is true because it stops at indx 4 and each value is true
# Second condition is FALSE because it stops at the end
# Third condition is FALSE becaise it also stops at the end
## Output: Good
# ----------------------------------
# Assignment #2
v = 40
my_range = list(range(v))
print(sum(my_range, v) + pow(v, v, v))
print("#"*80)
#NOTE: when calculated it seems that 39.05 is the actual value that satisfies the equation
# if it was 39 it would be exactly 819
# ----------------------------------
# Assignment #3
n = 21

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

    print("Good")
print("#"*80)
# Easy enough, we used formulas to get the value of n
# ----------------------------------
# Assignment #1 -> Second Sheet
def remove_chars(s):
    return s[1:-1]
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
cleaned_listf = map(remove_chars,friends_map)
cleaned_listl = map(lambda s:s[1:-1],friends_map)
for name in cleaned_listl:
    print(name)
print("#"*80)
# Function and Lambda OUTSIDE THE LOOP
# --
for name in friends_map:
    cleaner = lambda s: s[1:-1]
    print(cleaner(name))
print("#"*80)
# Lambda INSIDE THE LOOP
# ----------------------------------
# Assignment #2 -> Second Sheet
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
def get_namesf(name):
    return name.endswith("m")
names = filter(lambda name: name.endswith("m"),friends_filter)
for name in names: 
    print(name)
print("#"*80)
# Function and Lambda OUTSIDE THE LOOP
# --
for name in friends_filter: 
    get_namesl = lambda name:name.endswith("m")
    if get_namesl(name):
        print(name)
print("#"*80)
# Lambda INSIDE THE LOOP
# ----------------------------------
# Assignment #3 -> Second Sheet
from functools import reduce
def multiply(x,y):
    return x*y
nums = [2, 4, 6, 2]
print(reduce(multiply,nums))
print(reduce(lambda x,y: x*y,nums))
print("#"*80)
# ----------------------------------
# Assignment #4 -> Second Sheet
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
new_skills=reversed(skills)
for counter, skill in enumerate(new_skills,50):
    if type(skill) == int:
        continue
    else:
        print(f"{counter} - {skill}")

