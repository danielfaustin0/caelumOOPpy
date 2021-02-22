"""Jogo da Forca
 
 O jogo consiste em pedir que o usuário descubra a palavra escondida.
 Para isso, o usuário deverá dar palpites sobre as letras que ele
  acredita que existem na palavra.

 
 Feb 19 2021 - Daniel Faustino
"""

# TODO DONE: Creat a list to recieve the right guess
# TODO: Show the wrong guess
# TODO: Beautify the output from discovered_letters
# TODO: Clear the game screen

hidden_word = 'abelha'
discovered_letters = list()

for letter in hidden_word:
    discovered_letters.append('_')

while '_' in discovered_letters:
    letter_position = 0
    print(' '.join(discovered_letters))
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

if '_' not in discovered_letters:
    print(f'Palavra escondida: {hidden_word.upper()}')

