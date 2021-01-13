from django import forms
from dashboard.models import Planta


class PlantaRegisterForm(forms.ModelForm):

    agente = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': 'planta-agente-input'})
    )

    planta = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': 'planta-agente-input'})
    )

    tipo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': 'planta-agente-input'})
    )

    dc_ndc = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': 'planta-agente-input'})
    )

    clasificacion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': 'planta-agente-input'})
    )

    contratos = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': 'planta-agente-input'})
    )

    enficc_verificada = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    enficc_no_comprometida = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    fecha_inicio_vigencia_enficc = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': ''})
    )

    fecha_fin_vigencia_enficc = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': ''})
    )

    combustibles_declarados = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': 'planta-agente-input'})
    )


    class Meta:
        model = Planta
        fields = ['agente', 'planta', 'tipo', 'dc_ndc', 'clasificacion', 'contratos', 'enficc_verificada', 'enficc_no_comprometida', 'fecha_inicio_vigencia_enficc', 'fecha_fin_vigencia_enficc', 'combustibles_declarados']
