from django.urls import path
from . import views

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro.user"),
    path("logar/", views.logar, name="login"),
]
