"""Jogo da Forca
 
 O jogo consiste em pedir que o usuário descubra a palavra escondida.
 Para isso, o usuário deverá dar palpites sobre as letras que ele
  acredita que existem na palavra.

 O programa exibe para o usuário as letras que acerta e erra.

 
 Feb 19 2021 - Daniel Faustino
"""

import time
import os
import create_files as word
import boards


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

def hiding_word(hidden_word):
    letters = ["_" for i in hidden_word]
    return letters


def user_input_level():
    difficulty = {1:"easy", 2:"hard"}
    while True:
        clear()
        level = input("""Select difficulty: 
        1:  easy
        2:  hard
         """)
        
        if level.isnumeric():
            level = int(level)
            if level in range(1, 3):
                break
            else:
                print("Select the correct level.")
                time.sleep(1.4)
    return difficulty_levels(difficulty[level])
            


def difficulty_levels(difficulty):
    
    if difficulty == "easy":
        hangman_pics = boards.easy
    else:
        hangman_pics = boards.hard
    
    return hangman_pics


def wrong_attempts(letter):
    if letter in wrong_guess:
        print(f"Letter {letter} was already used.")
    else:
        wrong_guess.append(letter)
        print(f"Letter {letter} isn't in hidden word.")
    time.sleep(2.4)


def user_input():
    user_letter = input("Enter a letter: ").strip().upper()
    checking_input(user_letter)


def checking_input(user_letter):
    if user_letter.isalpha() and len(user_letter) == 1:
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
    

def play_game():
    while len(hangman) > len(wrong_guess):
    
        if "_" in found_letters:
            clear()
            game_intro()
            
            print(f"WRONG GUESSES: {'-'.join(wrong_guess)} ", end='')
            print(hangman[len(wrong_guess)], end=' ')
            print(f"HIDDEN WORD: {''.join(found_letters)}")
            user_input()
        else:
            break

    clear()
    game_over()
            


def game_over():
    if "_" in found_letters:
        score = boards.lose
    else:
        score = boards.win
    
    for i in score:
        print(i)
        time.sleep(0.3)
    
    print(f"HIDDEN WORD --> {' '.join(hidden_word)}")
    exit()




if __name__ == "__main__":
    wrong_guess = []
    hidden_word = getting_hidden_word()
    found_letters = hiding_word(hidden_word)
    hangman = user_input_level()

    play_game()

   