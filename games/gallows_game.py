"""Jogo da Forca
 
 O jogo consiste em pedir que o usuário descubra a palavra escondida.
 Para isso, o usuário deverá dar palpites sobre as letras que ele
  acredita que existem na palavra.

 O programa exibe para o usuário as letras que acerta e erra.

 
 Feb 19 2021 - Daniel Faustino
"""

# TODO DONE: Create a list to recieve the right guess
# TODO DONE: Show the wrong guess
# TODO DONE: Beautify the output from discovered_letters
# TODO DONE: Clear the game screen

import time
import os
import create_files as word

def clear():
    os.system('clear')


def game_intro():
    print("""
    =-=-=-==-=-=-==-=-=-==-=-=-==-=-=-=
    =-=-=-=-=- Jogo da Forca -=-=-=-=-=
    Descubra a palavra oculta.
    =-=-=-==-=-=-==-=-=-==-=-=-==-=-=-=
    
    """)


def getting_hidden_word():
    return word.choosing_word()
    

def wrong_attempts(letter):
    if letter in wrong_guess:
        print(f"Letter {letter} was already used.")
    else:
        wrong_guess.append(letter)
        print(f"Letter {letter} isn't in hidden word.")
    time.sleep(2.4)


def user_input():
    user_letter = input("Enter a letter: ").upper()
    checking_input(user_letter)


def checking_input(user_letter):
    if user_letter.isalpha and len(user_letter) == 1:
        checking_letter(user_letter)
    else:
        input_rules()
        

def checking_letter(letter):
    if letter in hidden_word:
        allocate_letter(letter)
    else:
        wrong_attempts(letter)


def input_rules():
    clear()
    print("""
    =-=-=-==-=-=-==-=-=-==-=-=-==-=-=-=
    =-=-=-=-=-| INPUT RULES |-=-=-=-=-=
    - Don't use numbers.
    - Don't use spaces.
    - Enter just a letter at time
    =-=-=-==-=-=-==-=-=-==-=-=-==-=-=-=
    
    """)
    time.sleep(3.5)


def allocate_letter(letter):
    letter_position = 0
    for hidden_letter in hidden_word:
        if hidden_letter == letter:
            found_letters[letter_position] = letter
        else:
            pass
        letter_position += 1
    


if __name__ == "__main__":
    wrong_guess = []
    hidden_word = getting_hidden_word()
    found_letters = ["_" for i in hidden_word]
    

    while True:
        
        clear()
        game_intro()

        if "_" in found_letters:
            print(f"WRONG GUESSES: {'-'.join(wrong_guess)}")
            print(f"HIDDEN WORD: {''.join(found_letters)}")
            user_input()
        else:
            print(f"HIDDEN WORD: {' '.join(found_letters)}")
            break
            
        
        # clear()
    