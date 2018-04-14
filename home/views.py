from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm
from .forms import LogForm
from .forms import AnunciForm
from .models import *
import datetime




# Create your views here.

def index(request):    
    noticies=["mor django atroplleat"]
    context={'news':noticies}
    return render(request,"home/index.html",context)


def chat(request):
    #aviso, aixo es un parxe de merda, pero rula
    if not (request.user.is_authenticated):
        return redirect('index')
    #fi del parxe de merda del haf
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

    if request.user.is_authenticated:#si el usuari esta online, a index te vas
        return redirect('index')
    
    template="home/register.html"
    form = UserForm(request.POST)

    if form.is_valid():
        user = form.save(commit=False)#guardem local no db
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()

        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('index')
            
    return render(request,template,{'form':form})


def signin(request):
    template="home/login.html"
    form = LogForm(request.POST)

    if request.user.is_authenticated:#si el usuari esta online, a index te vas
        return redirect('index')
    
    print("fins aqui")
    if form.is_valid():
        print("it is")
        username = form.cleaned_data['nom']
        password = form.cleaned_data['pwd']
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('home')
            
    return render(request,template,{'form':form})

def logout_v(request):
    logout(request)
    return redirect('index')



def prova(request):

    random=User(username="Marta")
    print(random)
    loadout=[1,2,4,3,2,5,3]
    context={'anuncis':loadout}
    return render(request,"home/prova.html",context)


def vista2(request):
    llista="hola"

def afegir_anunci(request):
    noticies=["mor django"]
    context={'news':noticies}

    form = AnunciForm(request.POST)
    if not(request.user.is_authenticated):
        return redirect('index')
    
    if form.is_valid():
        titol = form.cleaned_data['titol']
        descripcio = form.cleaned_data['descripcio']
        nou_anunci = Anunci(titol=titol,descripcio=descripcio,autor= request.user.username, date= datetime.datetime.now(), num_stars=0)
    

    return render(request,"home/afegir_anunci.html",context)
