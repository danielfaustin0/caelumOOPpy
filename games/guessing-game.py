"""Jogo de adivinhação

O usuário deve descobrir o número secreto.
O programa continua sendo executado até que o usuário acerte o número.

    Feb 15 2021 - Daniel Faustino
"""
import random
import os

# TODO: generate random numbers
secret_number = random.randint(1, 50) # generate random numbers

while True:    
    attempt = int(input("Digite o seu palpite: "))

    if attempt == secret_number:
        print('Você acertou.')
        break
    else:
        print('Você errou.')
        if attempt < secret_number:
            print('O número secreto é maior do que seu palpite.')
        else:
            print('O número secreto menor do que seu palpite.')
            