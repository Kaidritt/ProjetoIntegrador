from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Residuo, PontoColeta
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

class PontoColetaForm(forms.ModelForm):
    class Meta:
        model = PontoColeta
        fields = ['endereco', 'latitude', 'longitude', 'tipos_residuo']  # Corrected field name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Optional: Adding a placeholder to the 'endereco' field
        self.fields['endereco'].widget.attrs.update({'placeholder': 'Digite o endereço do ponto de coleta'})
        
        # Optional: Adding a help text for latitude and longitude fields
        self.fields['latitude'].help_text = 'Digite a latitude (opcional, será preenchido automaticamente se o endereço for válido).'
        self.fields['longitude'].help_text = 'Digite a longitude (opcional, será preenchido automaticamente se o endereço for válido).'

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance