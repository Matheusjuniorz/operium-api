from rest_framework import serializers
from .models import departamentos, cargos, funcionario, gerente, solitacao


class AtribuirCargoSerializer(serializers.Serializer):
    cargo_id = serializers.PrimaryKeyRelatedField(
        queryset=cargos.objects.all(), 
        source='cargo'
    ) 


class DepartamentoSerializer(serializers.ModelSerializer):
    departamento_display = serializers.CharField(source='get_departamento_display', read_only=True)
    class Meta:
        model = departamentos
        fields = ['id', 'departamento', 'departamento_display']


class CargoSerializer(serializers.ModelSerializer):
    cargo_display = serializers.CharField(source='get_cargo_display', read_only=True)
    class Meta:
        model = cargos
        fields = ['id', 'cargo', 'cargo_display']


class FuncionarioSerializer(serializers.ModelSerializer):
    cargo_nome = serializers.CharField(source='cargo.get_cargo_display', read_only=True)
    departamento_nome = serializers.CharField(source='departamento.get_departamento_display', read_only=True)
    class Meta:
        model = funcionario
        fields = [
            'id', 'nome', 'email', 'senha', 
            'cargo', 'cargo_nome', 
            'departamento', 'departamento_nome'
        ]
        extra_kwargs = {
            'senha': {'write_only': True}
        }


class GerenteSerializer(serializers.ModelSerializer):
    funcionario_nome = serializers.CharField(source='funcionario.nome', read_only=True)
    departamento_nome = serializers.CharField(source='departamento.get_departamento_display', read_only=True)
    class Meta:
        model = gerente
        fields = ['id', 'funcionario', 'funcionario_nome', 'departamento', 'departamento_nome']


class SolitacaoSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    funcionario_nome = serializers.CharField(source='funcionario.nome', read_only=True)
    gerentes_nomes = serializers.StringRelatedField(source='gerente', many=True, read_only=True)
    class Meta:
        model = solitacao
        fields = [
            'id', 'titulo', 'descrisao', 
            'status', 'status_display',
            'funcionario', 'funcionario_nome',
            'gerente', 'gerentes_nomes'
        ]
