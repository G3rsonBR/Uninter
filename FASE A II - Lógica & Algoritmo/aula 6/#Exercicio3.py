""" Cadastrar pessoas em um dicionário com uma lista, depois imprimir todos os cadastros """

cadastros = {
    'nomes': [],
    'anos': [],
    'sexos': []
}

while True:
    terminar = input('Deseja cadastrar uma pessoa? (S/N): ')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite somente S ou N para cadastrar ou encerrar...')
        continue

    nome = input('Digite o nome: ')
    sexo = input('Digite o sexo [S/N]: ')
    ano = int(input('Digite o ano de nascimento: '))
    cadastros['nomes'].append(nome)
    cadastros['sexos'].append(sexo.upper())
    cadastros['anos'].append(ano)

print(cadastros)

anoAtual = 2023
mediaIdade = 0
for i in cadastros['anos']:
    mediaIdade += (anoAtual - i)

mediaIdade /= len(cadastros['anos'])
print('Média de Idades: {}'.format(mediaIdade))

