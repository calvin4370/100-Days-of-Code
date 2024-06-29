"""
If you want a function to modify a global variable, you must call global inside the function, to that specific variable
"""
enzyme_state = "inactivated"

def coenzyme():
    global enzyme_state
    enzyme_state = "activated"

coenzyme()
print(enzyme_state)
#>>> activated

"""
If a global variable doesn't exist, you can create one inside a function, using global
"""
# Look, the order here doesn't matter
def check_goblin():
    print(goblin)
def create_global_goblin():
    global goblin
    goblin = "Ugly Bastard"

create_global_goblin()
check_goblin()
#>>> Ugly Bastard

"""
Learning points:
Example 1 is especially useful when you are doing a main() and many functions setup,
as you will likely define many variables inside main() and need to access them in your other functions

This is not necessary for iterables such as lists and dictionaries due to the concept of mutability
or primitive vs not primitive data types
"""
