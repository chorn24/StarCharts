from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class CreatePlanetForm(ModelForm):
    class Meta:
        model = PlanetChart
        fields = ["name", "habitat_rating", "description", "system", "documented_by"]

class CreateSystemForm(ModelForm):
    class Meta:
        model = SystemChart
        fields = ["name","planet_amount","documented_by"]
