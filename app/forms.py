#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from app.models import object_type, Item, Audit, Match, Requirement


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class FormBaseAddress(BaseForm):
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
                                                               'placeholder': _('Nome'),
                                'data-parsley-required-message': "Nome nao foi preenchido"
                                                               }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'maxlength': 200,
                                                              'placeholder': _('Sobrenome'),
                                'data-parsley-required-message': "Sobrenome nao foi preenchido"
                                                              }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'required': True, 'maxlength': 150,
                                                            'placeholder': _('Email'),
                             'data-parsley-required-message': "Email nao foi preenchido",
                            'data-parsley-error-message': "Formato de email nao eh valido"
                                                            }))
    username = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'maxlength': 200,
                                                             'placeholder': 'Nome de Usuario',
                                'data-parsley-required-message': "Nome de usuario nao foi preenchido"
                                                             }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True,
                                                                 'placeholder': _('Senha'),
                               'data-parsley-required-message': "Senha nao foi preenchido"
                                                                 }))
    cpf = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'maxlength': 150,
                                                        'placeholder': _('CPF'),
                              'data-parsley-required-message': "CPF nao foi preenchido"
                                                        }))
    phone = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'maxlength': 150,
                                                          'placeholder': _('Telefone'),
                                                          }))
    birth_date = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                               'placeholder': _('Data de Nascimento'),
                                                               'maxlength': 150,
                             'data-parsley-required-message': "Data de nascimento nao foi preenchido"
                                                               }))
    anonymous = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, required=True, initial='False')

    def __init__(self, *args, **kwargs):
        super(FormRegisterUser, self).__init__(*args, **kwargs)
        self.fields['birth_date'].widget.attrs['class'] += ' datepicker'


class FormRegisterInstitute(FormBaseAddress):
    cnpj = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                         'maxlength': 200,
                                                         'placeholder': _('CNPJ'),
                                     'data-parsley-required-message': "CNPJ nao foi preenchido"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                               'maxlength': 200,
                                                               'placeholder': _('First Name'),
                                     'data-parsley-required-message': "Nome nao foi preenchido"
                                                               }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'required': True,
                                                            'maxlength': 150,
                                                            'placeholder': _('Email'),
                                           'data-parsley-required-message': "Email nao foi preenchido",
                                           'data-parsley-error-message': "Formato de email nao eh valido"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                             'maxlength': 200,
                                                             'placeholder': _('Username'),
                                           'data-parsley-required-message': "Nome de usuario "
                                                                            "nao foi preenchido"
                                                             }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True,
                                                                 'placeholder': _('Password'),
                                            'data-parsley-required-message': "Senha nao foi preenchida"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                          'maxlength': 150,
                                                          'placeholder': _('Telefone'),
                                            'data-parsley-required-message': "Telefone nao foi preenchido"}))
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
                                                             'placeholder': 'Nome de Usuario',
                                   'data-parsley-required-message': "Nome de usuario nao foi preenchido"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True,
                                                                 'placeholder': _('Senha'),
                                          'data-parsley-required-message': "Senha nao foi preenchido"}))


class FormObject(BaseForm):
    name_item = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                              'maxlength': 100,
                                                              'placeholder': _('Nome do Objeto'),
                                    'data-parsley-required-message': "Nome do item nao foi preenchido"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'required': False,
                                                                               'maxlength': 300,
                                                                               'placeholder': _(
                                                                                   'Descricao do Objeto')}))
    object_type = forms.ChoiceField(choices=object_type, required=True, label=u'Type')


class FormObjectView(BaseForm):
    name_item = forms.CharField(widget=forms.TextInput(attrs={'readonly': True,
                                                              'maxlength': 100,
                                                              'placeholder': _('Nome do Objeto'),
                                'data-parsley-required-message': "Nome do item nao foi preenchido"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'required': False,
                                                                               'maxlength': 300,
                                                                               'placeholder': _(
                                                                                   'Descricao do Objeto')}))
    object_type = forms.ChoiceField(choices=object_type, required=True, label=u'Type')


class FormItemUpdate(forms.ModelForm, BaseForm):
    name_item = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                              'maxlength': 100,
                                                              'placeholder': _('Nome do Objeto'),
                            'data-parsley-required-message': "Nome do item nao foi preenchido"}))
    object_type = forms.ChoiceField(choices=object_type, required=True, label=u'Type')
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'required': False,
                                                                               'maxlength': 300,
                                                                               'placeholder': _(
                                                                                   'Descricao do Objeto')}))

    class Meta:
        model = Item
        fields = ['name_item', 'description']


class FormRequirement(forms.ModelForm, BaseForm):
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'required': False,
                                                                               'maxlength': 300,
                                                                               'placeholder': _(
                                                                                   'Descricao do Objeto')}))
    class Meta:
        model = Requirement
        fields = ['name', 'type', 'description', 'owner']
        widgets = {'owner': forms.HiddenInput()}


