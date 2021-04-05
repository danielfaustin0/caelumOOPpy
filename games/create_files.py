"""Arquivos para os jogos

Mar 31 2021 - Daniel Faustino
"""

import random

 # TODO: create functions to handle with files
file = "games/files/words_file.txt"
words = []


def add_words(word): # Open and Close the file
    with open(file, "a") as words_file:
        words_file.write(f"{word}\r\n")


def checking_input(word): # Receive user input
    if word.isalpha():
        print("Palavra aceita.")
        add_words(word)
    else:
        print("""Você deve:
        *- Digitar uma palavra por vez
        *- Não usar espaços
        *- Não usar números
        """)


def user_input():
    while True:
        word = input("Enter new word (or 'q' to quit): ").upper()

        if word == "Q":
            break
        else:
            checking_input(word)


def listing_words():
    with open(file, "r") as words_file:
        for line in words_file:
            line = line.strip()
            words.append(line)


def choosing_word():
    listing_words()
    pos = random.randrange(0, len(words))
    return words[pos]


palavra = choosing_word()
print(palavra)
