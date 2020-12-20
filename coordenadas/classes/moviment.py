POSITION = {
    270: 'Esquerda',
    180: 'Baixo',
    90: 'Direita',
    0: 'Cima'
}


class Moviment:
    def __init__(self, start):
        self.start = start

    def validate_position(self):
        error_message = 'Um movimento inválido foi identificado. ' \
                        'Sonda ultrapassou o limite da área de raise ' \
                        'PositionalError  contato e se perdeu.'
        success_message = 'A sonda se movimento com sucesso.'

        if self.start[0] or self.start[1] < 0 or self.start[0] or self.start[1] > 4:
            return error_message, self.start
        else:
            return success_message, self.start

    def move(self):
        face = self.start[2]
        if POSITION.get(face) == 'Direita':
            self.start[0] += 1
            return self.validate_position(self)

        elif POSITION.get(face) == 'Esquerda':
            self.start[0] -= 1
            return self.validate_position(self)

        elif POSITION.get(face) == 'Cima':
            self.start[1] += 1
            return self.validate_position(self)

        elif POSITION.get(face) == 'Baixo':
            self.start[1] -= 1
            return self.validate_position(self)