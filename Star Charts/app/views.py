from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.


def front_page(request: HttpRequest) -> render:
    context: dict = {}
    return render(request, "index.html", context)


def Register_documenter(request: HttpRequest) -> render:
    if request.user.is_authenticated:
        return redirect("CHARTS_D")
    else:
        form = UserCreationForm()
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Registered " + user + " as documenter")
                return redirect("LOGIN_DOCUMENTER")

        context: dict = {"form": form}
        return render(request, "register_documenter.html", context)


def Login_documenter(request: HttpRequest) -> render:
    if request.user.is_authenticated:
        return redirect("CHARTS_D")
    else:
        if request.method == "POST":
            name = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect("CHARTS_D")
            else:
                messages.info(request, "Name or Password incorrect")
                return render(request, "log_in.html")

        context: dict = {}
        return render(request, "log_in.html", context)


def logout_user(request: HttpRequest):
    logout(request)
    return redirect("LOGIN_DOCUMENTER")


@login_required(login_url="LOGIN_DOCUMENTER")
def Chart_D(request: HttpRequest) -> render:
    context: dict = {}
    return render(request, "charts.html", context)


@login_required(login_url="LOGIN_DOCUMENTER")
def view_planets(request: HttpRequest) -> render:
    planets = PlanetChart.objects.all()
    test = set()
    for P in planets:
        test.add(P)

    context: dict = {"test": test}
    return render(request, "view_planets.html", context)


@login_required(login_url="LOGIN_DOCUMENTER")
def view_systems(request: HttpRequest) -> render:
    systems = SystemChart.objects.all()
    test = set()
    for S in systems:
        test.add(S)
    context: dict = {"test":test}
    return render(request, "view_systems.html", context)


@login_required(login_url="LOGIN_DOCUMENTER")
def add_planets(request: HttpRequest) -> render:
    form = CreatePlanetForm(initial={"documented_by": request.user})
    if request.method == "POST":
        form = CreatePlanetForm(request.POST)
        form.documented_by = request.user
        print(form)
        if form.is_valid():
            print(form.documented_by)
            form.save()
            print(form.documented_by)
            return redirect("VIEW_P")

    context: dict = {"form": form}
    return render(request, "add_planets.html", context)


@login_required(login_url="LOGIN_DOCUMENTER")
def add_systems(request: HttpRequest) -> render:
    form = CreateSystemForm(initial={"documented_by": request.user})
    if request.method == "POST":
        form = CreateSystemForm(request.POST)
        form.documented_by = request.user
        if form.is_valid():
            form.save()
            return redirect("VIEW_S")
    context: dict = {"form":form}
    return render(request, "add_systems.html", context)


@login_required(login_url="LOGIN_DOCUMENTER")
def edit_planets(request: HttpRequest) -> render:
    context: dict = {}
    return render(request, "edit_planets.html", context)


@login_required(login_url="LOGIN_DOCUMENTER")
def edit_systems(request: HttpRequest) -> render:
    context: dict = {}
    return render(request, "edit_systems.html", context)
