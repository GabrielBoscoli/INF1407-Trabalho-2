<<<<<<< HEAD
=======
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.urls.base import reverse_lazy
from django.http import JsonResponse
from django.http.response import HttpResponseRedirect

def homeSec(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect(reverse_lazy('gastos:lista-gastos'))
    return render(request, "registro/homeSec.html")

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
    else:
        formulario = UserCreationForm()
    context = { 'form': formulario, }
    return render(request, 'registro/registro.html', context)

@login_required
def paginaSecreta(request):
    return render(request, 'registro/paginaSecreta.html')

def verificaUsername(request):
    username = request.GET.get("username", None)
    vazio = True
    if username:
        vazio = False
    resposta = {
        # nao pode ter iexact pq o username é case sensitive
        'existe': User.objects.filter(username=username).exists(),
        'vazio': vazio,
    }
    return JsonResponse(resposta)

def verificaEmail(request):
    email = request.GET.get("email", None)
    user = None
    existe = True
    try:
        user = User.objects.get(email__iexact=email)
    except:
        existe = False
    if user and request.user == user:
        existe = False
    vazio = True
    if email:
        vazio = False
    resposta = {'existe': existe,
                'vazio': vazio, }
    return JsonResponse(resposta)

# evita que usuários maliciosos modifiquem os dados de outro usuário
class MeuUpdateView(LoginRequiredMixin, UpdateView):
    def get(self, request, pk, *args, **kwargs):
        if request.user.id == pk:
            return super().get(request, pk, args, kwargs)
        else:
            return redirect('sec-home')
>>>>>>> 23c7312991bc1f3b7ba792e1d95e8ae1c7a3111c
