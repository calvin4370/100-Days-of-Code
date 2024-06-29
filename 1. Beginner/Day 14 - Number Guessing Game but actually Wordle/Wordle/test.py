with open("guesses.txt", "r") as file:
    raw_valid_guesslist = file.readlines()
    valid_guesslist = []
    for word in raw_valid_guesslist:
        valid_guesslist.append(word.strip().upper())

            
with open("answers.txt", "r") as file:
    raw_possible_wordlist = file.readlines()
    possible_wordlist = []
    for word in raw_possible_wordlist:
        possible_wordlist.append(word.strip().upper())

for word in possible_wordlist:
    print(f"{word}")

for word in valid_guesslist:
    print(f"{word}")

print(f"possible_wordlist has {len(possible_wordlist)} words")
print(f"valid_guesslist has {len(valid_guesslist)} words")

intersections = 0
missing = 0
for word in possible_wordlist:
    if word in valid_guesslist:
        intersections += 1
    else:
        missing += 1

print(f"possible_wordlist and valid_guesslist have {intersections} intersections")
print(f"{missing} words are missing")