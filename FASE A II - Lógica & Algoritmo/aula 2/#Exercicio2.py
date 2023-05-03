# Exercícios práticos da apostila:

# Pergunte a quantidade de km percorridos por um carro alugado pelo user, e a qauntidade de dias alugado
# Calcular o preço a pagar, sabendo que o carro custa R$ 60 p/ dia e R$ 0.15 p/ km rodado
kms = float(input('Informe quantos KMs foram rodados: '))
dias = int(input('Informe quantos dias ficou com o carro alugado: '))
total = dias * 60 + kms * 0.15

print('Vocẽ rodou {}KMs. Usou o carro por {} dias. O valor a se pagar é de R${}.'.format(kms, dias, total))