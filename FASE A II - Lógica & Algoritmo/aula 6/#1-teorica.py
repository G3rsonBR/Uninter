# Estruturas de dados
    # Tuplas: ()
    # Listas: []
    # Dicionário: {}
# Veremos também:
    # Conceitos de métodos
    # Métodos para String

# Tuplas:
# Estática, Imutável, Representada por '()'
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)
print(mochila[0]) # print elemento 1, indice = 0
print(mochila[2]) # print elemento 3, indice = 2
print(mochila[0:2]) # print dos elementos 1 e 2
print(mochila[2:]) # Print dos elementos a partir do indice = 2
print(mochila[-1]) # Ultimo indice

# mochila[2] = 'ovos'
# print(mochila)
# Erro, tupla não recebe uma atribuição, ela é imutável! 

for item in mochila:
    print('Item na mochila: {}'.format(item))

tam = len(mochila)
for i in range(0, tam):
    print('Item na mochila: {}'.format(mochila[i]))
# Alternativa do primeiro for

upgrade = ('Quejo', 'Canivete')
mochila_upgrade = mochila + upgrade
mochila_upgrade_invertido = upgrade + mochila
print(mochila_upgrade)
print(mochila_upgrade_invertido)
# Forma de add valoers a uma tupla, mas aqui você coloca em outra variável


# Desempacotamento de parâmetros em funções
def soma(*num):
    soma = 0
    print('\nTupla: {}'.format(num))
    for i in num:
        soma += i
    return soma
print('Resultado: {}'.format(soma(1,2)))
print('Resultado: {}'.format(soma(1,2,3,4,5,6,7,8,9)))


# Listas -> Dinâmica, index = nums inteiros, representadas por []
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila)

mochila[2] = 'Laranja'
print(mochila)

# Manipulando Listas
mochila.append('Ovos')
print(mochila) # Adicionar no último indice

mochila.insert(1, 'Canivete')
print(mochila) # Adicionar em um indeice específico

del mochila[1]
print(mochila)
mochila.remove('Ovos')
print(mochila)
# Removem valores, desde para um index específico, até por 'conteúdo'

# Referencia igual
x = [5, 7, 9, 11]
y = x
print(x)
print(y)

y[0] = 2
print(x)
print(y)
# Mudou nas duas, pois 'y = x' referencia a variável, ou seja y não tem um valor igual de x, ela tem a mesma referencia de memoria na alocação

y = x[:] # Cria uma cópia da variável x
y[0] = 9
print(x)
print(y)

# Métodos 
# Lista é um objeto de uma classe dentro de Python
# POO - Programação Orientada a Objetos
# mochila.append('ovos') => variavel.função(parâmetro)


# Strings e listas dentro de outras
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']

# Dupla indexação
# primeiro indice = referente ao item da lista
# o segundo = referente ao caractere da string
# podemos acessar os itens e o indices dos caracteres da string

print(mochila[0]) # Mochila
print(mochila[0][0]) # Indice 0, caractere 0
print(mochila[2][1])

for item in mochila:
    for letra in item:
        print(letra, end='')
    print()

for i in range(0, len(mochila)):
    for j in range(0, len(mochila[i])):
        print(mochila[i][j], end='')
    print()

# Lista dentro de outra
carrinho = [['Cebola', 0.39], ['Tomate', 0.49], ['Maça', 0.89]]
print(carrinho)
print(carrinho[0])
print(carrinho[0][0])
print(carrinho[2][1])

# Exercício
item = []
mercado = []

for i in range(3):
    item.append(input('Digite o nome do Item: '))
    item.append(int(input('Digite a quantidade: ')))
    item.append(float(input('Digite o valor: ')))
    mercado.append(item[:])
    item.clear()
print(mercado)

for i in range(3):
    nome = input('Digite o nome do Item: ')
    quantidade = int(input('Digite a quantidade: '))
    valor = float(input('Digite o valor: '))
    mercado.append([nome, quantidade, valor])
print(mercado)

soma = 0
print('Lista de compras: ')
print('-' * 20)
print('Item | Quantidade | Valor Unitário | Total do Item')
for item in mercado:
    print('{} | {} | {} | {}'.format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[1]
print('-' * 20)
print('Total a pagar: {}'.format(soma))

# Dicionários -> Dinâmico, indexado e representaod por {} 
game = {
    'nome': 'Super Mário',
    'dev': 'Nintendo',
    'ano': 1990 
}
print(game)
print(game['nome'])
print(game['dev'])
print(game['ano'])

# Métodos -> Values, Keys, Items

print(game.values())
for i in game.values():
    print(i)

print(game.keys())
for i in game.keys():
    print(i)

print(game.items())
for i, j in game.items():
    print('{} = {}'.format(i, j))

games = []
game1 = {
    'nome': 'Super Mário',
    'console': 'Super Nintendo',
    'ano': 1990 
}

game2 = {
    'nome': 'Zelda Ocarina of Time',
    'console': 'Nintendo 64',
    'ano': 1998
}

game3 = {
    'nome': 'Pokemon Yellow',
    'console': 'Game Boy',
    'ano': 1999 
}

games = [game1, game2, game3]
print(games)

game = {}
games = []
for i in range(3):
    game['nome'] = input('Digite o nome do jogo: ')
    game['plataforma'] = input('Digite a plataforma que ele foi lançado: ')
    game['ano'] = input('Digite o ano que ele foi lançado: ')
    games.append(game.copy())
print('-' * 20)
for e in games:
    for i,j in e.items():
        print('O Campo {} tem o valor {}'.format(i, j))

games = {
    'nome': ['Mario', 'Zelda', 'Pokemon'],
    'videogame': ['SNintendo', 'N64', 'Game Boy'],
    'ano': [1990, 1998, 1999]
}
print(games)

games = {
    'nome': [],
    'videogame': [],
    'ano': [],
}

for i in range(3):
    nome = input('Digite o nome do jogo: ')
    videogame = input('Digite o videogame do jogo: ')
    ano = input('Digite o ano do jogo: ')
    games['nome'].append(nome)
    games['videogame'].append(videogame)
    games['ano'].append(ano)
print('-' * 20)
print(games)

# Métodos com Strings
# Strings são IMUTÁVEIS, mas como listas podemos alterar ela
s1 = 'Algoritmo'
print(s1)
# s1[0] = 'a' # -> Erro
s1 = list('Algoritmo')
print(s1)
print(''.join(s1))

s1[0] = 'a'
print(''.join(s1))

# Verificar caracteres
s1 = 'Lógica de Programação e Algoritmo'
print(s1.startswith('Lógica'))
print(s1.startswith('Programação'))

print(s1.endswith('Algoritmo'))
print(s1.endswith('algoritmo'))

print(s1.lower().endswith('algoritmo'))
print(s1.upper())
print(s1.lower())

print(s1.count('a'))
print(s1.lower().count('a'))

s1 = 'Um Mafagafinho, dois Mafagafinhos, três Mafagafinhos...'
print(s1.lower().count('mafagafinho'))
print(s1.split(' ,'))
print(s1.replace('Mafagafinho', 'Gatinho'))
print(s1.replace('Mafagafinho', 'Gatinho', 1))

s1 = 'Lógica de Programação e Algoritmo'
s2 = '42'
s3 = 'oi'
print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum()) # True para números e letras (sem espaços!), acentos são aceitos

print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha()) # Somente letras, acentos são aceitos

