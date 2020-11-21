# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 01:36:33 2020

@author: Gabriel Boscoli
"""

from django import forms
from gastos.models import Gasto

class GastoModel2Form(forms.ModelForm):
    data = forms.DateField(input_formats=['%d/%m/%Y'], label='Data do gasto')
    class Meta:
        # usa o model de Gasto
        model = Gasto
        # usa todos os atributos do model
        fields = '__all__'