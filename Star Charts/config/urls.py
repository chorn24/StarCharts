"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",front_page,name="Front"),
    path("register",Register_documenter,name="REGISTER_DOCUMENTER"),
    path("login",Login_documenter,name="LOGIN_DOCUMENTER"),
    path("charts/directory",Chart_D,name="CHARTS_D"),
    path("logout",logout_user,name="LOGOUT"),
    path("view/planets", view_planets, name="VIEW_P"),
    path("view/systems", view_systems, name="VIEW_S"),
    path("add/planets", add_planets, name="ADD_P"),
    path("add/systems", add_systems, name="ADD_S"),
    path("edit/planets/<str:pk>", edit_planets, name="EDIT_P"),
    path("edit/systems/<str:pk>", edit_systems, name="EDIT_S"),
    path("delete/planets/<str:pk>", delete_planets, name="DELETE_P"),
    path("delete/systems/<str:pk>", delete_systems, name="DELETE_S"),
]
