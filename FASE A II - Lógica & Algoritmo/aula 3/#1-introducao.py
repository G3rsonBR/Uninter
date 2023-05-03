# Aulas voltadas a estrutura de condição
# Condicionais simples e compostas 

# Simples -> se Verdadeiro, segue as instruções, se falso, pula e não executa as intruções 
# Exercicio: Ler dois valores int, comparar se o primeiro é maior que o segundo, se for, imprimir o mesmo informando que é maior que o segundo
first = int(input('Digite o primeiro valor inteiro: '))
second = int(input('Digite o segundo valor inteiro: '))

if(first > second):
    print('{} é maior que {}'.format(first, second))

# Composta -> Se Verdadeiro, faça algo, se Falso faça outra
# Exercício: ler um valor e verificar se ele é par ou impar
num = int(input('Digite um valor inteiro: '))

if(num % 2 == 0):
    print('É par')
else:
    print('É impar')

# Operadores lógicos/booleanos
x = True
y = False
print(not x) # Retorna o contrário, no caso, False
print(not y) # Retorna o contrário, no caso, True
print(x and y)
print(x or y)


# Expressões Lógicas/Booleanas
x = 10
y = 1
res = not x > y #Primeiro a verificação, que é true, e depois ele nela, por isso dá False
print(res)


x = 10
y = 1
z = 5.5
res = x > y and z == y # Primeiro os operadores relacionais, depois que verfica o and
print(res)

# Exercício com tudo isso
nome = input('Informe seu nome: ')
nota1 = float(input('Informe a nota final da primeira matéria: '))
nota2 = float(input('Informe a nota final da segunda matéria: '))
nota3 = float(input('Informe a nota final da terceira matéria: '))
if(nota1 >= 7 and nota2 >= 7 and nota3 >= 7):
    print('Parabéns, {}. Você passou de ano!'.format(nome))
else:
    print('Foi mal, {}. Você reprovou ;-;.'.format(nome))


# Condicionais aninhados (dentro do outro)
# Exercício: pegar se o user quer comprar maça, banana ou laranja. Pegar a quantidade e calcular quanto irá pagar
# Maça: 2.30 // Laranja: 3.60 // Banana: 1.85
fruta = int(input('Digite o número do produto que deseja comprar (1-Maça, 2-laranja, 3-banana): '))
if(fruta == 1 or fruta == 2 or fruta == 3):
    quantidade = int(input('Digite quantas comprará: '))
    if(fruta == 1):
        print('Vocẽ irá pagar R${} em {} maças.'.format(quantidade * 2.30, quantidade))
    else:
        if(fruta == 2):
            print('Vocẽ irá pagar R${} em {} laranjas.'.format(quantidade * 3.60, quantidade))
        else:
            if(fruta == 3):
                print('Vocẽ irá pagar R${} em {} bananas.'.format(quantidade * 1.85, quantidade))
else:
    print('Valor Inválido')

# # Elif -> Simplifica multiplas condicionais
fruta = int(input('Digite o número do produto que deseja comprar (1-Maça, 2-laranja, 3-banana): '))
quantidade = int(input('Digite quantas comprará: '))

if(fruta == 1):
    print('Vocẽ irá pagar R${} em {} maças.'.format(quantidade * 2.30, quantidade))
elif(fruta == 2):
    print('Vocẽ irá pagar R${} em {} laranjas.'.format(quantidade * 3.60, quantidade))
elif(fruta == 3):
    print('Vocẽ irá pagar R${} em {} bananas.'.format(quantidade * 1.85, quantidade))
else:
    print('Valor Inválido')

# # Exercício 2: SE o nome for igual a "Jorge", esreva na tela. SE for outro, pegue a idade. SE for menor de 18, escrever na tela que é de menor
# # Se for maior que 100 anos, que ele não provavelmente não existe

nome = input('Digite seu nome: ')
if(nome == 'Jorge'):
    print('Oi {}'.format(nome))
else:
    idade = int(input('Digite a sua idade: '))
    if(idade < 18):
        print('Você é menor de idade')
    elif(idade >= 100):
        print('Talvez você não exista com essa idade...')
    else:
        print('Interessante')
