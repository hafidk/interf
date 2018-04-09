from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    noticies=["mor django atroplleat"]
    context={'news':noticies}
    return render(request,"home/index.html",context)

def chat(request):
    noticies=["mor django"]
    context={'news':noticies}
    return render(request,"home/chat.html",context)

def add(request):
    noticies=["mor django"]
    context={'news':noticies}
    return render(request,"home/add_fila_taula.html",context)

def comercos(request):
    noticies=["mor django"]
    context={'news':noticies}
    return render(request,"home/comercos.html",context)

def compra_venta(request):
    noticies=["mor django"]
    context={'news':noticies}
    return render(request,"home/compra_venta.html",context)

def mapa_lloc(request):
    noticies=["mor django"]
    context={'news':noticies}
    return render(request,"home/mapa_lloc.html",context)
def mercat_croat(request):
    noticies=["mor django"]
    context={'news':noticies}
    return render(request,"home/mercat_croat.html",context)

def noticies(request):
    noticies=["mor django"]
    context={'news':noticies}
    return render(request,"home/noticies.html",context)

def register(request):
    noticies=["mor django"]
    context={'news':noticies}
    return render(request,"home/register.html",context)

def singin(request):
    noticies=["mor django"]
    context={'news':noticies}
    return render(request,"home/singin.html",context)
