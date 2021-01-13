from django import forms
from dashboard.models import CLP


class CLPRegisterForm(forms.ModelForm):

    representante_proyecto = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': ''})
    )

    proyecto = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': ''})
    )

    clasificacion_planta = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': ''})
    )

    oef_asignada = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    inicio_vigencia = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': ''})
    )

    fin_vigencia = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': ''})
    )

    tecnologia = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': ''})
    )

    capacidad = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
    )

    fecha_entrada = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': ''})
    )


    class Meta:
        model = CLP
        fields = ['representante_proyecto', 'proyecto', 'clasificacion_planta', 'oef_asignada', 'inicio_vigencia', 'fin_vigencia', 'tecnologia', 'capacidad', 'fecha_entrada']
