import pandas as pd

data = pd.read_csv("weather_data.csv")

print(data)
"""
         day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny
"""

# Get data im column
print(data["temp"])
"""
0    12
1    14
2    15
3    14
4    21
5    22
6    24
Name: temp, dtype: int64
"""

# Get data in row
print(data[data.day == "Friday"])
"""
      day  temp condition
0  Friday    21     Sunny
"""

# Get data in row where condition is Rain
print(data[data.condition == "Rain"])
"""
         day  temp condition
1    Tuesday    14      Rain
2  Wednesday    15      Rain
"""

# Get data in row where the temp is the highest
print(data[data.temp == data.temp.max()])
"""
      day  temp condition
6  Sunday    24     Sunny
"""

