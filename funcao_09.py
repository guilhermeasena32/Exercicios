

u"""
Data com mês por extenso Construa uma função que receba uma data no formato.

DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""


def datas():
    """Funcao para transformar o mesPorExtenso."""
    date = input('Digite a data no formato (DD/MM/AA): ')
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return '{} de {} de {}'.format(date[0:2], meses[int(date[3:5])-1],
                                   date[6:10])


datas
print(datas())
