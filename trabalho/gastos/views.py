from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from gastos.models import Gasto
from gastos.forms import GastoModel2Form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Avg, Max

# Create your views here.

class GastoListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        gastos = Gasto.objects.filter(usuario=request.user)
        numero_entradas = gastos.count()
        custo_total = gastos.aggregate(Sum('custo')).get('custo__sum', None)
        custo_entrada_media = gastos.aggregate(Avg('custo')).get('custo__avg', None)
        maior_custo = gastos.aggregate(Max('custo')).get('custo__max', None)
        context = { 'gastos': gastos,
                   'numero_entradas': numero_entradas,
                   'custo_total': custo_total,
                   'custo_entrada_media': custo_entrada_media,
                   'maior_custo': maior_custo,
                   }
        return render(request, 'gastos/listaGastos.html', context)
    
class GastoCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = { 'formulario': GastoModel2Form }
        return render(request, "gastos/criaGasto.html", context)
    
    def post(self, request, *args, **kwargs):
        formulario = GastoModel2Form(request.POST)
        if formulario.is_valid():
            gasto = formulario.save()
            gasto.usuario = request.user
            gasto.save()
            return HttpResponseRedirect(reverse_lazy('gastos:lista-gastos'))
        else:
            return HttpResponseRedirect(reverse_lazy('gastos:cria-gasto'))
        
class GastoUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        gasto = Gasto.objects.get(pk=pk)
        formulario = GastoModel2Form(instance=gasto)
        context = {'gasto': formulario, }
        return render(request, 'gastos/atualizaGasto.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        gasto = get_object_or_404(Gasto, pk=pk)
        formulario = GastoModel2Form(request.POST, instance=gasto)
        if formulario.is_valid():
            gasto = formulario.save()
            gasto.save()
            return HttpResponseRedirect(reverse_lazy('gastos:lista-gastos'))
        else:
            context = { 'gasto': formulario, }
            return render(request, 'gastos/atualizaGasto.html', context)

class GastoDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        gasto = Gasto.objects.get(pk=pk)
        context = { 'gasto': gasto, }
        return render(request, 'gastos/apagaGasto.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        gasto =  Gasto.objects.get(pk=pk)
        gasto.delete()
        print("Removendo o gasto...")
        return HttpResponseRedirect(reverse_lazy('gastos:lista-gastos'))