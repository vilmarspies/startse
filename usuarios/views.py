from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if len(password) < 6:
            messages.add_message(
                request, constants.ERROR, "A senha deve possuir pelo menos 6 digitos"
            )
            return redirect("/usuarios/cadastro")

        if not password == confirmar_senha:
            messages.add_message(request, constants.ERROR, "As senhas não são iguais")
            return redirect("/usuarios/cadastro")

        users = User.objects.filter(username=username)

        if users.exists:
            messages.add_message(
                request, constants.ERROR, "Já existe um usuário com este username"
            )
            return redirect("/usuarios/cadastro")

        user = User.objects.create_user(username, password)

        return redirect("/usuarios/logar")


def logar(request):
    if request.method == "GET":
        return render(request, "logar.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("senha")

        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect("/empresarios/cadastrar_empresa")

        messages.add_message(request, constants.ERROR, "Usuario ou senha inválidos")
        return redirect("/usuarios/logar")
