# Exercícios de Fixação da Aula 2

# Expressões
# A) Somatório dos 5 primeiros números inteiros e positivos
print(1 + 2 + 3 + 4 + 5)

# B) A média entre 23, 19 e 31
print((23 + 19 + 31) / 3)

# C) O número de vezes que 73 cabe em 403
print(403 // 73)

# D) A sobra quando 403 é dividido por 73
print(403 % 73)

# E) 2 elavado à 10° potencia 
print(2 ** 10)

# F) O valor absoluto da diferença entre 54 e 57
print(abs(54 - 57))

# G) O menor valor entre 34, 29 e 31
print(min(34, 29, 31))


# Atribuições
# A) Atribuir o valor inteiro 3 à variável "a"
a = 3
print(a)

# B) Atribuir o valor 4 à variável "b"
b = 4
print(b)

# C) atribuir à variável "c" o valor da expressão a * a + b * b
c =  a * a + b * b
print(c)

# Strings
# Execute as seguintes atribuições
s1 = 'ant'
s2 = 'bat'
s3 ='cod'
print(s1)
print(s2)
print(s3)

# Utilizando os operadores + e *, cria as saídas:
# A) 'ant bat cod'
print(s1 + ' ' + s2 + ' ' + s3)

# B) 'ant ant ant ant ant ant ant ant ant ant'
print((s1 + ' ') * 10)

# C) 'ant bat bat cod cod cod
print(s1 + ' ' + ((s2 + ' ') * 2) + ((s3 + ' ') * 3))

# D) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
print(((s1 + ' ') + (s2 + ' ')) * 8)

# E) 'batbatcod batbatcod batbatcod batbatcod batbatcod'
print(((s2 + s2 + s3) + ' ') * 4)