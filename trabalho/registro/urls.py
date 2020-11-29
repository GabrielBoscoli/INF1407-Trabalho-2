"""trabalho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from registro import views
from django.urls.conf import include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls.base import reverse_lazy
from django.contrib.auth.models import User

app_name = "registro"

urlpatterns = [
    path('', views.homeSec, name='sec-home'),
    path('gastos/', include('gastos.urls', namespace='gastos')),
    path('registro/', views.registro, name='sec-registro'),
    path('login/', LoginView.as_view(template_name='registro/login.html',), name='sec-login'),
    path('profile/', views.paginaSecreta, name='sec-paginaSecreta'),
    path('logout/',
         LogoutView.as_view(next_page=reverse_lazy('sec-home'),),
         name='sec-logout'),
    path('password_change/',
         PasswordChangeView.as_view(template_name='registro/password_change_form.html',
                                    success_url=reverse_lazy('sec-password_change_done'),),
         name='sec-password_change'),
    path('password_change_done/',
         PasswordChangeDoneView.as_view(template_name='registro/password_change_done.html',),
         name='sec-password_change_done'),
    path('terminaRegistro/<int:pk>/',
         views.MeuUpdateView.as_view(template_name='registro/user_form.html',
                            success_url=reverse_lazy('sec-home'),
                            model=User,
                            fields=['first_name','last_name','email',],),
         name='sec-completaDadosUsuario'),
    path('password_reset/',
         PasswordResetView.as_view(template_name='registro/password_reset_form.html',
                                   success_url=reverse_lazy('sec-password_reset_done'),
                                   email_template_name='registro/password_reset_email.html',
                                   subject_template_name='registro/password_reset_subject.txt',
                                   from_email='inf1407django@gmail.com',),
         name='password_reset'),
    path('password_reset_done/',
         PasswordResetDoneView.as_view(template_name='registro/password_reset_done.html',),
         name='sec-password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registro/password_reset_confirm.html',
                                          success_url=reverse_lazy('sec-password_reset_complete'),),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         PasswordResetCompleteView.as_view(template_name='registro/password_reset_complete.html'),
         name='sec-password_reset_complete'),
    path('verificaUsername', views.verificaUsername, name='sec-verificaUsername'),
]
