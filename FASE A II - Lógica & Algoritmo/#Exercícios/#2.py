ru_identificador = 000000

print('Seja Bem Vindo a Lanchonete do Gerson Lucas Silva Leite!\n') # \n usado para pular linha apenas. Usado em Strings.

print('---------------Cardápio---------------')
print('Código |       Descrição       | Valor(R$)')
print(' 100   |    Cachorro Quente    |    9,40  ')
print(' 101   | Cachorro Quente Duplo |   11,00  ')
print(' 102   |         X-Egg         |   12,00  ')
print(' 103   |       X-Salada        |   12,00  ')
print(' 104   |        X-Bacon        |   14,00  ')
print(' 105   |        X-Tudo         |   17,00  ')
print(' 200   |   Refrigerante Lata   |    5,00  ')
print(' 201   |      Chá Gelado       |    4,00  ')
# Cardápio para o Usuário

total = 0
while True:
    codigo = input('Digite o código do produto que deseja: ')
    if codigo == '100':
        prod = 'Cachorro Quente'
        preco = 9.40
    elif codigo == '101':
        prod = 'Cachorro Quente Duplo'
        preco = 11
    elif codigo == '102':
        prod = 'X-Egg'
        preco = 12
    elif codigo == '103':
        prod = 'X-Salada'
        preco = 12
    elif codigo == '104':
        prod = 'X-Bacon'
        preco = 14
    elif codigo == '105':
        prod = 'X-Tudo'
        preco = 17
    elif codigo == '200':
        prod = 'Refrigerante Lata'
        preco = 5
    elif codigo == '201':
        prod = 'Chá Gelado'
        preco = 4
    elif codigo == 'sair':
        break
    else:
        print('Código Inválido')
        continue
    # Estrutura que verifica o código escolhido pelo usuário, caso esteja no cardápio, dá o devido valor e nome do produto para suas variáveis (prod e preco)
    # Caso o usuário digite 'sair', o programa encerra, e caso ele digite outra coisa que não esteja no intervalo, ele solicita novamente.

    total += preco
    print('Você pediu {}, valor R$ {}'.format(prod, preco))
    # Imprime o Produto escolhido e o Preço do mesmo

    maisCoisas = input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - Não\n>> ')
    if maisCoisas == '1':
        continue
    elif maisCoisas == '0':
        break
    else:
        print('Operação Inválida, reiniciando programa.')
        continue
    # Estrutura que verifica se o usuário deseja mais algo, foi usado '\n' para quebrar as linhas, evitando usar vários print()

print('Total a ser pago: R$ {:.2f}'.format(total))
# No final do programa, é informado o total a ser pago dos produtos escolhidos.