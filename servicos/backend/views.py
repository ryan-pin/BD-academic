from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
# from django.db.models import Count, Max, Min, Sum


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivrosViewSet(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer

class EditorasViewSet(viewsets.ModelViewSet):
    queryset = Editoras.objects.all()
    serializer_class = EditorasSerializer

class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class EmprestimosViewSet(viewsets.ModelViewSet):
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimosSerializer