from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    livros = models.ManyToManyField('Livros', related_name='autores_livro')

    editora = models.ForeignKey('Editoras', on_delete=models.CASCADE, related_name='editora_autor')

    def __str__(self):
        return f'{self.nome}'

class Livros(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField("Data de Publicação")
    foto_capa = models.ImageField(upload_to = 'uploads/')
    quantidade = models.IntegerField("Quantidade de exemplares")

    autores = models.ManyToManyField('Autor', related_name='autores_livro')
    editora = models.ForeignKey('Editoras', on_delete=models.CASCADE, related_name='editora_livro', blank=True, null=True)
    emprestimos = models.ForeignKey('Emprestimos', on_delete=models.CASCADE, related_name='emprestimos_livro', blank=True, null=True)
    reservas = models.ForeignKey('Reservas', on_delete=models.CASCADE, related_name='reservas_livro', blank=True, null=True)

    def __str__(self):
        return f'{self.nome}'
    

    
class Editoras(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField("Ano de fundação")
    localização = models.CharField(max_length=200)

    livros = models.ForeignKey('Livros', on_delete=models.CASCADE, related_name='editora_livro')
    autores = models.ForeignKey('Autor', on_delete=models.CASCADE, related_name='editora_autor')

    def __str__(self):
        return f'{self.nome}'
    
class Reservas(models.Model):
    usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE, related_name='reservas_usuario')  
    livro = models.ForeignKey('Livros', on_delete=models.CASCADE, related_name='reservas_livro')
    
    def __str__(self):
        return f'Reserva de {self.usuario.nome} para o livro {self.livro.nome}'

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    social_midia = models.CharField(max_length=100)
    endereço = models.CharField(max_length=200)

    # emprestimos = models.ForeignKey('Emprestimos', on_delete=models.CASCADE,related_name="emprestimos_usuario" , blank=True, null=True)
    # reservas = models.ForeignKey('Reservas', on_delete=models.CASCADE,related_name="reservas_usuario" , blank=True, null=True)

    def __str__(self):
        return f'{self.nome}'

class Emprestimos(models.Model):
    usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE, related_name='emprestimos_usuario')
    livro = models.ForeignKey('Livros', on_delete=models.CASCADE, related_name='emprestimos_livro')

    def __str__(self):
        return f'{self.usuario.nome} - {self.livro.nome}'
    

    
