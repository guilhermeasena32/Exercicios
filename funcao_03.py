
u"""
Faça um programa com uma função chamada somaImposto. A função possui dois.

parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas
expressa em porcentagem e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""


def somaImposto(taxaImposto, custo):
    """Funcao para calcular imposto sobre custo."""
    return (0.01 * taxaImposto) * custo + custo
# 0.10 * custo = 10 + custo = 110


soma = somaImposto(10, 100)
print(soma)
