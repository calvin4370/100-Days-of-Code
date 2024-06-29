import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
dataframe = pandas.read_csv('nato_phonetic_alphabet.csv')
#    letter      code
# 0       A      Alfa
# 1       B     Bravo
# ...   ...       ...
# 25      Z      Zulu

for index, row in dataframe.iterrows():
    #print(row)
    pass
# letter       A
# code      Alfa
# Name: 0, dtype: object
# letter        B
# code      Bravo
# Name: 1, dtype: object
# ...         ...
# letter       Z
# code      Zulu
# Name: 25, dtype: object

conversion_dict = {row["letter"]:row["code"] for index, row in dataframe.iterrows()}
# {'A': 'Alfa', 'B': 'Bravo', ..., 'Z': 'Zulu'}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word to be converted to NATO: ")

nato_phrase = ""
for letter in user_input:
    nato = conversion_dict[letter.upper()]
    nato_phrase += nato + " "

print(nato_phrase.rstrip(), "\n")
