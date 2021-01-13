from django import forms
from dashboard.models import PlanCapacidadAdicionalMaxERNC


class PlanCapacidadAdicionalMaxERNCRegisterForm(forms.ModelForm):

    fecha = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    eolica = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    solar = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    pch = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    ndc_t = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )


    class Meta:
        model = PlanCapacidadAdicionalMaxERNC
        fields = ['fecha', 'eolica', 'solar', 'pch', 'ndc_t']
