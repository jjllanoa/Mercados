from django import forms
from dashboard.models import PlanCortoPlazo


class PlanCortoPlazoRegisterForm(forms.ModelForm):

    planta = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': ''})
    )

    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': ''})
    )

    tipo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': ''})
    )

    asignacion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': ''})
    )


    class Meta:
        model = PlanCortoPlazo
        fields = ['planta', 'fecha', 'tipo', 'asignacion']
