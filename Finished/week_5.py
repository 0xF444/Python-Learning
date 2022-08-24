# Assignment #1
# -------------
# print(True)
# print(bool(1))
# print(bool(1.01))
# print(bool("hi"))
# print(bool({1, 2}))
# print(bool((1, 2)))
# print(bool([1, 2]))
# They're all true.
# print(False)
# print(bool(0))
# print(bool({}))
# print(bool([]))
# print(bool(()))
# They're all false.
# -------------
# Assignment #2
# html = 80
# css = 60
# javascript = 70
# print(html > 50 and css > 50 and javascript > 50)
# -------------
# Assignment #3
# n1 = 10
# n2 = 20
# n = 20
# print(n > n1 or n > n2)
# print(n > n1 and n > n2)
# -------------
# Assignment #4
# n1 = 10
# n2 = 20
# result = n1 + n2
# print(result)
# result **= 3
# print(result)
# result %= 26000
# print(result)
# result /= 5
# print(result)
# result = str(result)
# print(type(result))
# -------------------------------------------------------------
# Assignment #1
# name = input("Please enter your name.\n")
# name = name.strip().capitalize()
# print(f"Hello {name}, Happy to see you here.\n")
# -------------
# Assignment #2
# age = input("Please enter your age.\n")
# age = int(age)
# if age < 16:
#     print("Hello, your age is under 16, Some articles are not suitable for you.\n")
# else:
#     print(f"Hello, your age is {age}, All articles are suitable for you.\n")
# -------------
# Assignment #3
# fname = input("Please enter your first name.\n")
# sname = input("Please enter your second name.\n")
# fname = fname.strip().capitalize()
# sname = sname.strip().capitalize()
# print(f"Hello {fname} {sname:.1s}.")
# -------------
# Assignment #4
# email = input("Please enter your email.\n")
# email = email.strip().lower()
# fname = email[:email.index("@")].capitalize()
# prov = email[email.index("@")+1:email.index(".")]
# dom = email[email.index("."):]
# print(
#     f"Your name is {fname}\nYour E-mail Service Provider is {prov}\nTop Level Domain is {dom}\n")
