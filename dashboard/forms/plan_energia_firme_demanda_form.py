from django import forms
from dashboard.models import PlanEnergiaFirmeDemanda


class PlanEnergiaFirmeDemandaRegisterForm(forms.ModelForm):

    fecha_inicial = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    fecha_final = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    periodicidad_subasta = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )


    class Meta:
        model = PlanEnergiaFirmeDemanda
        fields = ['fecha_inicial', 'fecha_final', 'periodicidad_subasta']
