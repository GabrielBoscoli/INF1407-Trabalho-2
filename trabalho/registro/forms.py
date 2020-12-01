from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UniquEmailForm(forms.ModelForm):    
    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)
    
    def clean(self):
       email = self.cleaned_data.get('email')
       usuario = None
       try:
           usuario = User.objects.get(email__iexact=email)
       except:
           return self.cleaned_data
       if usuario and usuario != self.usuario and email:
           raise ValidationError({'email': "Email já cadastrado",}, code='invalid')
       return self.cleaned_data
    
    class Meta:
        model = User
        fields = ['email','first_name','last_name']