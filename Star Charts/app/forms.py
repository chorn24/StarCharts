from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class CreateDocumenter(ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        password_repeat = forms.CharField(widget=forms.PasswordInput)
        model = Documenter
        fields = "__all__"
        
    def clean(self):
        cleaned_data = super(CreateDocumenter, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password_repeat")

        if password != confirm_password:
            self.add_error('password_repeat', "Password does not match")

        return cleaned_data
    

class CreateExplorer(ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        password_repeat = forms.CharField(widget=forms.PasswordInput)
        model = Documenter
        fields = "__all__"
        
    def clean(self):
        cleaned_data = super(CreateDocumenter, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password_repeat")

        if password != confirm_password:
            self.add_error('password_repeat', "Password does not match")

        return cleaned_data