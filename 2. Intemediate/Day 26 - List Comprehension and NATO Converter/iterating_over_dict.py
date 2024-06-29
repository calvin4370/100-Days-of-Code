people = {
    "Rudeus":"Mage", 
    "Sylphiette":"Mage", 
    "Roxy":"Mage", 
    "Eris":"Warrior", 
    "Ruijierd":"Warrior", 
    "Zenith":"Healer"
    }

"""NOTE: REMEMBER TO USE HTE items() METHOD ON THE DICT TO GET TUPLES OF THE (key, value)s IN THE DICT"""

for person in people.items():
    print(person)
# ('Rudeus', 'Mage')
# ('Sylphiette', 'Mage')
# ('Roxy', 'Mage')
# ('Eris', 'Warrior')
# ('Ruijierd', 'Warrior')
# ('Zenith', 'Healer')

print()

for name, class_ in people.items():
    print(f"{name} is a {class_}")
# Rudeus is a Mage
# Sylphiette is a Mage
# Roxy is a Mage
# Eris is a Warrior
# Ruijierd is a Warrior
# Zenith is a Healer