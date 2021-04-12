""" Menu de Acesso ao Jogos
 
 Por este script o usuário poderá escolher qual jogo ele quer iniciar

 Feb 23 2021 - Daniel Faustino

"""

import os
import gallows_game as gallows
import guessing_game as guessing


def clear():
    os.system('clear')

leaving_game = False

# while not leaving_game:

def menu_intro():
    print("""
    =-=-=-==-=-=-==-=-=-==-=-=-==-=-=-=
    =-=-=-=-=-= Pick a Game =-=-=-=-=-=
        Guessing Game   1
        Gallows Game    2

    =-=-=-==-=-=-==-=-=-==-=-=-==-=-=-=
    Enter 'q' to quit.
    """)

    # return intro


def pick_game():
    picked_game = input()
    game_menu(picked_game)
    
    
def game_menu(game):
    if game.isnumeric():
        picked_game = int(game)

        if picked_game == 1:
            guessing.play_game()

        elif picked_game == 2:
            __name__ == "__main__"
            gallows.play_game()
        else:
            pass            
    else:
        if game.isalpha():
            if game == 'q':
                print('Saindo do jogo.')
                exit()
            else:
                menu_intro()
                pick_game()

if __name__ == "__main__":
    clear()
    menu_intro()
    pick_game()