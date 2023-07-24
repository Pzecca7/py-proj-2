import csv
from pprint import pprint
from abc import ABC, abstractmethod

class Cupcake(ABC):

    size = "regular"

    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)
    
    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price
    
# my_cupcake = Cupcake("Red Velvet", 2.99, "Cocoa", "Cream Cheese", "Cream Cheese")
# print(my_cupcake.name)

# my_cupcake.add_sprinkles("Hearts", "Cake Crumble", "Vanilla" )
# print(my_cupcake.sprinkles)

# my_cupcake.frosting = "Chocloate"
# my_cupcake.filling = "Chocolate"
# my_cupcake.name = "Triple Choclate"
# my_cupcake.is_miniature = False

# print(my_cupcake.is_miniature)
# print(my_cupcake.name)
# print(my_cupcake.filling)
# print(my_cupcake.frosting)


class Mini(Cupcake): 

    size = "mini"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
    
    def calculate_price(self, quantity):
        return quantity * self.price

my_mini_cupcake = Mini("Vanilla Fudge", 1.99, "Vanilla", "Chocolate")
print(my_mini_cupcake.name)
print(my_mini_cupcake.price)
print(my_mini_cupcake.size)
print(my_mini_cupcake.flavor)
print(my_mini_cupcake.frosting)

class Regular(Cupcake):

    size = "regular"

    def calculate_price(self, quantity):
        return quantity * self.price

class Large(Cupcake):

    size = "Large"

    def calculate_price(self, quantity):
        return quantity * self.price


cupcake1 = Mini("Vanilla Fudge", 1.99, "Vanilla", "Chocolate")
cupcake1.add_sprinkles("Rainbow")
cupcake2 = Regular("Red Velvet", 2.99, "Cocoa", "Cream Cheese", "Cream Cheese")
cupcake2.add_sprinkles("Red and White Hearts")
cupcake3 = Large("Oreo Bomb", 3.99, "Chocolate", "Cookies and Cream", "Fudge")
cupcake3.add_sprinkles("Oreo Crumbs", "Chocolate")
cupcake4 = Mini("Lemon", 1.99, "Lemon", "Vanilla")
cupcake4.add_sprinkles("White Pearls")
cupcake5 = Large("Birthday Cake", 3.99, "Vanilla", "Vanilla", "Vanilla")
cupcake5.add_sprinkles("Confetti", "Rainbow", "Birthday Truffles")

cupcake_list = [cupcake1, cupcake2, cupcake3, cupcake4, cupcake5]

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

read_csv("sample.csv")

def write_new_csv(file, cupcakes): 
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({
                    "size": cupcake.size,
                    "name": cupcake.name,
                    "price": cupcake.price,
                    "flavor": cupcake.flavor,
                    "frosting": cupcake.frosting,
                    "sprinkles": cupcake.sprinkles,
                    "filling": cupcake.filling
                })
            else: 
                writer.writerow({
                    "size": cupcake.size,
                    "name": cupcake.name,
                    "price": cupcake.price,
                    "flavor": cupcake.flavor,
                    "frosting": cupcake.frosting,
                    "sprinkles": cupcake.sprinkles,
                })

write_new_csv("cupcakes.csv", cupcake_list)

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
         fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]

         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

         if hasattr(cupcake, "filling"):
            writer.writerow({
                "size": cupcake.size,
                "name": cupcake.name,
                "price": cupcake.price,
                "flavor": cupcake.flavor,
                "frosting": cupcake.frosting,
                "sprinkles": cupcake.sprinkles,
                "filling": cupcake.filling
            })
         else: 
            writer.writerow({
                "size": cupcake.size,
                "name": cupcake.name,
                "price": cupcake.price,
                "flavor": cupcake.flavor,
                "frosting": cupcake.frosting,
                "sprinkles": cupcake.sprinkles,
            })



add_cupcake("cupcakes.csv", Regular("Chocolate Peanut Butter", 2.99, "Chocolate", "Peanut Butter", "Chocolate"))


def get_cupcakes(file):
    with open(file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader


pprint(get_cupcakes("cupcakes.csv"))

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
         fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]

         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
         writer.writerow(cupcake)
         


