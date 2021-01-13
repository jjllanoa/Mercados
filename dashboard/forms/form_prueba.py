from django import forms
# from dashboard.models import CLP


class PruebaRegisterForm(forms.ModelForm):

    file = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': '', 'enctype':"multipart/form-data"})
    )

    class Meta:
        # model = CLP
        fields = ['file']