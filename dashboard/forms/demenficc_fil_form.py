from django import forms
from dashboard.models import DemENFICCFil


class DemENFICCFilRegisterForm(forms.ModelForm):

    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': ''})
    )

    demanda_energia = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    enficc = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )


    class Meta:
        model = DemENFICCFil
        fields = ['fecha', 'demanda_energia', 'enficc']
