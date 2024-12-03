from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)  
    social_midia = models.URLField(blank=True)
    endereço = models.CharField(max_length=200)
    indicação = models.ForeignKey('self', blank=True , null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Servico(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)
    aberto = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.descricao}'