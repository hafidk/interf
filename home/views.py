from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    noticies=["mor django atroplleat"]
    context={'news':noticies}
    return render(request,"home/index.html",context)
