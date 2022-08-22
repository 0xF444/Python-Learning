age = int(input("What\'s your age?\n").strip())
months = age*12
weeks = months*4
days = age*365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(
    f"You have lived {months} months\n{days} days\n{hours} hours \n{minutes} minutes\n{seconds} seconds")
