""" Jokenpô, opçẽos de 1 a 3, validar se é número, se digitar 0 encerrar o programa"""
import random as rand

def valida_int(pergunta):
    try:
        x = int(input(pergunta))
        return x
    except ValueError:
        return

print('JOKENPÔ\n1 - Pedra\n2 - Papel\n3 - Tesoura')


while True:
    aleatorio = rand.randrange(1, 4)
    entrada = valida_int('Escolha uma opção: ')
    if entrada == 1:
        if aleatorio == 3:
            print('Parabéns, você ganhou!')
            break
        elif aleatorio == 1:
            print('Empate! De novo...')
            continue
        else:
            print('Putz, você perdeu :l\nTenta de novo...')
            continue
    elif entrada == 2:
        if aleatorio == 1:
            print('Parabéns, você ganhou!')
            break
        elif aleatorio == 2:
            print('Empate! De novo...')
            continue
        else:
            print('Putz, você perdeu :l\nTenta de novo...')
            continue
    elif entrada == 3:
        if aleatorio == 2:
            print('Parabéns, você ganhou!')
            break
        elif aleatorio == 3:
            print('Empate! De novo...')
            continue
        else:
            print('Putz, você perdeu :l\nTenta de novo...')
            continue
    elif entrada == 0:
        break
    else:
        print('Opção Inválida, tente novamente.')
        continue
print('Encerrando...')