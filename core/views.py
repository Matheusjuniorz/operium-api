from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import (
    CargoSerializer,
    DepartamentoSerializer,
    FuncionarioSerializer,
    GerenteSerializer,
    SolitacaoSerializer,
    AtribuirCargoSerializer,
)
from .models import cargos, departamentos, funcionario, gerente, solitacao


class FuncionarioViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = FuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListafuncionarioViewSet(viewsets.ViewSet):
    def list(self, request, format=None):
        queryset = funcionario.objects.all()
        serializer = FuncionarioSerializer(queryset, many=True)
        return Response(serializer.data)

class CriarSolicitacaoViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = SolitacaoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FuncionaGerenteViewSet(viewsets.GenericViewSet):
    queryset = funcionario.objects.all()
    serializer_class = AtribuirCargoSerializer  
    @action(detail=True, methods=['post'], url_path='escolher-cargo')
    @transaction.atomic
    def escolher_cargo(self, request, pk=None):
        func = self.get_object()

        serializer = AtribuirCargoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        novo_cargo = serializer.validated_data['cargo']

        func.cargo = novo_cargo
        func.save()

        if novo_cargo.cargo == 'GERENTE':
            novo_gerente, criado = gerente.objects.get_or_create(
                funcionario=func,
                defaults={'departamento': func.departamento}
            )
            
            return Response(
                {
                    "mensagem": "Cargo atualizado e funcionário promovido a gerente.",
                    "gerente": GerenteSerializer(novo_gerente).data
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "mensagem": "Cargo atualizado com sucesso.",
                "funcionario": FuncionarioSerializer(func).data
            },
            status=status.HTTP_200_OK
        )

class ReceberSolicitacaoViewSet(viewsets.GenericViewSet):
    queryset = solitacao.objects.all()
    serializer_class = SolitacaoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListaViewSet(viewsets.ViewSet):
    def list(self, request, format=None):
        queryset = solitacao.objects.all()

        serializer = SolitacaoSerializer(queryset, many=True)
        return Response(serializer.data)
0