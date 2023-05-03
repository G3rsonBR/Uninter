# Ler dois valores numéricos e perguntar qual operação deseja realizar (as 4 básicas). Exibir o resultado

print('Operações diponíveis:\n( + ) - Soma\n( - )Subtração\n( * ) - Multiplicação\n( / ) - Divisão')
opcao = input('Escolha uma operação: ')
if opcao == '+' or opcao == '-' or opcao == '*' or opcao == '/':
    num1 = float(input('Digite um valor: '))
    num2 = float(input('Digite outro valor: '))

if opcao == '+':
    print('A soma de {} com {} é: {}'.format(num1, num2, num1 + num2))
elif opcao == '-':
    print('A subtração de {} com {} é: {}'.format(num1, num2, num1 - num2))
elif opcao == '*':
    print('A multiplicação de {} com {} é: {}'.format(num1, num2, num1 * num2))
elif opcao == '/':
    print('A divisão de {} com {} é: {}'.format(num1, num2, num1 / num2))
else:
    print('Operação inválida')