## Expressões Boleanas
# a) Somatorio de 2 com 2 é menor que 4
print(2 + 2 < 4)

# b) O valor 7 // 3 é igual a 1 + 1
print(7 // 3 == 1 + 1)

# c) a soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25
print((3 ** 2) + (4 ** 2) == 25)

# d) A soma de 2, 4 e 6 é maior que 12
print((2 + 4 + 6) > 12)

# e) 1387 é divisivel por 19
print(1387 % 19 == 0)

# f) 31 é par
print(31 % 2 == 0)

# g) O menor valor entre 34, 29 e 31 é menor que 30
print(min(34, 29, 31) < 30)

## Condicionais simples
# a) SE idade é maior que 60, escreva: 'você tem direitos aos benefícios'
idade = 61
if idade > 60:
    print('Você tem direitos aos benefícios')

# b) Se dano é maior que 10 e escudo é igual a 0, escreva: 'Você está morto!'
dano = 11
escudo = 0
if dano > 10 and escudo == 0:
    print('Você está morto!')

# c) SE pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em True, escreva: 'Você escapou!'
norte = False
sul = False
leste = False
oeste = True
if norte or sul or leste or oeste:
    print('Você escapou!')

## Condicional Composta
# a) SE ano é divisível por 4, escreva: 'Pode ser um ano bissexto'. Caso contrário, escreva: 'Definitivamente não é um ano bissexto.'
ano = 2024
if ano % 4 == 0:
    print('Pode ser um ano bissexto.')
else:
    print('Definitivamente não é um ano bissexto.')

# b) Se ambas as variáveis booleanas cima e baixo forem True, escreva: 'Decida-se!', caso contrário, escreva: 'Você escolheu um caminho!'
cima = True
baixo = False
if cima and baixo:
    print('Decida-se!')
else:
    print('Você escolheu um caminho!')