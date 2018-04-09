from django.db import models

# Create your models here.


class Usuari(models.Model):
    nom=models.CharField(max_length=30)
    pwd=models.CharField(max_length=30)


class Anunci(models.Model):
    titol=models.CharField(max_length=30)
    descripcio=models.CharField(max_length=600)
    autor=models.ForeignKey(Usuari, on_delete=models.CASCADE)
    date=models.DateField()
    num_stars=models.IntegerField()
