from django.db import models
from django.contrib.auth.models import User

class Genero(models.Model):
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.genero
    
class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag
    
class Livro(models.Model):
    STATUS_CHOICES = (
        ('P', 'Para Doação'),
        ('D', 'Doação Realizada'),
        )
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ImageField(upload_to="capas_livros")
    estado = models.CharField(max_length=40)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    tags = models.ManyToManyField(Tag)
    genero = models.ForeignKey(Genero, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.titulo    