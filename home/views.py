
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
    llista_tots_anuncis=Anunci.objects.all().order_by("-date")
    context={'anuncis':llista_tots_anuncis}
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
    form = LogForm(request.POST or None)

    if request.user.is_authenticated:#si el usuari esta online, a index te vas
        return redirect('index')
    print(form)
    if form.is_valid():
        
        print("it is")
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('/home/')#fucking finally

    template="home/login.html"    
    return render(request,template,{'form':form})

def logout_v(request):
    logout(request)
    return redirect('index')


def prova(request):

    llista_tots_anuncis=Anunci.objects.all().order_by("-date")
    context={'anuncis':llista_tots_anuncis}
    return render(request,"home/prova.html",context)

def afegir_anunci(request):
    noticies=["mor django"]
    form = AnunciForm(request.POST or None)
    print(form)
    if not(request.user.is_authenticated):
        return redirect('signin')
    
    if form.is_valid():
        titol = form.cleaned_data['titol']
        descripcio = form.cleaned_data['descripcio']
        nou_anunci = Anunci(titol=titol,descripcio=descripcio,autor= request.user, date= datetime.datetime.now(), num_stars=0)
        nou_anunci.save()
        return redirect('/home/')

        
    return render(request,"home/afegir_anunci.html",{"form":form})

#de moment descontinuat perque no se com enfocarlo
def missatges(request):
    if not(request.user.is_authenticated):
        return redirect('index')
    
    llista_tots_missatges=Missatge.objects.filter(reciever=request.user)
    print (llista_tots_missatges)
    context={'anuncis':"nada"}
    return render(request,"home/missatges.html",context)
