# Functions
def realce():
    print('|','_' * 10, '|')
    print('|','_' * 10, '|')

realce()
print('     Hello')
realce()

#Passar params
def realce(s1):
    print('|','_' * 10, '|')
    print('|','_' * 10, '|')
    print(s1)
    print('|','_' * 10, '|')
    print('|','_' * 10, '|')

realce('     Hello')

def sub2(x, y):
    res = x - y
    print(res)

sub2(5, 2)
sub2(y = 5, x = 2)

# Params não opicinais
def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    print(res)

soma3(1, 2, 3)
soma3(1, 2)
soma3(2)

# Exercício -> Criar uma caixa em volta de uma palavra, que se adapte ao tamanho
def borda(s1):
    tam = len(s1)
    if tam:
        print('+','-' * tam, '+')
        print('|', s1, '|')
        print('+','-' * tam, '+')

borda('Olá')
borda('Olá Mundo!')

# Escopo de variáveis -> Termina onde uma variável pode ser usada
# Escopo local -> criada sempre que é chamada, só existem dentro da função em questão, chamar fora não rola
# Escopo Global -> criada no programa, existe em todas as funções que a invoca

def comida():
    print(ovos)

ovos = 12 # Global
comida()

def comida():
    ovos = 10
    bacon()
    print(ovos)

def bacon():
    ovos = 6

comida()

def comida():
    ovos = 'variável local de comida'
    print(ovos)

def bacon():
    ovos = 'vairável local de bacon'
    print(ovos)
    comida()
    print(ovos)

ovos = 'variável global'
bacon()
print(ovos)

# Instrução global
def comida():
    global ovos
    ovos = 'comida'

ovos = 'global'
comida()
print(ovos)

# Retorno de parametros

# Procedimento (procedure) - uma rotina sem retorno
# Função - uma rotina que retorna um dado a quem a invocou
def soma4(x = 0, y = 0, z = 0):
    res = x + y + z
    return res

retornado = soma4(1, 2, 3)
print(retornado)

print(soma4(2, 2))

retornado1 = soma4(2, 3, 1)
retornado2 = soma4(3, 1)
retornado3 = soma4()

print('Somatório: {}, {} e {}'.format(retornado1, retornado2, retornado3))

# Exercício -> valida string
def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1

x = valida_string('Digite uma string: ', 10, 30)
print('Você digitou a string: {}. \nDado válido. Encerrando o programa...'.format(x))

# Recursos avançados:
# Erro de sintaxe: falta algo na sintaxe
# Erro de exceções: pode ser um dado errado digitado pelo user ou até algo maior
# ZeroDivisionError -> Não é possível dividir por 0
# ValueError -> Dado não esperado 
# IndexError -> Índice inexistente sendo acessado

while True:
    try:
        x = int(input('Por favor, Digite um número: '))
        break
    except ValueError:
        print('Oops, valor inválido, tente de novo.')

def div():
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Impossível dividir por 0. Tente de novo')
    except:
        print('Algo de errado aconteceu...')
    else:
        return res
    finally:
        print('Executará sempre!')

print(div())

def imprime_com_condicao(num, fcond):
    if fcond(num):
        print(num)

def par(x):
    return x % 2 == 0
def impar(x):
    return not par(x)

imprime_com_condicao(5, par)
imprime_com_condicao(5, impar)


# Função Lambda
res = lambda x: x * x
print(res(3))

soma = lambda x, y: x + y
print(soma(3, 5)), 