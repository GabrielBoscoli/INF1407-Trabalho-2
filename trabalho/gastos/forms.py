# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 01:36:33 2020

@author: Gabriel Boscoli
"""

from django import forms
from gastos.models import Gasto

class GastoModel2Form(forms.ModelForm):
    data = forms.DateField(input_formats=['%d/%m/%Y'], label='Data do gasto', help_text="Data do gasto no formato <em>DD/MM/AAAA<em>")
    custo = forms.DecimalField(help_text="Entre com o custo", min_value=0.0, max_value=9999999999, decimal_places=2, max_digits=10)
    
    class Meta:
        # usa o model de Gasto
        model = Gasto
        # usa todos os atributos do model
        fields = [
            'descricao',
            'custo',
            'data',
        ]