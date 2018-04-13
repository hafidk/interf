from django.db import models

# Create your models here.


class Usuari(models.Model):
    nom=models.CharField(max_length=30)
    pwd=models.CharField(max_length=30)
    email=models.CharField(max_length=30)


class Anunci(models.Model):
    titol=models.CharField(max_length=30)
    descripcio=models.CharField(max_length=600)
    autor=models.ForeignKey(Usuari, on_delete=models.CASCADE)
    date=models.DateField()
    num_stars=models.IntegerField()

"""
class Intercanvi(models.Model):
    autor=models.CharField(Usuari, on_delete=models.CASCADE)
    date=models.DateField()
    Ncroats=models.IntegerField(max_length=50)
    PreuTotal=models.IntegerField(max_length=50)
    AcceptaMonedas=models.CharField(max_length=40)
"""
