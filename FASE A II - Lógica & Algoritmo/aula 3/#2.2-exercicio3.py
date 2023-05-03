# Calcule o preço a pagar pelo fornecimento de energia elétrica 
# Solicitar a quantidade de kWh consumido
# Solicitar o tipo de instalação: R = residêncial, I = indústrias, C = Comercios
# Tarifas:
    # Residencial: até 500 kWh = R$0,40 // Acima de 500 = R$0,65
    # Comercial: até 100 kWh = R$0,55 // Acima de 1000 = R$0,60
    # Industrial: até 5000 kWh = R$0,55 // Acima de 5000 = R$0,60

print('Tipos de instalação:\n(r) - Residêncial\n(c) - Comercial\n(i) - Industrial')
tipo = input('Digite a letra da sua instalação: ')

kWh = float(input('Digite quantos kWh foram consumidos: '))

if kWh > 0:
    if tipo == 'r':
        if kWh <= 500:
            print('Valor a pagar: R${}'.format(kWh * 0.40))
        else:
            print('Valor a pagar: R${}'.format(kWh * 0.65))
    elif tipo == 'c':
        if kWh <= 1000:
            print('Valor a pagar: R${}'.format(kWh * 0.55))
        else:
            print('Valor a pagar: R${}'.format(kWh * 0.60))
    elif tipo == 'i':
        if kWh <= 5000:
            print('Valor a pagar: R${}'.format(kWh * 0.55))
        else:
            print('Valor a pagar: R${}'.format(kWh * 0.60))
    else: 
        print('Tipo inválido')
else:
    print('Não há como calcular se kWh = 0')
