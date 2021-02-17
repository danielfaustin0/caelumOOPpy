"""Jogo de adivinhação

O usuário deve descobrir o número secreto.
O programa continua sendo executado até que o usuário acerte o número.
Quando o número for encontrado, será mostrado o total de tentativas.

O usuário pode escolher entre três níveis de dificuldade
Em cada nível aumenta a escala de números e diminui as tentativas.

    Feb 15 2021 - Daniel Faustino
"""

# TODO: DONE generate random numbers
# TODO: create difficulty levels
# TODO: Create punctuation system
# TODO: Stop game running
# TODO: Verify user's input
# TODO: Clear the game screen

import random
import os


failure = 0  # count how many times missed the number
number_limit = 0

while number_limit == 0:
    level = int(input("""Selecione a dificuldade:
    \nNível 1 \nNível 2 \nNível 3 \n:"""))

    if level == 1:
        print('Você tem 10 tentativas.\nNúmeros entre 01 e 30.')
        number_limit = 30
        failure = 10
    elif level == 2:
        print('Você tem 05 tentativas.\nNúmeros entre 01 e 45.')
        number_limit = 45
        failure = 9
    elif level == 3:
        print('Você tem 03 tentativas.\nNúmeros entre 01 e 60')
        number_limit = 60
        failure = 5
    else:
        print("Escolha a dificuldade correta.")


secret_number = random.randint(1, number_limit) # generate random numbers

while failure > 0:
    attempt = int(input("Digite o seu palpite: "))

    if attempt == secret_number:
        print('Você acertou.')
        print(f'Erros: {failure}')
        break
    else:
        print('Você errou.')
        if attempt < secret_number:
            print('O número secreto é maior do que seu palpite.')
        else:
            print('O número secreto menor do que seu palpite.')
        failure -= 1