from django import forms
from dashboard.models import MatrizActualDC, MatrizActualNDC


# class DemCaracRegisterForm(forms.ModelForm):

#     bloque = forms.DecimalField(
#         # label='Bloque',
#         # max_digits=3,
#         # decimal_places=0,
#         widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '1', 'id': 'demcarac-bloque-input'})
#     )

#     duracion = forms.DecimalField(
#         # label='Duración',
#         # max_digits=5,
#         # decimal_places=4,
#         widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '0.1234', 'id': 'demcarac-duracion-input'})
#     )

#     restup = forms.DecimalField(
#         # label='Restup',
#         # max_digits=5,
#         # decimal_places=4,
#         widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '0.1234', 'id': 'demcarac-restup-input'})
#     )

#     restdn = forms.DecimalField(
#         # label='Restdn',
#         # max_digits=5,
#         # decimal_places=4,
#         widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '0.1234', 'id': 'demcarac-restdn-input'})
#     )


#     class Meta:
#         model = DemCarac
#         fields = ['bloque', 'duracion', 'restup', 'restdn']


class MatrizActualDCRegisterForm(forms.ModelForm):

    tipo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Hidráulica', 'id': 'matrizactualdc-tipo-input'})
    )

    capacidad = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '0.1234', 'id': 'matrizactualdc-capacidad-input'})
    )

    conversion = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '0.1234', 'id': 'matrizactualdc-conversion-input'})
    )

    fecha = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'matrizactualdc-fecha-input'})
    )


    class Meta:
        model = MatrizActualDC
        fields = ['tipo', 'capacidad', 'conversion', 'fecha']


class MatrizActualNDCRegisterForm(forms.ModelForm):

    tipo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Hidráulica', 'id': 'matrizactualdc-tipo-input'})
    )

    capacidad = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '0.1234', 'id': 'matrizactualdc-capacidad-input'})
    )

    conversion = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '0.1234', 'id': 'matrizactualdc-conversion-input'})
    )

    fecha = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'matrizactualdc-fecha-input'})
    )


    class Meta:
        model = MatrizActualNDC
        fields = ['tipo', 'capacidad', 'conversion', 'fecha']


# class DemandaRegisterForm(forms.ModelForm):

#     fecha = forms.DateField(
#         widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'demanda-fecha-input'})
#     )

#     dia_mes = forms.IntegerField(
#         widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '31', 'id': 'demanda-dia_mes-input'})
#     )

#     demanda_energia = forms.DecimalField(
#         widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '0.1234', 'id': 'demanda-demanda_energia-input'})
#     )

#     demanda_energia_dia = forms.DecimalField(
#         required=False,
#         disabled=True,
#         widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '0.1234', 'id': 'demanda-demanda_energia_dia-input'})
#     )


#     class Meta:
#         model = Demanda
#         fields = ['fecha', 'dia_mes', 'demanda_energia', 'demanda_energia_dia']


# class PlantaRegisterForm(forms.ModelForm):

#     agente = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': 'planta-agente-input'})
#     )

#     planta = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': 'planta-agente-input'})
#     )

#     tipo = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': 'planta-agente-input'})
#     )

#     dc_ndc = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': 'planta-agente-input'})
#     )

#     clasificacion = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': 'planta-agente-input'})
#     )

#     contratos = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': 'planta-agente-input'})
#     )

#     enficc_verificada = forms.IntegerField(
#         widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
#     )

#     enficc_no_comprometida = forms.IntegerField(
#         widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '', 'id': ''})
#     )

#     fecha_inicio_vigencia_enficc = forms.DateField(
#         widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': ''})
#     )

#     fecha_fin_vigencia_enficc = forms.DateField(
#         widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': ''})
#     )

#     combustibles_declarados = forms.CharField(
#         required=False,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '', 'id': 'planta-agente-input'})
#     )


#     class Meta:
#         model = Planta
#         fields = ['agente', 'planta', 'tipo', 'dc_ndc', 'clasificacion', 'contratos', 'enficc_verificada', 'enficc_no_comprometida', 'fecha_inicio_vigencia_enficc', 'fecha_fin_vigencia_enficc', 'combustibles_declarados']
