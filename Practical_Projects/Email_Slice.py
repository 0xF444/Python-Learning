name = input("What\'s your name?\n")
email = input("What\'s your email?\n")
name = name.strip().capitalize()
email = email.strip()
usr = email[:email.index("@")]
dom = email[email.index("@")+1:]
print(f"Hello {name}, your email is {email}\nYour username is {usr} and your domain is {dom}.")
