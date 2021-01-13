from django import forms
from dashboard.models import ConsolidadoExistente


class ConsolidadoExistenteRegisterForm(forms.ModelForm):

    fuente_energia = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': ''})
    )

    planta = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': ''})
    )

    capacidad = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    enficc = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    tipo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': ''})
    )

    asignacion = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': ''})
    )


    class Meta:
        model = ConsolidadoExistente
        fields = ['fuente_energia', 'planta', 'capacidad', 'enficc', 'tipo', 'asignacion']
