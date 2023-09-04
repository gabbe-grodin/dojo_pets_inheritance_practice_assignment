import pet

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        print(f"{self.first_name} is walking their pet, {self.pet.name}, a {self.pet.type}.")
        self.pet.play()
        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        print(f"{self.first_name} is feeding {self.pet.name}, the {self.pet.type}, {self.pet_food}.")
        self.pet.eat()
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(f"{self.first_name} is bathing their pet {self.pet.type} named {self.pet.name}.")
        # print(f"{self.pet.name} says: '{self.pet.noise}'")
        self.pet.noise()
        return self

print("\n")
ninja_01 = Ninja("Wizard", "Loving", pet.pet_01, "Ants", "flies 'n grubs")
ninja_01.walk().feed().bathe()
print("\n")
ninja_02 = Ninja("Laura", "L", pet.pet_02, "mosquitos", "all the bugs")
ninja_02.bathe().feed().walk()
print("\n")