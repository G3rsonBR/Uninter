# Interactive Help
# Intricica na function
help(print)

# Docstring
def soma(x=0, y=0, z=0):
    """
    Função que soma até 3 params
    :param x: valor int opcional
    :param y: valor int opcional
    :param z: valor int opcional
    """
    return x + y + z
print(soma(1, 2, 3))
help(soma)