# Leia 3 valores, serão lados de um triângulo. Classificar o triângulo
# SE for Equilátero, Isósceles, Escano

lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if (lado1 > 0) and (lado2 > 0) and (lado3 > 0):
    if (lado1 + lado2 < lado3) and (lado2 + lado3 < lado1) and (lado1 + lado3 < lado2):
        if (lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3):
            print('Escaleno')
        elif (lado1 == lado2) and (lado2 == lado3):
            print('Equilatero')
        else:
            print('Isósceles')
    else:
        print('O Triângulo não existe')
else:
    print('O Triângulo não existe')