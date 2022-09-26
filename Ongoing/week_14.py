# Assignment #1
# -----
class Game:
    def __init__(self,name,dev,year,price) -> None:
        self.name = name
        self.developer = dev
        self.year = year
        self.price = price
    def price_in_pounds(self):
        return self.price*15.6
game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {float(game_one.price_in_pounds())}", end="")
print("\n")
print("#"*150)
# Assignment #2
# -----
class User:
    def __init__(self,fname,mname,age,gender) -> None:
        self.fname = fname
        self.mname = mname
        self.age = age
        self.gender = gender
    def full_details(self):
        if self.gender == "Male" or self.gender == "male":
            g = "Mr"
        else: 
            g = "Mrs"
        if self.age >40:
            print("Please enter an age less than 40.")
            return ""
        return f"Hello {g} {self.fname} {self.mname[0]}. [{str((40-self.age)).zfill(2)}] to reach 40."
user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 50, "Female")

print(user_one.full_details()) 
print(user_two.full_details())
print("#"*150)
# Assignment #3
# -----
class Message:
    content = "Hello From Class Message."
    def __init__(self) -> None:
        pass
    @classmethod
    def print_message(cls):
        return cls.content
print(Message.print_message())
print("#"*150)
# Assignment #4
# -----
class Games:
    def __init__(self,listofgames) -> None:
        self.list = listofgames
    def show_games(self):
        if type(self.list)==str:
            print(f"I have one game called \"{self.list}\"")
            return ""
        elif type(self.list)==list:
            print("I have many games:")
            for game in self.list:
                print(f"# -- {game}")
            return ""
        elif type(self.list)==int:
            print(f"I have {self.list}")
        
my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)
my_game.show_games()
my_games_names.show_games()
my_games_count.show_games()
# Assignment #5
# -----
