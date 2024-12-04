from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'

class Livros(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField("Data de Publicação")
    foto_capa = models.ImageField(upload_to = 'uploads/')
    quantidade = models.IntegerField("Quantidade de exemplares")

    author = models.ForeignKey(Autor, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.nome}'
    

    
class Editoras(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField("Ano de fundação")
    localização = models.CharField(max_length=200)

    autores = models.ManyToManyField(Autor)

    def __str__(self):
        return f'{self.nome}'
    
class Reservas(models.Model):
    usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)  
    livro = models.ForeignKey('Livros', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Reserva de {self.usuario.nome} para o livro {self.livro.nome}'

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    social_midia = models.CharField(max_length=100)
    endereço = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nome}'

class Emprestimos(models.Model):
    usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    livro = models.ForeignKey('Livros', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.usuario.nome} - {self.livro.nome}'
    

    
