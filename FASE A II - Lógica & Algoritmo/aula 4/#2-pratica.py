# Realize a sequência de print com for e while:
# A) inteiros de 3 até 12, com 12 incluso
init = 3
while init <= 12:
    print(init)
    init += 1

for i in range(3, 13, 1):
    print(i)

# B) inteiros de 0 até 9, exlcuindo o 9, com passo de 2
init = 0
while init < 9:
    print(init)
    init += 2

for i in range(0, 9, 2):
    print(i)

# Recriando exercício da aula 3
opcao = ''
while opcao != 'sair':
    print('Operações diponíveis:\n( + ) - Soma\n( - )Subtração\n( * ) - Multiplicação\n( / ) - Divisão\n"sair" - Encerra o programa')
    opcao = input('Escolha uma operação: ')
    if opcao == '+' or opcao == '-' or opcao == '*' or opcao == '/':
        num1 = float(input('Digite um valor: '))
        num2 = float(input('Digite outro valor: '))

    if opcao == 'sair':
        break
    elif opcao == '+':
        print('A soma de {} com {} é: {}\n'.format(num1, num2, num1 + num2))
    elif opcao == '-':
        print('A subtração de {} com {} é: {}\n'.format(num1, num2, num1 - num2))
    elif opcao == '*':
        print('A multiplicação de {} com {} é: {}\n'.format(num1, num2, num1 * num2))
    elif opcao == '/':
        print('A divisão de {} com {} é: {}\n'.format(num1, num2, num1 / num2))
    else:
        print('\nOperação inválida\n')
print('Encerrando...')

# Exercícios para saber quantas notas pagam x valor
valor = int(input('Digite o valor em R$: '))
while True:
    if valor >= 100:
        conta100 = valor // 100
        valor -= conta100 * 100
        print('Cédulas de 100: {}'.format(conta100))
        if not valor:
            break
    if valor >= 50:
        conta50 = valor // 50
        valor -= conta50 * 50
        print('Cédulas de 50: {}'.format(conta50)) 
        if not valor:
            break
    if valor >= 20:
        conta20 = valor // 20
        valor -= conta20 * 20
        print('Cédulas de 20: {}'.format(conta20))
        if not valor:
            break
    if valor >= 10:
        conta10 = valor // 10
        valor -= conta10 * 10
        print('Cédulas de 10: {}'.format(conta10)) 
        if not valor:
            break
    if valor >= 5:
        conta5 = valor // 5
        valor -= conta5 * 5
        print('Cédulas de 5: {}'.format(conta5))
        if not valor:
            break
    if valor:
        conta1 = valor
        print('Cédulas de 1: {}'.format(conta1)) 
        break

# Calcular quanto irá ser pago de acordo com a idade da pessoa
total = 0
dinheiro = 0

while True:
    idade = input('Qual sua idade? ')
    if idade == 'sair':
        break
    
    idade = int(idade)
    total += 1
    
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15

    dinheiro += ingresso
media = dinheiro / total
print('Total de pessoas: {}'.format(total))
print('Total arrecadado: {}'.format(dinheiro))
print('Média arrecadada: {}'.format(media))