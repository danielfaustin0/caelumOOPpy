"""Jogo da Forca
 
 O jogo consiste em pedir que o usuário descubra a palavra escondida.
 Para isso, o usuário deverá dar palpites sobre as letras que ele
  acredita que existem na palavra.

 
 Feb 19 2021 - Daniel Faustino
"""

hidden_word = 'abelha'
discovered_letters = ['_', '_', '_', '_', '_', '_']

for i in range(1, len(hidden_word)):
    letter_position = 0
    print(discovered_letters)
    letter_input = input('Informe uma letra: ')

    if letter_input in hidden_word:
        for letter in hidden_word:
            if letter == letter_input:
                discovered_letters[letter_position] = letter_input
            else:
                pass
            letter_position += 1
    else:
        print('A letra não está na palavra escondida.')


