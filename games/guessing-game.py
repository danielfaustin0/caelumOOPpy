"""Jogo de adivinhação

O usuário deve descobrir o número secreto.
O programa continua sendo executado até que o usuário acerte o número.

    Feb 15 2021 - Daniel Faustino
"""

# TODO: keep the script running until answer right
# TODO: Show hints about the guess is below or above the secret number
secret_number = 40

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
            