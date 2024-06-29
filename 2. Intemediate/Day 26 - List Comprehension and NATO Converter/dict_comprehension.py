"""
DICTIONARY COMPREHENSION
new_dict = {new_key:new_value for element in iterable if condition}
new_dict = new_key:new_value for (key,value) in dict.items() if condition}
"""
people = {"Rudeus":"Mage", "Sylphiette":"Mage", "Roxy":"Mage", "Eris":"Warrior", "Ruijierd":"Warrior", "Zenith":"Healer"}

values = {value for key, value in people.items()}
print(values)
# {'Mage', 'Warrior', 'Healer'}
# NOTE that a set is produced if not a dict which is why elements are not repeated

same_dict = {key:value for key, value in people.items()}
print(same_dict)
# {'Rudeus': 'Mage', 'Sylphiette': 'Mage', 'Roxy': 'Mage', 'Eris': 'Warrior', 'Ruijierd': 'Warrior', 'Zenith': 'Healer'}

mages = {key for key, value in people.items() if value == "Mage"}
print(mages)
# {'Roxy', 'Rudeus', 'Sylphiette'}


list = [["Rudeus", "Mage"], ["Sylphiette","Mage"], ["Roxy","Mage"], ["Eris","Warrior"], ["Ruijierd","Warrior"], ["Zenith","Healer"]]
dict = {name:class_ for name, class_ in list}
print(dict)
# {'Rudeus': 'Mage', 'Sylphiette': 'Mage', 'Roxy': 'Mage', 'Eris': 'Warrior', 'Ruijierd': 'Warrior', 'Zenith': 'Healer'}