POSITION = {
    270: 'Esquerda',
    180: 'Baixo',
    90: 'Direita',
    0: 'Cima'
}


class Moviment:
    """
    Objeto para movimentação na Matriz.
    """
    def __init__(self, coordenadas):
        self.coordenadas = coordenadas

    def validate_position(self):
        """
        Valida se nova posição não ultrapassa os limites do quadrante.
        :return: Retorna nova posição ou mensagem de erro.
        """
        error_message = 'Um movimento inválido foi identificado. ' \
                        'A sonda ultrapassou o limite da área de ' \
                        'contato e se perdeu.'

        if self.coordenadas[0] < 0 or self.coordenadas[1] < 0 or self.coordenadas[0] > 4 or self.coordenadas[1] > 4:
            return (error_message)
        else:
            return (self.coordenadas)

    def move(self):
        """
        Executa a movimentação na matriz.
        :return: Retorna nova posição ou mensagem de erro vindo do
        método de validação da posição.
        """
        face = self.coordenadas[2]
        if POSITION.get(face) == 'Direita':
            self.coordenadas[0] += 1
            new_coordinates = self.validate_position()
            return new_coordinates

        elif POSITION.get(face) == 'Esquerda':
            self.coordenadas[0] -= 1
            new_coordinates = self.validate_position()
            return new_coordinates

        elif POSITION.get(face) == 'Cima':
            self.coordenadas[1] += 1
            new_coordinates = self.validate_position()
            return new_coordinates

        elif POSITION.get(face) == 'Baixo':
            self.coordenadas[1] -= 1
            new_coordinates = self.validate_position()
            return new_coordinates
