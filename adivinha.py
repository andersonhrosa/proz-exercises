#crie um protótipo de um jogo de adivinhação de números.
# Ele deve pedir ao jogador um número inteiro entre 0 e 100 e, 
# se a entrada fornecida for válida, informar se o chute acertou o alvo

import random

def adivinha():
    numero = random.randint(0, 100)
    chances = 5
    while chances > 0:
        try:
            chute = input('Digite um número entre 0 e 100 (ou "q" para sair): ')
            if chute.lower() == 'q':
                print('Saindo do jogo...')
                break
            chute = int(chute)
            if chute == numero:
                print('Você acertou!')
                break
            elif chute < numero:
                print('Você errou! O número alvo é maior.')
            else:
                print('Você errou! O número alvo é menor.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número válido ou "q" para sair.')
        chances -= 1

adivinha() 