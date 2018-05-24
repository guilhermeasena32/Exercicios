
u"""
Funcao.

Faça uma função que informe a quantidade de dígitos de um determinado
número inteiro informado.
"""


def quantidade():
    """Funcao para retornar o tamanho do valor informado pelo usuario."""
    num = int(input("informe um numero para saber a quantidade de digitos: "))
    return (len(str(num)))


quantidade
print(quantidade())
