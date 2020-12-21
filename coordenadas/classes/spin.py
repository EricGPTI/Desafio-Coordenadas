class Spin:
    """
    Classe que executa as movimentações na matriz
    :param: recebe uma lista contendo as movimentações.
    """

    def __init__(self, start):
        self.start = start

    def ge(self):
        """
        Método para movimentação à esquerda.
        :return: Retorna a nova posição visual na matriz.
        """
        face = self.start[2]
        if face - 90 < 0:
            new_positiion = face + 270
            return new_positiion
        else:
            new_positiion = face - 90
            return new_positiion

    def gd(self):
        """
        Método para movimentação à esquerda.
        :return: Retorna a nova posição visual na matriz.
        """
        face = self.start[2]
        if face + 90 == 360:
            new_positiion = face - 270
            return new_positiion
        else:
            new_positiion = face + 90
            return new_positiion
