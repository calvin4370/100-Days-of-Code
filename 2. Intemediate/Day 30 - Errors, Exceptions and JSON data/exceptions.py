try:
    # Do something that might cause an Error,
    # For each line that does not cause an error, it will trigger no problem
    pass
except:
    # Do this if there WAS an Error
    pass
else:
    # Do this if there WAS NO Error
    pass
finally:
    # Do this EITHER WAY
    pass

"""
Examples of Errors (Not all of them)
"""
# FileNotFoundError
try:
    with open("random_file.txt", "r") as file:
        print("Success!")
except FileNotFoundError:
    print("FileNotFoundError")
except AssertionError:
    print("Weird, this could not possibly have triggered")

# IndexError
holos = ["Marine", "Fubuki", "Suisei", "Nene", "Korone", "Okayu"]
try:
    print(holos[10])
except IndexError:
    print("IndexError")

# KeyError
mushokus = {
    "Rudeus":"Mage",
    "Roxy":"Mage",
    "Sylphiette":"Mage",
    "Eris":"Warrior"
}
try:
    value = "Hi"
    print(mushokus["Ruijierd"])
except KeyError as error_message:
    print(f"The key: {error_message} does not exist")

# TypeError
number = 16
try:
    number += 'string'
except TypeError:
    print("TypeError")