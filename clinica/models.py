from django.db import models
from django.conf import settings


class Especialidade(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    
    def __str__(self):
        return self.nome 

class Medico(models.Model):
    nome = models.CharField(max_length=200)
    crm = models.CharField(max_length=8) 
    email = models.EmailField()
    telefone = models.CharField(max_length=12)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, verbose_name="Especialidade") #relacionamento 1-n
    imagem = models.ImageField(upload_to='clinica/media', blank=True)


    def __str__(self):
        return self.nome 

    
class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    sexo = models.CharField(max_length=9)
    telefone = models.CharField(max_length=12)

    def __str__(self):
        return self.nome 

class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name="Medico") 
    data = models.DateField()
    
    Horarios = (
        ("1", "08:00 ás 09:00"),
        ("2", "09:00 ás 10:00"),
        ("3", "10:00 ás 11:00"),
        ("4", "13:00 ás 14:00"),
        ("5", "14:00 ás 15:00"),
    )
    horario = models.CharField(max_length=10, choices=Horarios)
        
    def __str__(self):
        return f'{self.medico} - {self.get_horario_display()}'

class Consulta(models.Model):
    agendas = models.ForeignKey(Agenda, on_delete=models.CASCADE, verbose_name="Consulta")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente", blank=False)
        
    def __str__(self):
        return f'{self.agendas} - {self.cliente}'