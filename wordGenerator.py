import json
from random import shuffle

with open("letters.json", 'r') as letters_file:
    letters = json.load(letters_file)
new_letters = []
while letter_input := input("New Letter? "):
    new_letters.append(letter_input[0].upper())
if any(new_letter not in letters for new_letter in new_letters):
    with open("letters.json", 'w') as letters_file:
        json.dump(list(set(letters + new_letters)), letters_file, indent=4)
letters = set(letters)
with open("words.json", 'r') as words_file:
    words = json.load(words_file)
new_words = [word for word in words if all(char in letters for char in word)]
shuffle(new_words)

n = int(input("How many words? "))

with open("out.txt", 'w') as out:
    out.write(' '.join(new_words[:n]))