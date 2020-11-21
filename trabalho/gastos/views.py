from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from gastos.models import Gasto
from gastos.forms import GastoModel2Form

# Create your views here.

class GastoListView(View):
    def get(self, request, *args, **kwargs):
        gastos = Gasto.objects.all()
        context = { 'gastos': gastos, }
        return render(request, 'gastos/listaGastos.html', context)
    
class GastoCreateView(View):
    def get(self, request, *args, **kwargs):
        context = { 'formulario': GastoModel2Form }
        return render(request, "gastos/criaGasto.html", context)
    
    def post(self, request, *args, **kwargs):
        formulario = GastoModel2Form(request.POST)
        if formulario.is_valid():
            gasto = formulario.save()
            gasto.save()
            return HttpResponseRedirect(reverse_lazy("gasto:lista-gastos"))
        else:
            return HttpResponseRedirect(reverse_lazy('gastos:cria-gasto'))