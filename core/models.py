from django.db import models

class departamentos(models.Model):
    DEPARTAMENTO = [
        ('administrativo', 'Administrativo'),
        ('financeiro', 'Financeiro'),
        ('rh', 'RH'),
        ('logistica', 'Logística'),
    ]

    departamento = models.CharField(choices=DEPARTAMENTO, max_length=20)

    def __str__(self):
        return self.get_departamento_display()


class cargos(models.Model):
    CARGO = [
        ('analista', 'Analista'),
        ('assistente', 'Assistente'),
        ('operador', 'Operador'),
    ]

    cargo = models.CharField(choices=CARGO, max_length=20)

    def __str__(self):
        return self.get_cargo_display()


class funcionario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    senha = models.CharField(max_length=128)
    cargo = models.ForeignKey(cargos, on_delete=models.CASCADE)
    departamento = models.ForeignKey(departamentos, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class gerente(models.Model):
    funcionario = models.ForeignKey(funcionario, on_delete=models.CASCADE)
    departamento = models.ForeignKey(departamentos, on_delete=models.CASCADE)

    def __str__(self):
        return self.funcionario.nome


class solitacao(models.Model):
    funcionario = models.ForeignKey(funcionario, on_delete=models.CASCADE)
    gerente = models.ManyToManyField(gerente)
    titulo = models.CharField(max_length=100)
    descrisao = models.CharField(max_length=300)
    STATUS = [
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
    ]

    status = models.CharField(choices=STATUS, max_length=20)

    def __str__(self):
        return self.titulo
