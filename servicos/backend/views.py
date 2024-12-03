from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializers import *

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
# from django.db.models import Count, Max, Min, Sum


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer 

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

    @action(detail=False, methods=['get'])
    def servicos_cliente(self, request):
        cliente_id = request.query_params.get('cliente_id')
        servicos = Servico.objects.filter(cliente_id=cliente_id)
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def servicos_pendentes(self, request):
        cliente_id = request.query_params.get('cliente_id')
        servicos = Servico.objects.filter(cliente_id=cliente_id, pago=False)
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)