from coordenadas.classes.spin import Spin


# Test Spin
class TestSpin:
    coordinates = [0, 0, 90]

    def test_spin_ge(self):
        spin = Spin(self.coordinates)
        face = spin.ge()
        assert face == 0

    def test_spin_gd(self):
        spin = Spin(self.coordinates)
        face = spin.gd()
        assert face == 180
