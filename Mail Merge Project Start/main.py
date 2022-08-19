with open("./Input/Names/invited_names.txt") as name_file:
    for name in name_file.readlines():
        name_strip = name.strip()
        with open("./Input/Letters/starting_letter.txt") as letter_file:
            new_letter = letter_file.read().replace("[name]", name_strip)
        with open(f"./Output/ReadyToSend/letter_for_{name_strip}.txt", mode="w") as ready_file:
            ready_file.write(new_letter)
