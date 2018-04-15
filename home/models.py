from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Anunci(models.Model):
    titol=models.CharField(max_length=30)
    descripcio=models.CharField(max_length=600)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
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
