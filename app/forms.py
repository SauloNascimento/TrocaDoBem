from django import forms

from app.models import Instituicao


class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        # fields = ['photo', 'cnpj', 'email', 'username', 'first_name', 'last_name', 'password']
