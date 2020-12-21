from coordenadas.classes.moviment import Moviment


# Test Moviment
class TestMoviment:

    def test_move_right(self):
        coordenadas = [0, 0, 90]
        movement = Moviment(coordenadas)
        mr = movement.move()
        assert mr[0] == 1

    def test_move_left(self):
        coordenadas = [1, 0, 270]
        movement = Moviment(coordenadas)
        mr = movement.move()
        assert mr[0] == 0

    def test_move_up(self):
        coordenadas = [0, 0, 0]
        movement = Moviment(coordenadas)
        mr = movement.move()
        assert mr[1] == 1

    def test_move_down(self):
        coordenadas = [0, 1, 180]
        movement = Moviment(coordenadas)
        mr = movement.move()
        assert mr[1] == 0

    def test_move_limit(self):
        coordenadas = [0, 0, 180]
        movement = Moviment(coordenadas)
        mr = movement.move()
        assert mr[1] != 0
