class Moviment:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def ge(self):
        rotation = 0
        if self.coordinates[2] - 90 == -90: # 0
            new_face = rotation + 270
            return new_face
        else:
            new_face = rotation - 90 # 0
            return new_face

    def gd(self):
        global f
        rotation = 0
        if last_position + 90 == 360:
            rotation = 0
            new_start_position = move(rotation)
            f = new_start_position
            return new_start_position
        else:
            rotation = last_position + 90
            new_start_position = move(rotation)
            f = new_start_position
            return new_start_position

    def move(self):
        if isinstance(start_position, int):
            return start_position # [0,0,0]
        elif POSITION.get(start_position[2]) == 'Cima':
            y += 1
            new_position = [x, y, f] # [0,1,0]
            return new_position
        elif POSITION.get(start_position[2]) == 'Baixo':
            y -= 1
            new_position = [x, y, f]
            return new_position
        elif POSITION.get(start_position[2]) == 'Direita':
            x += 1
            new_position = [x, y, f]
            return new_position
        elif POSITION.get(start_position[2]) == 'Esquerda':
            x -= 1
            new_position = [x, y, f]
            print(new_position)
            return new_position

    def valida_position(movement):
        if movement[0] < 0 or movement[0] > 4 or movement[1] < 0 or movement[1] > 4:
            raise ValueError('Erro: Um movimento inválido foi identificado. \n '
                'Sonda ultrapassou o limite da área de contato e se perdeu.')
        else:
            return movement