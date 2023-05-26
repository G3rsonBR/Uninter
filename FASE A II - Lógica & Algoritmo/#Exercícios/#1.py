ru_identificador = 000000

print('Bem Vindo a Loja do Gerson Lucas Silva Leite.')

def valida_dado(pergunta, min, max, tipo, erro):
    """
        Faz a validação dos dados.
        :pergunta: Parâmetro que será usado para imprimir no console o que está sendo solicitado
        :min: Valor mínimo esperado na entrada
        :max: Valor máximo esperado na entrada
        :tipo: Define o tipo de dado que está sendo pedido
        :erro: mensagem apresentada quando o usuário digitar um valor fora do min e max
    """
    try:
        x = tipo(input(pergunta))
        while ((x < min) or (x > max)):
            print(erro)
            x = tipo(input(pergunta))
        return x
    except ValueError:
        print('\nOpa, digite apenas números inteiros!')


valor = valida_dado('Digite o Valor do produto (ex: 12.50): ', 0, 999999999999999999999, float, 'Digite um valor válido...')
quantidade = valida_dado('Digite a Quantidade que levará: ', 0, 999999999999999999999, int, 'Digite um valor válido...')
# Variáveis de entrada do valor do produto e da quantidade

if quantidade >= 10 and quantidade <= 99:
    desconto = 5 / 100
elif quantidade >= 100 and quantidade <= 999:
    desconto = 10 / 100
elif quantidade >= 1000:
    desconto = 15 / 100
else:
    desconto = 1
# Estrutura de decisão que verifica a quantidade, e aplica o desconto de acordo com o foi pedido no enunciado 

semDesconto = valor * quantidade
comDesconto = semDesconto - (semDesconto * desconto)
# Variáveis que armazenam o valor sem e com o desconto, com seus devidos calculos.

print('Valor sem o desconto: R$ {:.2f}'.format(semDesconto))
print('Valor com o desconto: R$ {:.2f}'.format(comDesconto))
print('Desconto: R$ {:.2f}'.format(semDesconto - comDesconto))
# Impressão do resultado dos parametros passados.