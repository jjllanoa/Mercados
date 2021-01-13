from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterForm(forms.Form):

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("El correo ya existe")
        return email


    def clean_password1(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password and password1 and password != password1:
            raise ValidationError('La contraseña no coincide')
        return password1


    email = forms.EmailField(
        label='Correo electrónico',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'correo@ejemplo.com', 'id': 'user-email-input'})
    )

    password = forms.CharField(
        label='Contraseña',
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Contraseña', 'id': 'user-password-input'})
    )

    password1 = forms.CharField(
        label='Contraseña (confirmación)',
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Contraseña', 'id': 'user-password1-input'})
    )

    options = (('True', 'Activo'),('False', 'Inactivo'),)
    is_active = forms.ChoiceField(
        label='Estado',
        choices=options,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'user-active-input'})
    )


class UserEditForm(forms.Form):

    def clean_password1(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password and password1 and password != password1:
            raise ValidationError('La contraseña no coincide')
        return password1


    email = forms.EmailField(
        label='Correo electrónico',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'correo@ejemplo.com', 'id': 'user-email-input'})
    )

    password = forms.CharField(
        label='Contraseña',
        max_length=50,
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Contraseña', 'id': 'user-password-input'})
    )

    password1 = forms.CharField(
        label='Contraseña (confirmación)',
        max_length=50,
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Contraseña', 'id': 'user-password1-input'})
    )

    options = (('True', 'Activo'),('False', 'Inactivo'),)
    is_active = forms.ChoiceField(
        label='Estado',
        choices=options,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'user-active-input'})
    )
