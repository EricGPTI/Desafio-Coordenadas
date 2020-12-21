from coordenadas.classes.spin import Spin
from coordenadas.classes.moviment import Moviment
from api.models import Position


def process_data(actions):
    """
    Processa os dados vindos da view movement
    :param actions: Comandos de movimentação e giro.
    :return: Retorna a posição atual ou mensagem de erro.
    """
    coordenadas = list(Position.objects.all())
    for value in coordenadas:
        id = int(value.id)
        x = int(value.x)
        y = int(value.y)
        f = int(value.face)
        last_position = value.last_position

    coordinates = [x, y, f]
    old_position = f'{x},{y},{f}'

    spin = Spin(coordinates)
    try:
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
                return 'Um movimento inválido foi identificado. Nenhuma ação foi executada.'

        if isinstance(coordinates, str):
            return coordinates
        else:
            old_coordinates = Position(id=id, last_position=old_position)
            old_coordinates.save()
            new_coordinates = Position(id=id, x=coordinates[0], y=coordinates[1], face=coordinates[2],
                                       last_position=old_position)
            new_coordinates.save()
            return coordinates
    except TypeError:
        return 'Um movimento inválido foi identificado. A sonda ultrapassou o limite da área de contato e se perdeu.'
