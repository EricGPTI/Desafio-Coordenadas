POSITION = {
    270: 'Esquerda', 
    180: 'Baixo',
    90: 'Direita',
    0: 'Cima', 
}

COMMANDS = {'GE': 'Girar_Esquesda',
            'GD': 'Girar_Direita', 
            'M': 'Movimentar'
}

MATRIZ = [
        [(0,4), (1,4), (2,4), (3,4), (4,4)], 
        [(0,3), (1,3), (2,3), (3,3), (4,3)], 
        [(0,2), (1,2), (2,2), (3,2), (4,2)], 
        [(0,1), (1,1), (2,1), (3,1), (4,1)], 
        [(0,0), (1,0), (2,0), (3,0), (4,0)]
    ]

start_rotation = 90
x = MATRIZ[4][0][0]
y = MATRIZ[4][0][1]
f = start_rotation

def ge(last_position):
    rotation = 0
    if last_position - 90 == -90:
        rotation += 270
        new_start_position = move(rotation)
        return new_start_position
    else:
        rotation = last_position - 90
        new_start_position = move(rotation)
        return new_start_position


def gd(last_position):
    rotation = 0
    if last_position + 90 == 360:
        rotation = 0
        new_start_position = move(rotation)
        return new_start_position
    else:
        rotation = last_position + 90
        new_start_position = move(rotation) 
        return new_start_position


def move(position):
    if isinstance(position, int):
        return position
    elif position[0] < 0 or position[0] > 4 \
        or position[1] < 0 or position[1] > 4:
        raise ValueError('Erro: Um movimento inválido foi identificado. \n '
            'Sonda ultrapassou o limite da área de contato e se perdeu.')
        start_rotation = POSITION.get(position[2])
    new_position = POSITION.get(position[2])
    if new_position == 'Baixo' and position[1] == 0 \
        or new_position == 'Esquerda' and position[0] == 0 \
        or new_position == 'Direita' and position[0] > 4:
        raise ValueError('Erro: Um movimento inválido foi identificado. \n '
                        'Sonda ultrapassou o limite da área de contato e se perdeu.')


def test_matriz_limites(comandos) -> list:
    start_position = [x, y, f] 
    for c in comandos:
        if c == 'GE':
            start_position[2] = ge(start_position[2])
        elif c == 'GD':
            start_position[2] = gd(start_position[2])
        else:
            movement = move(start_position)
            return movement


if __name__== '__main__':
    comandos = ['GD', 'GD', 'M']
    test_matriz_limites(comandos)
