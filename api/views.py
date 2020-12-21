from .models import Position
from coordenadas.core import process_data
from .serializer import PositionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def start(request):
    """
    View para redefinição das coordenadas.
    :param request: Não recebe nenhum parâmetro no corpo da requisição.
    :return: retorna a posição inicial (0,0,90)
    """
    if request.method == 'POST':
        data = {'x': 0,
                'y': 0,
                'face': 90,
                'start': '0,0,90',
                'last_position': '0,0,90'
                }
        Position.objects.update_or_create(data)
        start_position = Position.objects.all()
        serializer = PositionSerializer(start_position, many=True)
        return Response(serializer.data[0])


@api_view(['GET'])
def atual(request):
    """
    View para obtenção dos dados da posição atual.
    :param request: Não recebe nenhum parâmetro no corpo da requisição.
    :return: Retorna as coordenadas atuais gravadas no banco, sendo x, y, e face.
    """
    if request.method == 'GET':
        atual = Position.objects.all()
        serializer = PositionSerializer(atual, many=True)
        current_coordinates = {
            'x': serializer.data[0].get('x'),
            'y': serializer.data[0].get('y'),
            'face': serializer.data[0].get('face')
        }
        return Response(current_coordinates)


@api_view(['POST'])
def movement(request):
    """
    View para movimentação dada uma coordenada.
    :param request: Recebe as posições de GE ou GD (Giar a Direita ou Girar a Esquerda)
    e M (Movimentar)
    :return: Retorna a posição atual ou uma mensagem de erro.
    """
    if request.method == 'POST':
        actions = request.data['movimentos']
        moviments = [x.upper() for x in actions]
        response_moviment = process_data(moviments)
        return Response(response_moviment)
