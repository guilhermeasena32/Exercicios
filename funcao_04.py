
"""Programa para converter notacao de 24horas para 12horas."""


class conversao:
    """Classe para conversao de horas 24 para 12."""

    def __init__(self, horas, minutos):
        """Def construtor."""
        self.horas = horas
        self.minutos = minutos

    def conv(self):
        """Funcao para converter as horas para formato 12 e imprimir."""
        if self.horas > 12:
            self.horas -= 12
            return "{}:{} PM".format(self.horas, self.minutos)
        else:
            return "{}:{} AM".format(self.horas, self.minutos)


relogio = conversao(14, 25)
times = relogio.conv()
print(times)
