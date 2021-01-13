from django import forms
from dashboard.models import DemCarac


class DemCaracRegisterForm(forms.ModelForm):

    bloque = forms.DecimalField(
        # label='Bloque',
        # max_digits=3,
        # decimal_places=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '1', 'id': 'demcarac-bloque-input'})
    )

    duracion = forms.DecimalField(
        # label='Duración',
        # max_digits=5,
        # decimal_places=4,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '0.1234', 'id': 'demcarac-duracion-input'})
    )

    restup = forms.DecimalField(
        # label='Restup',
        # max_digits=5,
        # decimal_places=4,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '0.1234', 'id': 'demcarac-restup-input'})
    )

    restdn = forms.DecimalField(
        # label='Restdn',
        # max_digits=5,
        # decimal_places=4,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '0.1234', 'id': 'demcarac-restdn-input'})
    )


    class Meta:
        model = DemCarac
        fields = ['bloque', 'duracion', 'restup', 'restdn']
