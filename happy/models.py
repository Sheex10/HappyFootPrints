from django.db import models

# Create your models here.
Class Raza(models.Model):
    codigo = models.AutoField(primary_key = True, verbose_name='Codigo de la raza')
    nombreRaza = models.CharField(max_length=20, verbose_name='Nombre de la raza', null=True, blank=True)

Class Perro(models.Model):
    codChip = models.IntegerField(primary_key = True)
    nombrePerro = models.CharField(max_length=30)
    edadPerro = models.IntegerField()
    fotoPerro = models.ImageField(upload_to="perro")
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)