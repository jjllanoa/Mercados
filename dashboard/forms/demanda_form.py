from django import forms
from dashboard.models import Demanda


class DemandaRegisterForm(forms.ModelForm):

    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'demanda-fecha-input'})
    )

    dia_mes = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '31', 'id': 'demanda-dia_mes-input'})
    )

    demanda_energia = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '0.1234', 'id': 'demanda-demanda_energia-input'})
    )

    demanda_energia_dia = forms.DecimalField(
        required=False,
        disabled=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '0.1234', 'id': 'demanda-demanda_energia_dia-input'})
    )


    class Meta:
        model = Demanda
        fields = ['fecha', 'dia_mes', 'demanda_energia', 'demanda_energia_dia']
