import csv

with open("weather_data.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)

print(reader)