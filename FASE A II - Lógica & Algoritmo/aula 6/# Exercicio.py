""" Achar a quantidade de alunos que tiraram a nota mínima numa lista (7 é a nota) """
notas = [9, 7, 7, 8, 5, 4, 3, 8, 7]
print(notas.count(7))

""" Alterar a última nota para 4 """
notas.pop()
notas.append(4)
print(notas)

# Também serviria:
notas = [9, 7, 7, 8, 5, 4, 3, 8, 7]
notas[-1] = 4
print(notas)

""" Encontrar a maior nota """
notas = [9, 7, 7, 10, 5, 4, 3, 8, 7]
maiorNota = 0
for i in notas:
    if i > maiorNota:
        maiorNota = i
print(maiorNota)

""" Ordenar lista de notas """
notas = [9, 7, 7, 10, 5, 4, 3, 8, 7]
notas_ordenadas = sorted(notas)
print(notas_ordenadas)

notas = [9, 7, 7, 10, 5, 4, 3, 8, 7]
notas_ordenadas = sorted(notas, reverse=True)
print(notas_ordenadas)

""" Média das notas """
media = 0
soma = 0
for i in notas:
    soma += i
media = soma / len(notas)
print(media)