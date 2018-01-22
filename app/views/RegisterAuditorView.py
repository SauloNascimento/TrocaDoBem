#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import FormView

from app.forms import FormRegisterAuditor
from app.models import Auditor

__author__ = "JoaoMarcos"
__copyright__ = "Copyright 2017, LES-UFCG"


class RegisterAuditorView(FormView):
    """
    Displays the login form.
    """
    template_name = 'registers/register-auditor.html'
    form_class = FormRegisterAuditor
    success_url = '/login'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        data = form.cleaned_data
        aux_obj = User.objects.filter(username=data['username'])
        if len(aux_obj) > 0:
            return self.form_invalid(form)
        user_data = {}
        auditor_data = {}
        user_data['last_name'] = data['last_name']
        user_data['first_name'] = data['first_name']
        user_data['email'] = data['email']
        user_data['username'] = data['username']
        user_data['password'] = data['password']
        auditor_data['phone'] = data['phone']
        if data['username'] and data['password']:
            new_user = User.objects.create_user(**user_data)
            new_auditor = Auditor(user=new_user, **auditor_data)
            new_auditor.save()
            messages.success(self.request, 'Novo auditor cadastrado com sucesso.')
        else:
            return self.form_invalid(form)
        return super(RegisterAuditorView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Não foi possível cadastrar.')
        return super(RegisterAuditorView, self).form_invalid(form)

    def str_to_bool(self, s):
        if s == 'True':
            return True
        elif s == 'False':
            return False
        else:
            raise ValueError
