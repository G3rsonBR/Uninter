# AULA 1 -  Ciclos de Processamentos de Dados 
print('Hello World') #texto literal

# Cuidados: Letras Maiusculas e Minusculas fazem diferença, atente-se 
# A comunidade Python usa mais aspas simples, porém é aceito as duplas para strings

print(2 + 2) # calculo literal
print('2 + 2') # texto literal
print('2' + '2') # concatenação => união de dois textos
print('Olá ' + 'Mundo') # Assim concatenamos
print('Olá', 'Mundo') # Assim temos dois textos que são impressos juntos
print('O resultado de 2 + 3 é:', 2 + 3) #concatenando Texto + Números 

# Operadores Matemáticos:
# Igual na matemática, temos que respeitar as ordens

print(10*(5+7)/4)
print(10*(5+7/4)) 
# São resultados diferentes

# ------------------------------------------------------------------------

# AULA 2 -  Variáveis, dados e seus tipos

# Variável = Espaço de armazenamento de um dado
nota = 8.5
diciplina = 'Lógica de Programação e Algoritmo'
print(nota)
print(diciplina)
print('Diciplina:', diciplina, '|| nota:', nota)

# Variáveis não podem começar com numeros ou simbolos, a não ser o _ (underline)
# então: nota e _nota são nomes válidos de variáveis, mas 1nota ou $nota não são, porém nota1 ou n0t4 funcionam 
# _n_o_t_a também é válido, preço (com acento) é aceitável, mas NÃO USE, pois apenas a v3 do python aceita, e é uma das poucas linguagens que aceitam acentuação

# Tipos de variáveis:
# Inteiros (int, sem casas decimais) ou Ponto Flutuante (Float, com casas decimais) -> São para números
# Boolean (verdadeiro ou falso, 0 ou 1, nível lógico alto ou baixo)
# String -> Textos

# Variáveis Lógicas:
a = 1
b = 5
resposta = a == b
print(resposta) # Falso, porque "a" não é igual a "b"

resposta = a != b
print(resposta) # Verdadeiro, pois "a" é diferente de "b"

# Variáveis String
frase = 'Olá Mundo!'
print(frase)

print(frase[0])
print(frase[5])
# Usando os [], podemos pegar o indice da palavra,


# AULA 3 - Sessão apenas de Strings

s1 = 'Lógica de Programação'
s1 = s1 + ' e Algoritmos'
print(s1)

s1 = 'A' + '-' * 10 + 'B'
print(s1)
# Um recurso interessante é que podemos multiplicar a quantidade que vezes que o caracter irá aparecer

# Composição
nota = 8.5
s1 = 'Você tirou %f na disciplina de Algoritmos' % nota
print(s1)
# Substituímos o %f pela variável no final do texto

nota = 8.5
s1 = 'Você tirou %.2f na disciplina de Algoritmos' % nota
print(s1)
# Aqui limitamos o número de casas decimais

nota = 8.5
disciplina = 'Algoritmo'
s1 = 'Você tirou %.2f na disciplina de %s' % (nota, disciplina)
print(s1)

# Por que %f, %s? -> Cada tipo de variável tem seu respectivo %
# %d ou %i servem para Int // %f é para Float // %s é para Strings

# Composição Moderna:
s1 = 'Você tirou {} na disciplina de {}' .format(nota, disciplina)
print(s1)

# Fatiar String
s1 = 'Lógica de Programação e Algoritmos'
print(s1[0:6])
print(s1[24:34])
print(s1[:6]) # É como a primeira fatiada, mas sem o 0

# Saber o tamanho de uma String
s1 = 'Lógica de Programação e Algoritmos'
tamanho = len(s1)
print(tamanho)

# AULA 4 - Função de entrada e fluxo de execução do programa
# Função de entrada -> input

idade = input('Qual sua Idade? ')
print(idade)

nome = input('QUal seu nome? ')
print('Olá {}, seja bem-vindo!'.format(nome))

# Atenção: O resultado do input sempre retoarna uma String
# Uma forma de converter para Number é...
nota = float(input('Qual nota você recebeu na diciplina? '))
print('Você tirou nota {}.'.format(nota))


# EXERCÍCIO DE FIXAÇÃO: Receba dois valores inteiros definidos pelo usuário e imprima a soma dos mesmos

a = int(input('Digite o Primeiro Valor: '))
b = int(input('Digite o Segundo Valor: '))
print('A soma de {} com {}, é: {}.'.format(a, b, a + b))