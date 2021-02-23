""" Menu de Acesso ao Jogos
 
 Por este script o usuário poderá escolher qual jogo ele quer iniciar

 Feb 23 2021 - Daniel Faustino

"""

import os
import gallows_game
import guessing_game


def clear():
    os.system('clear')

leaving_game = False

while not leaving_game:
    print('Escolha um jogo:')
    print('Jogo de adivinhação (1)')
    print('Jogo da Forca (2)')
    print('Aperte "q" para sair.')

    game = input()
    clear()

    if game.isnumeric():
        chosen_game = int(game)

        if chosen_game == 1:

            print('Bem vindo ao Jogo de Adivinhação.')
            guessing_game.play_game()
        elif chosen_game == 2:
            print('Bem vindo ao Jogo Da Forca.')
            gallows_game.play_game()
        else:
            print('Opção Inválida.')
    else:
        if game.isalpha():
            if game == 'q':
                print('Saindo do jogo.')
                leaving_game = True
            else:
                print('Opção inválida.')