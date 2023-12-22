from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *

# Create your views here.

def front_page(request:HttpRequest) -> render:
    context:dict = {}
    return render(request, "index.html",context)

def Register_documenter(request:HttpRequest) -> render:
    form = CreateDocumenter()

    if request.method == "POST":
        form = CreateDocumenter(request.POST)
        if form.is_valid():
            form.save()

    context:dict = {"form":form}
    return render(request, "register_documenter.html",context)

def Register_explorer(request:HttpRequest) -> render:
    form = CreateExplorer()

    if request.method == "POST":
        form = CreateExplorer(request.POST)
        if form.is_valid():
            form.save()

    context:dict = {"form":form}
    return render(request, "register_explorer.html",context)

def Login_documenter(request:HttpRequest) -> render:
    context:dict = {}
    return render(request, "log_doc.html",context)

def Login_explorer(request:HttpRequest) -> render:
    context:dict = {}
    return render(request, "log_exp.html",context)