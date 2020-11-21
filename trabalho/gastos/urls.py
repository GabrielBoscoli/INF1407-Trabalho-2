# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 20:38:56 2020

@author: Gabriel Boscoli
"""

from django.urls.conf import path
from gastos import views

app_name = "gastos"

urlpatterns = [
    path('cria/',  views.GastoCreateView.as_view(), name='cria-gasto'),
    path('lista/', views.GastoListView.as_view(), name="lista-gastos"),
    path('', views.GastoListView.as_view(), name="home-gastos"),
]