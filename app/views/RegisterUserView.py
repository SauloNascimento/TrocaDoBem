#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import FormView

from app.forms import FormRegisterUser
from app.models import CommonUser

__author__ = "Raphaeldobu"
__copyright__ = "Copyright 2017, LES-UFCG"


class RegisterUserView(FormView):
    """
    Displays the login form.
    """
    template_name = 'registers/register-user.html'
    form_class = FormRegisterUser
    success_url = '/login'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        data = form.cleaned_data
        user_data = {}
        common_data = {}
        user_data['last_name'] = data['last_name']
        user_data['first_name'] = data['first_name']
        user_data['email'] = data['email']
        user_data['username'] = data['username']
        user_data['password'] = data['password']
        common_data['cpf'] = data['cpf']
        common_data['phone'] = data['phone']
        common_data['birth_date'] = data['birth_date']
        common_data['cep'] = data['cep']
        common_data['address'] = data['address']
        common_data['number'] = data['number']
        common_data['state'] = data['state']
        common_data['city'] = data['city']
        common_data['district'] = data['district']
        common_data['complement'] = data['complement']
        if data['username'] and data['password']:
            new_user = User.objects.create_user(**user_data)
            new_common_user = CommonUser(user=new_user, **common_data)
            new_common_user.save()
            messages.success(self.request, 'Novo usuário cadastrado com sucesso.')
        else:
            return self.form_invalid(form)
        return super(RegisterUserView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Não foi possível cadastrar.')
        return super(RegisterUserView, self).form_invalid(form)
