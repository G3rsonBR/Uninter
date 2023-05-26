""" Criar uma Tupla com 10 palavras, em cada palavra, pegar suas vogais, e printar a palvra + suas vogais """
palavras = ('Gerson', 'gosta', 'de', 'comer', 'açai', 'com', 'leite', 'condensado', 'acredita?')
palavraVogal = {}
vogal = []

for i in palavras:
    for j in i:
        if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
            vogal.append(j)
        palavraVogal[i] = vogal
    vogal = []

for i in palavraVogal:
    print('Palvra: {} - Contém vogais: {}'.format(i, palavraVogal[i]))

# Forma feita na aula:
palavras = ('Gerson', 'gosta', 'de', 'comer', 'açai', 'com', 'leite', 'condensado', 'acredita?')

for palavra in palavras:
    print('\nPalavra: {}. Vogais: '.format(palavra.upper()), end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')