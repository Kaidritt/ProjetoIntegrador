from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Residuo
from django.contrib.auth.models import User

class ResiduoForm(forms.ModelForm):
    class Meta:
        model = Residuo
        fields = ['tipoResiduo', 'descricao', 'diretrizes', 'imagem']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Informe um endereço de email válido.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')