class Animal:
    def __init__(self):
        self.living_thing = True
        self.response_to_stimuli = True
        self.name = ""

    def animalise(self):
        print(f"{self.name} uses Animalise! It is a move unique to animals!")
    
class Mammal(Animal):
    def __init__(self):
        super().__init__() # super refers to the super class put in the brackets upon defining the class

        self.mother_produces_milk = True
        self.blood_temp = "warm-blooded"

    def blood_boil(self):
        print(f"{self.name} uses Blood Boil! It is a move unique to mammals!")

class Human(Mammal):
    def __init__(self):
        super().__init__() # NOTE the call to superclass is recommended but not strictly necessary, as logn as you have the (superclass) in teh class bracket

        self.birth_method = "born alive"

    def big_brain(self):
        print(f"{self.name} uses Big Brain! It is a move unique to humans!")

steve = Human()
steve.name = "Steve"

# Class Attributes
print(f"\n        steve.living_thing: {steve.living_thing}")
print(f" steve.response_to_stimuli: {steve.response_to_stimuli}")
print(f"steve.mother_produces_milk: {steve.mother_produces_milk}")
print(f"          steve.blood_temp: {steve.blood_temp}")
print(f"        steve.birth_method: {steve.birth_method}")
print(f"                steve.name: {steve.name}\n")

# Class Methods
steve.animalise()
steve.blood_boil()
steve.big_brain()