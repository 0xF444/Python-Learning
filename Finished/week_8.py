# Assignment #1 --> First Sheet
def calculate(n1, n2, op="Add"):
    n1 = int(n1)
    n2 = int(n2)
    op = str(op)
    op = op.capitalize()
    print("Result is:")
    if op == "Add" or op == "A" or op == "a" or op == "+":
        return n1+n2
    elif op == "Subtract" or op == "S" or op == "s" or op == "-":
        return n1-n2
    elif op == "Multiply" or op == "M" or op == "m" or op == "*":
        return n1*n2
    else:
        return "Invalid operation."


print("You may only do three operations: Addition, Subtraction and Multiplication.")
f1, f2, op = input("Please enter your first number. "), input(
    "Please enter your second number. "), input("Please enter your operation. ")
print(calculate(f1, f2, op))
# -----------------------
# Assignment #2 --> First Sheet


def addition(*numbers):
    sum = 0
    for number in numbers:
        if number == 10:
            continue
        if number == 5:
            sum -= 5
            continue
        sum += number
    return sum


print(addition(10, 20, 30, 10, 15))
print("="*100)
print(addition(10, 20, 30, 10, 15, 5, 100))
# -----------------------
# Assignment #3 --> First Sheet


def show_skills(name, *skills):
    if len(skills) == 0:
        print(f"Hello {name}, you have no skills to show.")
        return
    else:
        print(f"Hello {name}, Your skills are: ")
        for skill in skills:
            print(f"- {skill}")
        return


show_skills("Osama", "HTML", "CSS", "JS", "Python")
print("="*100)
show_skills("Ahmed")
# -----------------------
# Assignment #4 --> First Sheet


def say_hello(name="Unknown", age="Unknown", country="Unknown"):
    return f"Hello {name}, Your age is {age} and you live in {country}."


print(say_hello("Osama", 38, "Egypt"))
print("="*100)
print(say_hello())
# -----------------------
# Assignment #1 --> Second Sheet


def get_score(**subjects):
    for subject, score in subjects.items():
        print(f"{subject} => {score}")
    return


get_score(Math=90, Science=80, Language=70)
print("="*100)
get_score(Logic=70, Problems=60)
# -----------------------
# Assignment #2 --> Second Sheet


def get_people_scores(name="", **subjects):
    if not subjects:
        print(f"Hello {name}, you have no scores to show.")
    else:
        if name:
            print(f"Hello {name}, this is your score table: ")
        else:
            pass

        for subject, score in subjects.items():
            print(f"{subject} => {score}")
    return


get_people_scores("Osama", Math=90, Science=80, Language=70)
print("="*100)
get_people_scores("Mahmoud", Logic=70, Problems=60)
print("="*100)
get_people_scores(Logic=70, Problems=60)
print("="*100)
get_people_scores("Ahmed")
print("="*100)
# -----------------------
# Assignment #3 --> Second Sheet
scores_list = {
    "Math": 90,
    "Science": 80,
    "Language": 70
}


def get_the_scores(name="", **scores_list):
    if not name:
        for subject, score in scores_list.items():
            print(f"{subject} => {score}")
            return

    else:
        if not scores_list:
            print(f"Hello {name}, you have no scores to show.")
            return
        else:
            print(f"Hello {name}, this is your score table.")
            for subject, score in scores_list.items():
                print(f"{subject} => {score}")
    return


get_the_scores("Osama", **scores_list)
print("="*100)
get_the_scores("Osama")
print("="*100)
get_the_scores(**scores_list)
