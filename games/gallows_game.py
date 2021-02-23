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

import os

def clear():
    os.system('clear')


def play_game():

    hidden_word = 'abelha'
    discovered_letters = list()
    wrong_guess = list()

    for letter in hidden_word:
        discovered_letters.append('_')
    clear()
    while '_' in discovered_letters:
        letter_position = 0
        print('respostas erradas: ',', '.join(wrong_guess))
        print('Palavra oculta: ', ' '.join(discovered_letters))
        letter_input = input('Informe uma letra: ')
        clear()
        if letter_input in hidden_word:
            for letter in hidden_word:
                if letter == letter_input:
                    discovered_letters[letter_position] = letter_input.upper()
                else:
                    pass
                letter_position += 1
        else:
            if letter_input not in wrong_guess:
                wrong_guess.append(letter_input)
                print('A letra não está na palavra escondida.')
            else:
                print('Essa letra já foi digitada antes.')
        

    if '_' not in discovered_letters:
        print(f'Palavra escondida: {hidden_word.upper()}')

# play_game()