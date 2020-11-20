from django.shortcuts import render
from gastos.models import Gasto
from django.views.generic.base import View

# Create your views here.

class GastoListView(View):
    def get(self, request, *args, **kwargs):
        gastos = Gasto.objects.all()
        context = { 'gastos': gastos, }
        return render(request, 'gastos/listaGastos.html', context)