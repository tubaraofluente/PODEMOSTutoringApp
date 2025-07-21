from django.db import models
from django.contrib.auth.models import User

class AreaConhecimento(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Área de Conhecimento")
    
    def __str__(self):
        return self.nome

class Mentor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    areas = models.ManyToManyField(AreaConhecimento)
    biografia = models.TextField()
    disponibilidade = models.JSONField()  # Armazena horários disponíveis
    
    def __str__(self):
        return self.usuario.get_full_name()

class Mentorado(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    areas_interesse = models.ManyToManyField(AreaConhecimento)
    
    def __str__(self):
        return self.usuario.get_full_name()

class SessaoMentoria(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    mentorado = models.ForeignKey(Mentorado, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    duracao = models.PositiveIntegerField()  # em minutos
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('agendada', 'Agendada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada')
    ])
    
    def __str__(self):
        return f"Sessão {self.id} - {self.mentor} para {self.mentorado}"