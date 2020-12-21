from coordenadas.classes.spin import Spin
from coordenadas.classes.moviment import Moviment
from api.models import Position

COMMANDS = {'GE': 'Girar_Esquesda',
            'GD': 'Girar_Direita',
            'M': 'Movimentar'
            }

MATRIZ = [[(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)],
          [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)],
          [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
          [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)],
          [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]]


def process_data(actions):
    """Aqui devo pegar os dados vindos do banco de dados."""
    data = Position.objects.all()
    x = MATRIZ[4][0][0]
    y = MATRIZ[4][0][1]
    f = 90
    coordinates = [x, y, f]
    old_position = [x, y, f]

    spin = Spin(coordinates)
    for action in actions:
        if action == 'GE':
            f = spin.ge()
            coordinates[2] = f
        elif action == 'GD':
            f = spin.gd()
            coordinates[2] = f
        elif action == 'M':
            movement = Moviment(coordinates)
            coordinates = movement.move()
        else:
            return 'Um movimento inválido foi identificado. ' \
                        'A sonda ultrapassou o limite da área de ' \
                        'contato e se perdeu.'
    return coordinates

