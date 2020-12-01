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
    path('atualiza/<int:pk>/', views.GastoUpdateView.as_view(), name='atualiza-gasto'),
    path('apaga/<int:pk>/', views.GastoDeleteView.as_view(), name='apaga-gasto'),
    path('lista/', views.GastoListView.as_view(), name="lista-gastos"),
    path('lista-mensal/', views.GastoMonthListView.as_view(), name="lista-gastos-mensal"),
    path('lista-mensal/<int:month>/<int:year>', views.GastoListMonthView.as_view(), name="gastos-mensais"),
    path('', views.GastoListView.as_view(), name="home-gastos"),
]