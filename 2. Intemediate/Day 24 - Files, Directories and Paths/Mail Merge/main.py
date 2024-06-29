with open("list_of_subscribers.txt", "r") as file:
    names = file.readlines()

with open("letter_template.txt", "r") as file:
    template = file.readlines()

for name in names:
    with open(f"letters/{name.strip()}.txt", "w") as letter:
        letter.write(f"{template[0].strip()} {name.strip()},\n")

        letter.writelines(template[1:])