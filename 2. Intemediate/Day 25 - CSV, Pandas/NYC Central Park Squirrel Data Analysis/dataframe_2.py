import pandas
"""
We are working with the massive csv file: "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
It has [3023 rows x 31 columns]:
X, Y, Unique Squirrel ID, Hectare,Shift, Date, Hectare Squirrel Number, Age, Primary Fur Color, Highlight Fur Color, Combination of Primary and Highlight Color, Color notes, Location,
Above Ground Sighter Measurement, Specific Location, Running, Chasing, Climbing, Eating, Foraging, Other Activities, Kuks, Quaas, Moans, Tail flags, Tail twitches, Approaches, Indifferent, 
Runs from, Other Interactions, Lat/Long
"""
# Create a pandas dataframe, read the csv into it
dataframe = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Convert the big csv to a smaller one with only the columns we want


# Get the totals of squirrels of a particular fur colour
primary_fur_color_series = dataframe["Primary Fur Color"]
# print(primary_fur_color_series)
"""
0            NaN
1           Gray
2       Cinnamon
3           Gray
4            NaN
          ...
3018        Gray
3019        Gray
3020        Gray
3021        Gray
3022    Cinnamon
Name: Primary Fur Color, Length: 3023, dtype: object
"""
# This gets just the 2473 rows x 31 columns of primary fur color: grey squirrels
gray_squirrels = dataframe[dataframe["Primary Fur Color"] == "Gray"]

gray_count = len(gray_squirrels)
# 2473

cinnamon_count = len(dataframe[dataframe["Primary Fur Color"] == "Cinnamon"])
black_count = len(dataframe[dataframe["Primary Fur Color"] == "Black"])

new_dict = {
    "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

mini_dataframe = pandas.DataFrame(new_dict)
print(mini_dataframe)
"""
  Primary Fur Color  Count
0              Gray   2473
1          Cinnamon    392
2             Black    103
"""