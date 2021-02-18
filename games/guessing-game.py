"""Jogo de adivinhação

 O usuário deve descobrir o número secreto.
 O programa continua sendo executado até que o usuário acerte o número.
 Quando o número for encontrado, será mostrado o total de tentativas.

 O usuário pode escolher entre três níveis de dificuldade
 Em cada nível aumenta a escala de números e diminui as tentativas.

 Feb 15 2021 - Daniel Faustino
"""

# TODO: DONE generate random numbers
# TODO: DONE create difficulty levels
# TODO: DONE Create a system points
# TODO: DONE Stop game running
# TODO: DONE Verify user's input
# TODO: Clear the game screen

import random
import os


failure = 0  # count how many times missed the number
number_limit = 0
error_message = ''
win = False

# Difficulty levels
while number_limit == 0:
    level = input("""Selecione a dificuldade:
    Nível (1) | Nível (2) | Nível (3)
    Aperte 'enter' para sair.\tNível: """)

    if level == '':
        print('Saindo do programa.')
        break
    if level.isnumeric():
        level = int(level)
        if level == 1:
            number_limit = 30
            failure = 10
        elif level == 2:
            number_limit = 45
            failure = 9
        elif level == 3:
            number_limit = 60
            failure = 5
        else:
            print("Escolha a dificuldade correta.")
        
        # generate random numbers
        secret_number = random.randint(1, number_limit) 
        # points system
        points = number_limit * 10
        score = int(points / failure)
    else:
        print('Você deve escolher entre os níveis 1, 2 ou 3')

# Runnung the game
while failure != 0:
    print(error_message)
    print(f'Points: {points}')
    print(f'{failure} tentativas.\nNúmeros entre 01 e {number_limit}')
    attempt = input("Digite o seu palpite: ")

    if attempt == '':
        break

    if attempt.isnumeric():
        attempt = int(attempt)
        if attempt == secret_number:
            win = True
            break
        else:
            if attempt < secret_number:
                error_message = '\nO número secreto é maior do que seu palpite.'
            else:
                error_message = '\nO número secreto é menor do que seu palpite.'
            failure -= 1
            points -= score
        msg = f'\nPontuação final: {points}'

if not win:
    print('Programa encerrado.')
if win:
    print(f'você acertou.{msg}')
else:
    print(f'Você não tem mais tentativas.{msg}')
