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




# Create your views here.

def index(request):    
    noticies=["mor django atroplleat"]
    context={'news':noticies}
    return render(request,"home/index.html",context)


@login_required()
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
    
    if form.is_valid():
        print(form)
        username = form.cleaned_data['nom']
        password = form.cleaned_data['pwd']
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('index')
            
    return render(request,template,{'form':form})

def logout_v(request):
    logout(request)
    return redirect('index')
