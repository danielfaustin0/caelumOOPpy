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
# TODO: Create a system points
# TODO: Stop game running
# TODO: Verify user's input
# TODO: Clear the game screen

import random
import os


failure = 0  # count how many times missed the number
number_limit = 0
error_message = ''
win = False

# Difficulty levels
while number_limit == 0:
    level = int(input("""Selecione a dificuldade:
    \nNível 1 \tNível 2 \tNível 3 \n\tNível:"""))

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
secret_number = random.randint(1, number_limit) # generate random numbers
points = number_limit * 10
score = int(points / failure)
# Runnung the game
while failure > 0:
    print(error_message)
    print(f'Points: {points}')
    print(f'{failure} tentativas.\nNúmeros entre 01 e {number_limit}')
    attempt = int(input("Digite o seu palpite: "))

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

# points system
msg = f'\nPontuação final: {points}'
if win:
    print(f'você acertou.{msg}')
else:
    print(f'Você não tem mais tentativas.{msg}')
