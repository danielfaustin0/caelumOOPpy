"""Jogo de adivinhação

O usuário deve descobrir o número secreto.

    Feb 15 2021 - Daniel Faustino
"""

# TODO: define a constant to be the hidden number
secret_number = 40

attempt = int(input("Digite o seu palpite: "))

if attempt == secret_number:
    print('Você acertou.')
else:
    print('Você errou.')