class FormDonatorUpdate(forms.ModelForm, FormBaseAddress):
    cpf = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'maxlength': 150,
                                                        'placeholder': _('CPF'),
                             'data-parsley-required-message': "CPF nao foi preenchido"}))
    phone = forms.CharField(required=False,
                            widget=forms.TextInput(attrs={'required': False, 'maxlength': 150,
                                                          'placeholder': _('Telefone'),
                                                          }))
    birth_date = forms.CharField(required=False,
                                 widget=forms.TextInput(attrs={'required': True, 'placeholder': _('Data de Nascimento'),
                                                               'maxlength': 150,
                              'data-parsley-required-message': "Data de nascimento nao foi preenchido"}))
    anonymous = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, required=False, label=u'Type')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(FormDonatorUpdate, self).__init__(*args, **kwargs)
        self.fields['birth_date'].widget.attrs['class'] += ' datepicker'


class FormInstituteUpdate(forms.ModelForm, FormBaseAddress):
    cnpj = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                         'maxlength': 200,
                                                         'placeholder': _('CNPJ'),
                                                         'data-parsley-required-message': "CPF nao foi preenchido"}))
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'required': False,
                                                                          'maxlength': 150,
                                                                          'placeholder': _('Telefone')}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'maxlength': 300,
                                                                               'placeholder': _(
                                                                                   'Descricao da Instituicao'),
                                                                               'data-parsley-required-message': "Descricao nao foi preenchido"}))
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


class FormAuditView(ModelForm, BaseForm):
    class Meta:
        model = Audit
        fields = ['new_owner', 'donor', 'item', 'is_complete', 'is_deferred']


class FormMatchView(ModelForm, BaseForm):
    class Meta:
        model = Match
        fields = ['requirement', 'item', ]


class FormOrderView(ModelForm, BaseForm):
    class Meta:
        model = Requirement
        fields = ['name', 'type', 'status', 'owner', 'description', ]


class FormDonationView(ModelForm, BaseForm):
    class Meta:
        model = Item
        fields = ['owner', 'description', 'name_item', 'photo', 'status', ]


class FormChangePassword(PasswordChangeForm, BaseForm):

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2


class FormDonatorRequeriment(FormDonatorUpdate, FormObject):
    birth_date = forms.CharField(required=False,
                                 widget=forms.TextInput(attrs={'required': False,
                                                               'placeholder': _('Data de Nascimento'),
                                                               'maxlength': 150}))
    cpf = forms.CharField(required=False, widget=forms.TextInput(attrs={'required': False, 'maxlength': 150,
                                                                        'placeholder': _('CPF')}))


class FormDonatorRequerimentNewUser(FormRegisterUser, FormObject):
    password = forms.CharField(widget=forms.PasswordInput
    (attrs={'required': True,
            'placeholder': _('Password')})),
    birth_date = forms.CharField(required=False,
                                 widget=forms.TextInput(attrs={'required': False,
                                                               'placeholder': _('Data de Nascimento'),
                                                               'maxlength': 150}))
    last_name = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={'required': False,
                                                              'maxlength': 200,
                                                              'placeholder': _('Sobrenome')}))


class FormRegisterAuditor(FormBaseAddress):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'maxlength': 200,
                                                               'placeholder': _('Nome')}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                              'maxlength': 200,
                                                              'placeholder': _('Sobrenome')}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'required': True,
                                                            'maxlength': 150,
                                                            'placeholder': _('Email')}))
    username = forms.CharField(widget=forms.TextInput(attrs={'required': True,
                                                             'maxlength': 200,
                                                             'placeholder': 'Nome de Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True,
                                                                 'placeholder': _('Senha')}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'required': False,
                                                          'maxlength': 150,
                                                          'placeholder': _('Telefone')}))

    def __init__(self, *args, **kwargs):
        super(FormRegisterAuditor, self).__init__(*args, **kwargs)


class FormAuditorUpdate(forms.ModelForm, FormBaseAddress):
    phone = forms.CharField(required=False,
                            widget=forms.TextInput(attrs={'required': False, 'maxlength': 150,
                                                          'placeholder': _('Telefone')}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(FormAuditorUpdate, self).__init__(*args, **kwargs)


class FormNewItemRequeriment(FormItemUpdate, FormRequirement):
    name = forms.CharField(required=False,widget=forms.TextInput(attrs={'required': True,
                                                            'maxlength': 100,
                                                            'placeholder': _('Nome do Objeto')}))
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={'required': False,
                                                            'maxlength': 300,
                                                            'placeholder': _('Descricao do Objeto')}))
    type = forms.ChoiceField(required=False,choices=object_type,  label=u'Type')

    class Meta:
        model = Requirement
        fields = ['name', 'description', 'type']
        widgets = {'owner': forms.HiddenInput()}
