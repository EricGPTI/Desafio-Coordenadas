from coordenadas.core import process_data

POSITION = {
    270: 'Esquerda',
    180: 'Baixo',
    90: 'Direita',
    0: 'Cima'
}

COMMANDS = {'GE': 'Girar_Esquesda',
            'GD': 'Girar_Direita',
            'M': 'Movimentar'
            }

MATRIZ = [[(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)],
          [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)],
          [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
          [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)],
          [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]]


def test_spin_ge(act):
    """
    Testando método GE da classe Moviment
    :param: ["GE", "GE", "M"]
    :return: eve retornar error
    """
    x = MATRIZ[4][0][0]
    y = MATRIZ[4][0][1]
    f = 90
    start = [x, y, f]
    response = process_data(act)
    x = response[0]
    y = response[1]
    f = response[2]
    assert x == 1
    assert y == 2
    assert f == 90


def test_spin_gd(act):
    """
    Testando método GD da classe Moviment
    :param: ["GE", "GE", "M"]
    :return: eve retornar error
    """
    x = MATRIZ[4][0][0]
    y = MATRIZ[4][0][1]
    f = 90
    start = [x, y, f]
    response = process_data(act)


act = ["GE", "M", "M", "GD", "M"]
test_spin_ge(act)

act = ["GD", "GD", "GD"]
test_spin_gd(act)
