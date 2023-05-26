# Função que calcula o fatorial de um param de função
# Validar somente valores + 
# criar help da function

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fatorial(num):
    """
    Calcula o Fatorial de um num
    :param num: número inteiro passado como parâmetro para o calculo
    :return: caso num seja igual a 0 retorna 1 (0! = 1) ou o fatorial de um número positivo digitado
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num + 1, 1):
        fat *= i
    return fat


valor = valida_int('Digite um número para calcular seu fatorial: ', 0, 9999999999)
print('{}! = {}'.format(valor, fatorial(valor)))
# help(fatorial)