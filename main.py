
with open("./Input/Names/invited_names.txt", "r") as file:
    list_names = [linea.rstrip() for linea in file]

with open("./Input/Letters/starting_letter.txt", "r") as file:
    list_letters = [linea.rstrip() for linea in file]


for name in list_names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        list_letters[0] = f"Dear [{name}]"
        string = " ".join(list_letters)
        file.write(string)



