# import ninja # why when i import ninja is that file running when i only call this one?
# How to avoid circular imports so i can associate both directions- add/invoke instance before class with dot notation?

class Pet:
    def __init__(self, name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.health = 100
        self.energy = 10
    
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy = self.energy + 25
        print(f"{self.name}, the {self.type}, is sleeping. They now have {self.energy} grams of energy.")
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        print(f"{self.name} is eating. Energy increased to: {self.energy}. Health increased to: {self.health}")
        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health = self.health + 5
        print(f"{self.name} is playing. Health increased to: {self.health}")
        return self
    
    # noise() - prints out the pet's sound
    def noise(self):
        print(f"{self.name} makes the sound '{self.sound}'.")
        return self

class CatPet(Pet):
    def __init__(self, name, type, tricks, sound, is_feral):
        super().__init__(name, type, tricks, sound)
        self.is_feral = is_feral

class DogPet(Pet):
    def __init__(self, name, type, tricks, sound, is_mutt):
        super().__init__(name, type, tricks, sound)
        self.is_mutt = is_mutt

pet_01 = Pet("Doctor", "Gila Monster", "doesn't blink for hours", "hmmmmmmmmmmm")
# pet_01.sleep().eat()

dogpet_01 = DogPet("Sancho","Standard Poodle", "impersonate a fluffy smiling cloud", "arf. arf.", True)
# dogpet_01.sleep()

catpet_01 = CatPet("Garak","Short-haired domestic cat", "pees in toilet", "meowprrrrr", False)
# catpet_01.sleep().play()

pet_02 = Pet("Pixel", "Jumping Spider", "hides for weeks and turns up when you least expect it.", "ugh!")
