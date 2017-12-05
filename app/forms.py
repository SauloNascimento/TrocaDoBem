#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from app.models import object_type, Item, Requirement


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class FormBaseAddress(BaseForm):
    """
    Base class containing common address fields.
    """

    cep = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={
    }))
    address = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={
    }))
    number = forms.CharField(max_length=5, required=False, widget=forms.TextInput(attrs={
    }))
    state = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={
    }))
    city = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={
    }))
    district = forms.CharField(max_length=45, required=False, widget=forms.TextInput(attrs={
    }))
    complement = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={
    }))


TRUE_FALSE_CHOICES = (
    (True, 'Sim'),
    (False, 'Nao')
)


class FormRegisterUser(FormBaseAddress):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'maxlength': 200,
                                                               'placeholder': _('Nome')}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'maxlength': 200,
                                                              'placeholder': _('Sobrenome')}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'required': True, 'maxlength': 150,
                                                            'placeholder': _('Email')}))
    username = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'maxlength': 200,
                                                             'placeholder': 'Nome de Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True,
                                                                 'placeholder': _('Senha')}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'maxlength': 150,
                                                        'placeholder': _('CPF')}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'maxlength': 150,
                                                          'placeholder': _('Telefone')}))
    birth_date = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                               'placeholder': _('Data de Nascimento'),
                                                               'maxlength': 150}))
    anonymous = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, required=True, initial='False')

    def __init__(self, *args, **kwargs):
        super(FormRegisterUser, self).__init__(*args, **kwargs)
        self.fields['birth_date'].widget.attrs['class'] += ' datepicker'


class FormRegisterInstitute(FormBaseAddress):
    cnpj = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                         'maxlength': 200,
                                                         'placeholder': _('CNPJ')}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                               'maxlength': 200,
                                                               'placeholder': _('First Name')}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'required': True,
                                                            'maxlength': 150,
                                                            'placeholder': _('Email')}))
    username = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                             'maxlength': 200,
                                                             'placeholder': _('Username')}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True,
                                                                 'placeholder': _('Password')}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                          'maxlength': 150,
                                                          'placeholder': _('Telefone')}))
    site = forms.CharField(required=False, widget=forms.TextInput(attrs={'required': False,
                                                                         'maxlength': 150,
                                                                         'placeholder': _('Site')}))
    social = forms.CharField(required=False, widget=forms.TextInput(attrs={'required': False,
                                                                           'maxlength': 150,
                                                                           'placeholder': _('Rede Social')}))

    def __init__(self, *args, **kwargs):
        super(FormRegisterInstitute, self).__init__(*args, **kwargs)


class FormLogin(BaseForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                             'maxlength': 200,
                                                             'placeholder': 'Nome de Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True,
                                                                 'placeholder': _('Senha')}))


class FormObject(BaseForm):
    name_item = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                              'maxlength': 100,
                                                              'placeholder': _('Nome do Objeto')}))
    description = forms.CharField(widget=forms.Textarea(attrs={'required': False,
                                                               'maxlength': 300,
                                                               'placeholder': _('Descricao do Objeto')}))
    object_type = forms.ChoiceField(choices=object_type, required=True, label=u'Type')


class FormObjectView(BaseForm):
    name_item = forms.CharField(widget=forms.TextInput(attrs={'readonly': True,
                                                              'maxlength': 100,
                                                              'placeholder': _('Nome do Objeto')}))
    description = forms.CharField(widget=forms.Textarea(attrs={'maxlength': 300,
                                                               'placeholder': _('Descricao do Objeto')}))
    object_type = forms.ChoiceField(choices=object_type, required=True, label=u'Type')


class FormItemUpdate(forms.ModelForm, BaseForm):
    object_type = forms.ChoiceField(choices=object_type, required=True, label=u'Type')

    class Meta:
        model = Item
        fields = ['name_item', 'description']


class FormRequirement(forms.ModelForm, BaseForm):
    class Meta:
        model = Requirement
        fields = ['name', 'type', 'description', 'owner']
        widgets = {'owner': forms.HiddenInput()}


class FormDonatorUpdate(forms.ModelForm, FormBaseAddress):
    cpf = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'maxlength': 150,
                                                        'placeholder': _('CPF')}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'maxlength': 150,
                                                          'placeholder': _('Telefone')}))
    birth_date = forms.CharField(
        widget=forms.TextInput(attrs={'required': True, 'placeholder': _('Data de Nascimento'), 'maxlength': 150}))
    anonymous = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, required=True, label=u'Type')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(FormDonatorUpdate, self).__init__(*args, **kwargs)
        self.fields['birth_date'].widget.attrs['class'] += ' datepicker'


class FormInstituteUpdate(forms.ModelForm, FormBaseAddress):
    cnpj = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'maxlength': 200,
                                                         'placeholder': _('CNPJ')}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'maxlength': 150,
                                                          'placeholder': _('Telefone')}))
    description = forms.CharField(widget=forms.Textarea(attrs={'maxlength': 300,
                                                               'placeholder': _('Descricao da Instituicao')}))
    site = forms.CharField(required=False, widget=forms.TextInput(attrs={'required': False,
                                                                         'maxlength': 150,
                                                                         'placeholder': _('Site')}))
    social = forms.CharField(required=False, widget=forms.TextInput(attrs={'required': False,
                                                                           'maxlength': 150,
                                                                           'placeholder': _('Rede Social')}))
    class Meta:
        model = User
        fields = ['first_name', 'email']

    def __init__(self, *args, **kwargs):
        super(FormInstituteUpdate, self).__init__(*args, **kwargs)
