from coordenadas.classes.spin import Spin

COMMANDS = {'GE': 'Girar_Esquesda',
            'GD': 'Girar_Direita',
            'M': 'Movimentar'
            }

MATRIZ = [[(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)],
          [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)],
          [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
          [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)],
          [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]]


def process_data(actions): # actions = ["GE", "GE", "M"]
    """Aqui devo pegar os dados vindso do banco de dados."""
    x = MATRIZ[4][0][0]
    y = MATRIZ[4][0][1]
    f = 90
    coordinates = [x, y, f] # [0,0,90]
    new_position = []
    old_position = []

    movement = Spin(coordinates)

    for action in actions:
        if action == 'GE':
            f = movement.ge() # 0
            coordinates[2] = f
            return coordinates[2]

        #    start_position[2] = ge(start_position[2]) # [0,0,0]
        #    contador += 1 if contador < len(comandos) else contador
        #    print(contador)
        #    print(start_position)
        #    test_matriz_limites(start_position, contador)
        #    return start_position
        # elif comando == 'GD':
        #    start_position[2] = gd(start_position[2])
        #    contador += 1 if contador < len(comandos) else contador
        #    print(contador)
        #    print(start_position)
        #    test_matriz_limites(start_position, contador)
        #    start_position
        # else:
        #    movement = move(start_position) #start_position = [0,1,0]
        #    response = valida_position(movement)
        #    contador += 1 if contador < len(comandos) else contador
        #    start_position = response
        #    print(contador)
        #    print(start_position)
        #    test_matriz_limites(start_position, contador)
        #    return start_position


if __name__ == '__main__':
    comandos = ['GE']
    test_matriz_limites(comandos)
