from django import forms
from dashboard.models import ExistenteCxCCLP


class ExistenteCxCCLPRegisterForm(forms.ModelForm):

    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': ''})
    )

    hidraulica = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    liquidos = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    carbon = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    gas = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    glp = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    pch = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    ndc_t = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    solar = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    eolica = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    existente_cxc_clp = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )


    class Meta:
        model = ExistenteCxCCLP
        fields = ['fecha', 'hidraulica', 'liquidos', 'carbon', 'gas', 'glp', 'pch', 'ndc_t', 'solar', 'eolica', 'existente_cxc_clp']
