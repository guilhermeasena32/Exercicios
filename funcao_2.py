
u"""
Faça um programa, com uma função que necessite de um argumento.

A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
e ‘N’, se seu argumento for zero ou negativo.
"""


def imprime(n):
    """Funcao que retorna P se o valor informado for > que 0 e N se for <."""
    if n > 0:
        print('P')
    elif n <= 0:
        print('N')
    return imprime


imprime(1)
