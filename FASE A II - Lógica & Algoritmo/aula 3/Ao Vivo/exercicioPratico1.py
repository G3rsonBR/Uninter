nome = input('Digite seu nome: ')
valorProd = float(input('Entre com valor do produto: '))
quantidadeProd = int(input('Entre com quantidade do produto: '))

semDesconto = valorProd * quantidadeProd

if 5 <= quantidadeProd <= 19:
    desconto = semDesconto * (3 / 100)
elif 20 <= quantidadeProd <= 99:
    desconto = semDesconto * (6 / 100)
elif quantidadeProd >= 100:
    desconto = semDesconto * (10 / 100)
else:
    desconto = 0

comDesconto = semDesconto - desconto

print('O valor sem desconto: {:.2f}'.format(semDesconto))
print('O valor com desconto: {:.2f}'.format(comDesconto))