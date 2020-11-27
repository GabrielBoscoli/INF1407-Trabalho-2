from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
'''
from django.urls.base import reverse_lazy
from django.contrib.auth.models import User
'''

def homeSec(request):
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

# evita que usuários maliciosos modifiquem os dados de outro usuário
class MeuUpdateView(UpdateView):
    '''
    template_name='registro/user_form.html'
    success_url=reverse_lazy('sec-home')
    model=User
    fields=['first_name','last_name','email',]
    '''
    
    def get(self, request, pk, *args, **kwargs):
        if request.user.id == pk:
            return super().get(request, pk, args, kwargs)
        else:
            return redirect('sec-home')