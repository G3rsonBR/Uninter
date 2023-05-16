# Estruturas de repetição => Servem para facilitar instruções que se repetem várias vezes
# Vamos supor que precisamos fazer nosso personagem mover, escrever "moveu" 5 vezes, é de boa...
# Mas e quando for 100x? 1000x? Na mão é difícil fazer isso.

# Laço While => Faça enquanto... 
# Em resumo, ele irá executar um número de vezes ENQUANTO for verdadeiro a condição
x = 1
while(x <= 5):
    print(x)
    x += 1

# Exercício do contador
inicial = int(input('Digite o inicio do intervalo: '))
final = int(input('Digite o final do intervalo: '))
x = inicial
while(x <= final):
    if(x % 2 == 0):
        print(x)
    x += 1

# Exercício Acumulador
soma = 0
cont = 1
while(cont <= 5):
    x = float(input('Digite a {}ª nota: '.format(cont)))
    soma += x
    cont += 1
media = soma / 5
print('Média Final: {}'.format(media))

# Um pouco mais avançado agora...
# Validando dados de entrada

x = int(input('Digite um valor maior do que zero: '))
while (x <= 0):
    x = int(input('Digite um valor maior do que zero: '))
print('Você digitou {}. Encerrando o programa...'.format(x))

# Instrução Break
print('Digite uma mensagem que irei repetir para você!')
print('Digite "sair" para encerrar.')
while True:
    texto = input('')
    print(texto)
    if(texto == 'sair'):
        break
print('Encerrando o Programa...')

# Instrução Continue
while True:
    nome = input('Qual o seu nome? ')
    if(nome != 'Gerson'):
        continue
    senha = input('Qual sua senha? ')
    if(senha == '1234'):
        break
print('Acesso Concedido.')

# Valoers Truthy e Falsey => Valores não booleans que podem ser tratados como boolean
nome = '' # Falsey, pois não há um valor atribuido diretamente, mas o programa lê como False
while not nome: # While True! Pois é a negação de um False
    nome = input('Digite seu nome: ')
valor = int(input('Digite um número qualquer: '))
if valor:
    print('Você digitou um valor diferente de 0')
else:
    print('Digitou 0')

# For => Igual o While, roda enquanto a condição for True, porém o numero de execuções é finito e bem definido
for i in range(6):
    print(i)

for i in range(1, 6, 1):
    print(i)

for i in range(1, 6, 2):
    print(i)

for i in range(10, 0, -2):
    print(i)

# Exercício media pares
soma = 0
quantidade = 0
for i in range(1, 101):
    if(i % 2 == 0):
        soma += i
        quantidade += 1
media = soma / quantidade
print('A média dos pares de 1 até 100 é: {}'.format(media))

# Exercício tabuada com laços de repetição aninhados 
inicial = 1
while inicial <= 10:
    mult = 1
    while mult <= 10:
        print('{} x {} = {}'.format(inicial, mult, inicial * mult))
        mult += 1
    inicial += 1
    print('')

for i in range(1, 11, 1):
    for x in range(1, 11, 1):
        print('{} x {} = {}'.format(i, x, i * x))
    print('')

for i in range(1, 11, 1):
    mult = 1
    while mult <= 10:
        print('{} x {} = {}'.format(i, mult, i * mult))
        mult += 1
    print('')
