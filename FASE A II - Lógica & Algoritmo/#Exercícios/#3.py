ru_identificador = 000000

def verifica_valor(pergunta, min, max):
    """
    Função que verifica se o número passado é um número de ponto flutuante (pois números inteiros entram nessa categoria)
    : valor: parametro passado para a verificação de seu tipo 
    : min: parametro com o valor minimo que 'valor' deve estar 
    : max: parametro com o valor máximo que 'valor' deve estar 
    """
    try:
        x = float(input(pergunta))
        while ((x < min) or (x >= max)):
            if x < min:
                print('Valor abaixo do permitido, tente novamente')    
            elif x >= max:
                print('Valor acima ou no valor permitido, tente novamente'.format(max))
            x = float(input(pergunta))
        return x
    except ValueError:
        print('Digite um valor válido')
        verifica_valor(pergunta, min, max)

def dimensoesObjeto():
    while True:
        comprimento = verifica_valor('Digite o Comprimento (em cm) do objeto: ', 0.1, 100000)
        altura = verifica_valor('Digite a Altura (em cm) do objeto: ', 0.1, 100000)
        largura = verifica_valor('Digite a Largura (em cm) do objeto: ', 0.1, 100000)
        volume = comprimento * altura * largura
        # Variáveis que invocam a função verifica_valor, a qual faz uma verificação: do tipo da variável e toma um caminho,
        # Ou ela faz a verificação se o valor digitado é maior ou menor que o valor maximo e minimo (respectivamente)
        # Ou ela entra no except do "ValueError" e pede para voltar e digitar um valor váldio para continuar o código.
        if volume < 1000:
            valor = 10
            return valor
        elif 1000 <= volume < 10000:
            valor = 20
            return valor
        elif 10000 <= volume < 30000:
            valor = 30
            return valor
        elif 30000 <= volume < 100000:
            valor = 50
            return valor
        else:
            print('Não é aceito (Volume máximo: 99999 cm3, informado: {} cm3)'.format(volume))
            continue
    # Estrutura de decisão que toma um caminho de acordo com o volume do objeto

def pesoObjeto():
    while True:
        peso = verifica_valor('Digite o peso (em Kg) do Objeto: ', 0, 999999)
        if peso <= 0.1:
            multi = 1
            return multi
        if 0.1 <= peso < 1:
            multi = 1.5
            return multi
        if 1 <= peso < 10:
            multi = 2
            return multi
        if 10 <= peso < 30:
            multi = 3
            return multi
        else:
            print('Não é aceito (Peso máximo: 29.99Kg, informado: {}Kg)'.format(peso))
            continue
    # Function que pega o peso do objeto invocando a mesma Function "verifica_valor", e toma uma decisão de acordo com o peso final do objeto, definindo o multiplicador

def rotaObjeto():
    rota = ''
    print('Rotas disponíveis:')
    print('RS - Do Rio de Janeiro até São Paulo')
    print('SR - De São Paulo até o Rio de Janeiro')
    print('BS - De Brasília até São Paulo')
    print('SB - De São Paulo até Brasília')
    print('BR - De Brasília até o Rio de Janeiro')
    print('RB - Do Rio de Janeiro até Brasília')
    while True:
        rota = input('Digite a rota do Objeto (apenas a sua sigla): ')
        if rota.upper() == 'RS' or rota.upper() == 'SR':
            multi = 1
            return multi
        elif rota.upper() == 'BS' or rota.upper() == 'SB':
            multi = 1.2
            return multi
        elif rota.upper() == 'BR' or rota.upper() == 'RB':
            multi = 1.5
            return multi
        else:
            print('Digite uma rota válida (digitada: {}))'.format(rota))
            continue
    # Function que imprime as rotas disponíveis e armazena a escolha do usuário, em seguite define o valor do multiplicador de Rota   

resultDimensao = dimensoesObjeto()
resultPeso = pesoObjeto()
resultRota = rotaObjeto()
total = resultDimensao * resultPeso * resultRota
print('Total a pagar(R$): {} (dimensões: {} * peso: {} * rota: {})'.format(total, resultDimensao, resultPeso, resultRota))
# Invocando todas as funções e calculando o valor final da encomenda.