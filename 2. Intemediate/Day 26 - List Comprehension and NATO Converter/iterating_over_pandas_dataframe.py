import pandas
"""
Iterating over Pandas DataFrame
"""

student_results = {
    "students": ["Rudeus", "Sylphiette", "Eris", "Ghislaine"],
    "Fire": [70, 62, 20, 16],
    "Water": [88, 71, 33, 27],
    "Wind": [76, 69, 28, 15],
    "Earth": [89, 57, 30, 10],
    
    "Sword God": [39, 17, 82, 90],
    "Water God": [37, 20, 70, 75],
    "North God": [36, 22, 73, 78]
}

dataframe = pandas.DataFrame(student_results)
print(dataframe)
#      students  Fire  Water  Wind  Earth  Sword God  Water God  North God
# 0      Rudeus    70     88    76     89         39         37         36
# 1  Sylphiette    62     71    69     57         17         20         22
# 2        Eris    20     33    28     30         82         70         73
# 3   Ghislaine    16     27    15     10         90         75         78

# Looping through datafram
for key, value in dataframe.items():
    print(key)
# students
# Fire
# Water
# Wind
# Earth
# Sword God
# Water God
# North God
    
for key, value in dataframe.items():
    print(value)
# 0        Rudeus
# 1    Sylphiette
# 2          Eris
# 3     Ghislaine
# Name: students, dtype: object
# 0    70
# 1    62
# 2    20
# 3    16
# Name: Fire, dtype: int64
# 0    88
# 1    71
# 2    33
# 3    27
# Name: Water, dtype: int64
# 0    76
# 1    69
# 2    28
# 3    15
# Name: Wind, dtype: int64
# 0    89
# 1    57
# 2    30
# 3    10
# Name: Earth, dtype: int64
# 0    39
# 1    17
# 2    82
# 3    90
# Name: Sword God, dtype: int64
# 0    37
# 1    20
# 2    70
# 3    75
# Name: Water God, dtype: int64
# 0    36
# 1    22
# 2    73
# 3    78
# Name: North God, dtype: int64

print("\n\n\n")
"""Use pandas method .iterrows() to iterate through rows of a pandas dataframe"""
for index, row in dataframe.iterrows():
    print(index)
0
1
2
3

for index, row in dataframe.iterrows():
    print(row, "\n")
# students     Rudeus
# Fire             70
# Water            88
# Wind             76
# Earth            89
# Sword God        39
# Water God        37
# North God        36
# Name: 0, dtype: object
    
# students     Sylphiette
# Fire                 62
# Water                71
# Wind                 69
# Earth                57
# Sword God            17
# Water God            20
# North God            22
# Name: 1, dtype: object
    
# students     Eris
# Fire           20
# Water          33
# Wind           28
# Earth          30
# Sword God      82
# Water God      70
# North God      73
# Name: 2, dtype: object
    
# students     Ghislaine
# Fire                16
# Water               27
# Wind                15
# Earth               10
# Sword God           90
# Water God           75
# North God           78
# Name: 3, dtype: object
