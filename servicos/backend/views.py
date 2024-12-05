from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import action



class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    @action(detail=True, methods=["get"])
    def livros(self, request, pk=None):
        autor = self.get_object()
        livros = autor.livros.all()
        serializer = LivrosSerializer(livros, many=True)
        return Response(serializer.data)

class LivrosViewSet(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer

    @action(detail=True, methods=["get"])
    def autores(self, request, pk=None):
        livro = self.get_object()
        autores = livro.autores.all()
        serializer = AutorSerializer(autores, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def editora(self, request, pk=None):
        livro = self.get_object()
        serializer = EditorasSerializer(livro.editora)
        return Response(serializer.data)

class EditorasViewSet(viewsets.ModelViewSet):
    queryset = Editoras.objects.all()
    serializer_class = EditorasSerializer

class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer

    @action(detail=True, methods=["get"])
    def reservas_livro(self, request, pk=None):
        livro_id = request.query_params.get("livro_id")
        reservas = self.queryset.filter(livro__id=livro_id)
        serializer = self.get_serializer(reservas, many=True)
        return Response(serializer.data)

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

    @action(detail=True, methods=["get"])
    def emprestimos_usuario(self, request, pk=None):
        usuario = self.get_object()
        emprestimos = Emprestimos.objects.filter(usuario=usuario)
        serializer = EmprestimosSerializer(emprestimos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def reservas_usuario(self, request, pk=None):
        usuario = self.get_object()
        reservas = Reservas.objects.filter(usuario=usuario)
        serializer = ReservasSerializer(reservas, many=True)
        return Response(serializer.data)

class EmprestimosViewSet(viewsets.ModelViewSet):
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimosSerializer

    @action(detail=True, methods=["get"])
    def emprestimos_livro(self, request, pk=None):
        livro_id = request.query_params.get("livro_id")
        emprestimos = self.queryset.filter(livro_id=livro_id)
        serializer = self.get_serializer(emprestimos, many=True)
        return Response(serializer.data)
