from bs4 import BeautifulSoup
import requests

url = "https://www.wordunscrambler.net/word-list/wordle-word-list"

# The requests module's get function is used to send a request to the https website with a GET request
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to retrieve webpage. Status code:", response.status_code)
    quit()

soup = BeautifulSoup(html_content, "lxml")


list_of_wordle_words_starting_with_each_letter = soup.find_all("ul", class_="list-unstyled")

list_of_lists_of_all_anchors_by_letter = []
for letter in list_of_wordle_words_starting_with_each_letter:
    list_of_lists_of_all_anchors_by_letter.append(letter.find_all("a"))

wordle_possible_words = []
for list_of_anchors_by_letter in list_of_lists_of_all_anchors_by_letter:
    for anchor in list_of_anchors_by_letter:
        wordle_possible_words.append(anchor.text)
"""
for word in wordle_possible_words:
    print(word)

print(len(wordle_possible_words))
"""

with open("wordle_possible_words.txt", "w") as file:
    for word in wordle_possible_words:
        file.write(f"{word}\n")
print("\nFile created")