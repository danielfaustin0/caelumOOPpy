"""Jogo de adivinhação

O usuário deve descobrir o número secreto.
O programa continua sendo executado até que o usuário acerte o número.
Quando o número for encontrado, será mostrado o total de tentativas.

    Feb 15 2021 - Daniel Faustino
"""

# TODO: generate random numbers
# TODO: create difficulty levels
# TODO: Create punctuation system
# TODO: Stop game running
# TODO: Verify user's input
# TODO: Clear the game screen
import random
import os


secret_number = random.randint(1, 50) # generate random numbers

failure = 0  # count how many times missed the number
while True:
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
        failure += 1