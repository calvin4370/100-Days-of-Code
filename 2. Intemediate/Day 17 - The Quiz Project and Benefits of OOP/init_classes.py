class Car:
    # The init function (The constructor) is called every time an object is initialised
    def __init__(self, brand, model, year="", seats=5):
        self.brand = brand
        self.model = model
        self.year = year

        self.seats = seats

    def intro(self):
        print(f"This car is a {self.brand} {self.model} {self.year}")
        print(f"It has {self.seats} seats")

toyota_corolla = Car("Toyota", "Corolla", "2023", 5)
toyota_corolla.intro()

