import pandas

# Creating a dataframe from scratch
student_results = {
    "students": ["Rudeus", "Sylphiette", "Eris", "Ghislaine"],
    "Sword God": [39, 17, 82, 90],
    "Water God": [37, 20, 70, 75],
    "North God": [36, 22, 73, 78],

    "Fire": [70, 62, 20, 16],
    "Water": [88, 71, 33, 27],
    "Wind": [76, 69, 28, 15],
    "Earth": [89, 57, 30, 10]
}

dataframe = pandas.DataFrame(student_results)
print(dataframe)
"""
     students  Sword God  Water God  North God  Fire  Water  Wind  Earth
0      Rudeus         39         37         36    70     88    76     89
1  Sylphiette         17         20         22    62     71    69     57
2        Eris         82         70         73    20     33    28     30
3   Ghislaine         90         75         78    16     27    15     10
"""

# Create a csv version from this pandas DataFrame
dataframe.to_csv("dataframe.csv")