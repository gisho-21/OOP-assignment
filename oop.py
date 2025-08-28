# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def call(self, number):
        print(f"{self.model} is calling {number}... 📞")

    def charge(self):
        print(f"{self.model} is charging... 🔋")

    def info(self):
        print(f"{self.brand} {self.model} - {self.storage}GB, {self.battery}mAh")


# Inherited class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        print(f"{self.model} is playing {game} 🎮 with {self.cooling_system} cooling system!")

    # Overriding method
    def info(self):
        print(f"{self.brand} {self.model} - {self.storage}GB, {self.battery}mAh, Cooling: {self.cooling_system}")


# activity Polymorphism Challenge!

class Animal:
    def move(self):
        print("Animals can move")

class Dog(Animal):
    def move(self):
        print("The dog runs 🐕")

class Bird(Animal):
    def move(self):
        print("The bird flies 🕊️")

class Fish(Animal):
    def move(self):
        print("The fish swims 🐟")


# Vehicle Example
class Vehicle:
    def move(self):
        print("Vehicles can move")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

