from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from empresarios.models import Empresas


# Create your views here.
def sugestao(request):
    areas = Empresas.area_choices
    if request.method == "GET":
        return render(request, "sugestao.html", {"areas": areas})
    elif request.method == "POST":
        tipo = request.POST.get("tipo")
        area = request.POST.getlist("area")
        valor = request.POST.get("valor")

        if tipo == "C":
            empresas = Empresas.objects.filter(tempo_existencia="+5").filter(
                estagio="E"
            )
        elif tipo == "D":
            empresas = Empresas.objects.filter(
                tempo_existencia__in=["-6", "+6", "+1"]
            ).exclude(estagio="E")
        else:
            messages.add_message(
                request, constants.ERROR, "Tipo de investidor não localizado"
            )
            return redirect(f"/investidores/sugestao")
        
        empresas = empresas.filter(area__in=area)

        empresas_selecionadas = []
        for empresa in empresas:
            percentual = (float(valor) * 100) / float(empresa.valuation)
            if percentual >= 1:
                empresas_selecionadas.append(empresa)

        return render(
            request,
            "sugestao.html",
            {"empresas": empresas_selecionadas, "areas": areas},
        )
