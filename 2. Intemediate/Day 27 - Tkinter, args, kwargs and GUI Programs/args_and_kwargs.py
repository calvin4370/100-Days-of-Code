"""
Optional Arguments (arguments with default values)
--------------------------------------------------
"""
def function(a=1, b=2, c=3):
    print(sum([a, b, c]))


"""
*args (Many Positional Arguments)
---------------------------------
NOTE args is the name of the tuple of (unnamed) positional arguments and can be renamed, but the convention is to use *args
These are positional arguments as their position matters as the args are unnamed, and the index of the args will refer to different args
"""
def sum_all(*args):
    total = 0
    for arg in args:
        total += int(arg)
    print(total)

sum_all(10, 20, 30)
# 60

def group(*people):
    print(f"{people[0]} is the group leader")
    print("Members:")
    for person in people[1:]:
        print(f"- {person}")

group("Rudeus", "Roxy", "Sylphiette", "Eris")
# Rudeus is the group leader
# Members:
# - Roxy
# - Sylphiette
# - Eris

"""
**kwargs (Many Keyword Arguments)
---------------------------------
NOTE kwargs is the name of the DICTIONARY of (named) keyword arguments (kwarg:value) pairs and can be renamed, but the convention is to use **kwargs
"""
def make_dict(**kwargs):
    print(kwargs)

make_dict(Rudeus="Mage", Eris="Warrior", Zenith="Healer")
# {'Rudeus': 'Mage', 'Eris': 'Warrior', 'Zenith': 'Healer'}

def state_class(**key_value_pairs):
    for key, value in key_value_pairs.items():
        print(f"{key} is a {value}")

state_class(Rudeus="Mage", Eris="Warrior", Zenith="Healer")
# Rudeus is a Mage
# Eris is a Warrior
# Zenith is a Healer

def calculate(start, **kwargs):
    final = start
    try:
        final += kwargs["add"]
    except KeyError:
        pass
    try:
        final -= kwargs["minus"]
    except KeyError:
        pass
    try:
        final *= kwargs["times"]
    except KeyError:
        pass
    try:
        final /= kwargs["divide"]
    except KeyError:
        pass

    print(final)

calculate(1, add=9, times=2)
# 20
calculate(10, times=2, divide=5)
# 4.0

"""NOTE that kwargs just hides the keyword args from the mini documentation but you will still experience keyerrors like so:"""
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        print(f"I am a {self.make.title()} {self.model.title()}")

car = Car(make="toyota", model="vios")
# I am a Toyota Vios

"""NOTE that to circumvent this, use the dictionary method get()"""
class Car2:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make", "Default")
        self.model = kwargs.get("model")
        print(f"I am a {self.make} {self.model}")

car2 = Car2()
# I am a Default None
