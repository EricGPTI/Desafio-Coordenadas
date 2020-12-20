import pytest
from django.test import TestCase
from coordenadas.classes.moviments import Moviment

def test_movement_ge():
    """
    Testando método GE da classe Moviment
    :param: ["GE", "GE", "M"]
    :return: eve retornar error
    """
    actions = ["GE", "GE", "M"]
    moviment = Moviment(actions)
    response = moviment.ge()
    print(response)