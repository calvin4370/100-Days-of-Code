old_list = [1, 2, 3, 4]
"""
LIST COMPREHENSION
new_list = [new_item for old_item in old_list]
"""
new_list = [2 * x for x in old_list]
print(new_list)
# [2, 4, 6, 8]


even_numbers = [2 * x for x in range(1, 5)]
print(even_numbers)
# [2, 4, 6, 8]


"""
LIST COMPREHENSION WITH CONDITION
new_list = [new_item for old_item in old_list if (condition)]
"""
names = ['Rudeus', 'Sylphiette', 'Eris', 'Linia', 'Roxy', 'Purrsena']
short_names = [name for name in names if len(name) <= 5]
long_names = [name for name in names if len(name) > 5]

print(short_names)
print(long_names)
# ['Eris', 'Linia', 'Roxy']
# ['Rudeus', 'Sylphiette', 'Purrsena']

numbers = [0, 1010, 1111, 1212, 1223, 1234, -500, -501, 3.1415, -3.1415926535898323]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
# [0, 1010, 1212, 1234, -500]
negative_numbers = [number for number in numbers if number < 0]
print(negative_numbers)
# [-500, -501, -3.141592653589832]
floats = [number for number in numbers if type(number) == float]
print(floats)
# [3.1415, -3.141592653589832]
