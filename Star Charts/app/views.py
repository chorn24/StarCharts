from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *

# Create your views here.

def front_page(request:HttpRequest) -> render:
    context:dict = {}
    return render(request, "index.html",context)









def Register_documenter(request:HttpRequest) -> render:
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Registered " + user + " as documenter")
            return redirect("LOGIN_DOCUMENTER")

    context:dict = {"form":form}
    return render(request, "register_documenter.html",context)








def Login_documenter(request:HttpRequest) -> render:
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=name,password=password)
        if user is not None:
            login(request, user)
            return redirect("CHARTS_D")
        else:
            messages.info(request, "Name or Password incorrect")
            return render(request, "log_in.html")

    context:dict = {}
    return render(request, "log_in.html",context)



def Chart_D(request:HttpRequest) -> render:
    context:dict = {}
    return render(request, "charts.html",context)

def logout_user(request:HttpRequest):
    logout(request)
    return redirect("LOGIN_DOCUMENTER")