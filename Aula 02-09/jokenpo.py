#Jogo jokenpo em Python

import random

def jokenpo():
    opcoes = ['pedra', 'papel', 'tesoura']
    vitorias=0
    derrotas=0
    empates=0
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
            empates+=1
            print('Empate!')
        elif jogador.lower() == 'pedra' and computador == 'tesoura':
            vitorias+=1
            print('Você ganhou!')
        elif jogador.lower() == 'papel' and computador == 'pedra':
            vitorias+=1
            print('Você ganhou!')
        elif jogador.lower() == 'tesoura' and computador == 'papel':
            vitorias+=1
            print('Você ganhou!')
        else:
            derrotas+=1
            print('Você perdeu!')

    print(f'Você ganhou {vitorias} vezes, perdeu {derrotas} vezes e empatou {empates} vezes.')

jokenpo()