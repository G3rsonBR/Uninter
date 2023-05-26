from math import inf

ru_identificador = 000000

codProduto = 0
produtos = []

def valida_dado(pergunta, min, max, type, erro):
    """
        Faz a validação dos dados.
        :pergunta: Parâmetro que será usado para imprimir no console o que está sendo solicitado
        :min: Valor mínimo esperado na entrada
        :max: Valor máximo esperado na entrada
        :type: Define o tipo de dado que está sendo pedido
        :erro: mensagem apresentada quando o usuário digitar um valor fora do min e max
    """
    try:
        x = type(input(pergunta))
        while ((x < min) or (x > max)):
            print(erro)
            x = type(input(pergunta))
        return x
    except ValueError:
        print('\nOpa, digite apenas números inteiros!')

def cadastrar_produto(cod):
    # Função que coloca tem como parametro o código do produto, que é acrescentado de forma automática.
    # É solicitado o nome, fabricante e valor do produto, e depois é adicionada a uma lista de produtos
    # Porém: O produto em si é salvo como um DICIONÁRIO 
    produto = {}

    print('O código do produto é: {}'.format(cod))

    produto['cod'] = cod
    produto['nome'] = input('Digite o NOME da Peça:')
    produto['fabricante'] = input('Digite o Nome do FABRICANTE:')
    produto['valor'] = valida_dado('Digite o VALOR(R$) do produto: ', 0, inf, float, 'Digite um valor válido...')
    produtos.append(produto.copy())
    
    print('')

def listar_produtos():
    while True:
        print('1-Consultar Todas as Peças\n2-Consultar Peça por Código\n3-Consultar Peças por Fabricante\n4-Retornar')
        escolha = valida_dado('Escolha uma opção: ', 1, 4, int, '\nOpção Inválida...')
        print('')
        if escolha == 4:
            break
        elif escolha == 1:
            print('-' * 20)
            for item in produtos:
                for i,j in item.items():
                    print('{}: {}'.format(i, j))
                print('-' * 20)
        elif escolha == 2:
            escolha = valida_dado('Digite o código:', 1, len(produtos), int, '\nOpção Inválida...')
            print('-' * 20)
            for item in produtos:
                if escolha == item['cod']:
                    for i,j in item.items():
                        print('{}: {}'.format(i, j))
                    print('-' * 20)
        elif escolha == 3:
            escolha = input('Digite o nome do Fabricante:')
            print('-' * 20)
            for item in produtos:
                if escolha == item['fabricante']:
                    for i,j in item.items():
                        print('{}: {}'.format(i, j))
                    print('-' * 20)
        print('')
    # Function que lista todas os produtos no sistema de acordo com o usuário, podendo listar Todas as Peças, Peças por Código ou Por Fabricante, e finalizar a consulta

def remover_produto():
    escolha = valida_dado('Digite o Código do Produto para Remover: ', 1, len(produtos), int, 'Digite um valor válido!')
    for item in produtos:
        if escolha == item['cod']:
            return produtos.remove(item)
    print('')
    # Função que remove o item de acordo com o código digitado pelo usuário

print('Bem vindo ao Estoque da Bicicletaria do Gerson Lucas Silva Leite.')
while True:
    print('1-Cadastrar Peça\n2-Consultar Peças\n3-Remover Peça\n4-Sair')
    escolha = valida_dado('Selecione uma opção:', 1, 4, int, 'Opção inválida...')
    print('')
    if escolha == 4:
        break
    elif escolha == 1:
        codProduto += 1
        cadastrar_produto(codProduto)
    elif escolha == 2:
        listar_produtos()
    elif escolha == 3:
        remover_produto()

print('Até mais!')
# Loop que dá as opções que o usuário tem para continuar. 