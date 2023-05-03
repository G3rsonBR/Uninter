# Exercícios práticos da apostila:

# Desenvolver um algoritmo, o usuário irá passar o valor de um produto e o percentual de desconto
# Calcular e exibir o valor do produto

valor = float(input('Informe o valor do produto: '))
percentual = float(input('Informe o percentual a ser descontado (0 ~ 100): '))
desconto = valor * (percentual / 100)
print('O valor do produto com desconto é: {}'.format(valor - desconto))
