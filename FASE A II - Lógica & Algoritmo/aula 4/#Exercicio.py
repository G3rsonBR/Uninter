#Exercício 2 da att prática
acumulador = 0
continuar = 's'
print('Bem-vindo a pizzaria.')
print('---------------Cardápio---------------')
print('CÓDIGO | DESCRIÇÃO | PIZZA MÉDIA (M) | PIZZA GRANDE (G) |')
print('    21 | Napolitana|        R$ 20,00 |         R$ 26,00 |')
print('    22 | Margherita|        R$ 20,00 |         R$ 26,00 |')
print('    23 | Calabresa |        R$ 25,00 |         R$ 32,50 |')
print('    24 | Toscana   |        R$ 30,00 |         R$ 39,00 |')
print('    25 | Portuguesa|        R$ 30,00 |         R$ 39,00 |')
print('------------------------------')
while continuar == 's':
    tamanho = input('Entre com o tamanho da pizza desejado (M/G): ')
    if tamanho != 'M' and tamanho != 'm' and tamanho != 'G' and tamanho != 'g':
        print('Opção Inválida, digite um tamanho válido.')
        continue
    codigo = int(input('Entre com o código da pizza desejado (21 ~ 25): '))
    if codigo < 21 or codigo > 25:
        print('Opção Inválida, digite um código válido válido.')
        continue

    if codigo == 21:
        if tamanho == 'm' or tamanho == 'M':
            print('Escolheu a pizza Napolitana, tamanho M')
            acumulador += 20.00
        if tamanho == 'g' or tamanho == 'G':
            print('Escolheu a pizza Napolitana, tamanho G')
            acumulador += 26.00
    if codigo == 22:
        if tamanho == 'm' or tamanho == 'M':
            print('Escolheu a pizza Margherita, tamanho M')
            acumulador += 20.00
        if tamanho == 'g' or tamanho == 'G':
            print('Escolheu a pizza Margherita, tamanho G')
            acumulador += 26.00
    if codigo == 23:
        if tamanho == 'm' or tamanho == 'M':
            print('Escolheu a pizza Calabresa, tamanho M')
            acumulador += 25.00
        if tamanho == 'g' or tamanho == 'G':
            print('Escolheu a pizza Calabresa, tamanho G')
            acumulador += 32.50
    if codigo == 24:
        if tamanho == 'm' or tamanho == 'M':
            print('Escolheu a pizza Toscana, tamanho M')
            acumulador += 30.00
        if tamanho == 'g' or tamanho == 'G':
            print('Escolheu a pizza Toscana, tamanho G')
            acumulador += 39.00
    if codigo == 25:
        if tamanho == 'm' or tamanho == 'M':
            print('Escolheu a pizza Portuguesa, tamanho M')
            acumulador += 30.00
        if tamanho == 'g' or tamanho == 'G':
            print('Escolheu a pizza Portuguesa, tamanho G')
            acumulador += 39.00
    
    print('Valor a pagar: R$ {}\n'.format(acumulador))
    continuar = input('Deseja comprar mais? "s" para Sim e "n" para Não: ')
    
print('Valor Total: R$ {}'.format(acumulador))