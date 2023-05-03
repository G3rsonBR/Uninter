# Exercícios práticos da apostila:

# Criar uma variável String que recebe uma frase qualquer, uma segunda que recebera a metade dessa primeira.
# Imprimir os dois últimos caracteres da segunda variável string.

frase = input('Escreva uma frase qualquer: ')
tam = len(frase)
metade = frase[:tam//2]
print(metade[-2:])