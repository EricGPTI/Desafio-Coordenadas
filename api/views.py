from .models import Position
from .classes.moviments import Moviment
from .serializer import PositionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def start(request):
    if request.method == 'POST':
        data = {'x': 0,
                'y': 0,
                'face': 'Direita',
                'start': '0,0,90',
                'last_position': '0,0,90'
                }
        Position.objects.update_or_create(data)
        start_position = Position.objects.all()
        serializer = PositionSerializer(start_position, many=True)
        return Response(serializer.data[0])


@api_view(['GET'])
def atual(request):
    if request.method == 'GET':
        atual = Position.objects.all()
        serializer = PositionSerializer(atual, many=True)
        coordenada_atual = serializer.data[0].get('last_position')
        return Response(coordenada_atual)
