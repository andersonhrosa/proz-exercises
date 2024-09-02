#Jogo jokenpo em Python

import random

def jokenpo():
    opcoes = ['pedra', 'papel', 'tesoura']
    while True:
        jogador = input('Escolha pedra, papel ou tesoura (ou "q" para sair): ')
        if jogador.lower() == 'q':
            print('Saindo do jogo...')
            break
        elif jogador.lower() not in opcoes:
            print('Escolha inválida. Por favor, escolha pedra, papel ou tesoura.')
            continue
        computador = random.choice(opcoes)
        print(f'O computador escolheu {computador}.')
        if jogador.lower() == computador:
            print('Empate!')
        elif jogador.lower() == 'pedra' and computador == 'tesoura':
            print('Você ganhou!')
        elif jogador.lower() == 'papel' and computador == 'pedra':
            print('Você ganhou!')
        elif jogador.lower() == 'tesoura' and computador == 'papel':
            print('Você ganhou!')
        else:
            print('Você perdeu!')

jokenpo()