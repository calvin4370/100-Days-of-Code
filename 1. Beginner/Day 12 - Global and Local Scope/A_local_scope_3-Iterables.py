shopping_list = ["eggs", "sugar", "flour"]

# Reads a list and returns it
def readlist(list):
    return list

print(readlist(shopping_list))
#>>> ['eggs', 'sugar', 'flour']

# Appends a string to the end of a list
def iwantatoy(list):
    list.append("toy")

# NOTE that functions can append to lists, thereby changing their value in the global scene
iwantatoy(shopping_list)
print(shopping_list)
#>>> ['eggs', 'sugar', 'flour', 'toy']




playing_card = {
    "face":"Ace",
    "suit":"Hearts"
}

def read_dict(dict):
    print(dict)

read_dict(playing_card)
#>>> {'face': 'Ace', 'suit': 'Spaces'}

def hot(card):
    card["face"] = "Queen"
    card["suit"] = "Spades"

# NOTE that functions can change the value of iterables, like a dictionary in the global scene
hot(playing_card)
print(playing_card)
#>>> {'face': 'Queen', 'suit': 'Spades'}


# NOTE that this won't work with tuples, as they are immutable
# LEARNING POINT: functions can modify mutable iterables but not primitive variables in the global scene