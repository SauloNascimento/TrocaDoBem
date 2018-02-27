#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from app.mixins.CustomContextMixin import CustomContextMixin, UserContextMixin
from django.views.generic import DetailView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect

from app.forms import FormRegisterInstitute
from app.models import InstituteSingUp, Institute

__author__ = "Saulo e Joao Marcos"
__copyright__ = "Copyright 2017, LES-UFCG"


class RegisterInstituteView(FormView):
    """
    Displays the login form.
    """
    template_name = 'registers/register-institute.html'
    form_class = FormRegisterInstitute
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
        institute_data = {}
        user_data['first_name'] = data['first_name']
        user_data['email'] = data['email']
        user_data['username'] = data['username']
        user_data['password'] = data['password']
        institute_data['cnpj'] = data['cnpj']
        institute_data['phone'] = data['phone']
        institute_data['cep'] = data['cep']
        institute_data['address'] = data['address']
        institute_data['number'] = data['number']
        institute_data['state'] = data['state']
        institute_data['city'] = data['city']
        institute_data['district'] = data['district']
        institute_data['complement'] = data['complement']
        institute_data['site'] = data['site']
        institute_data['social'] = data['social']
        if data['username'] and data['password']:
            new_institute = InstituteSingUp(**user_data, **institute_data)
            new_institute.save()
            messages.success(self.request, 'Requisicao feita com sucesso, aguarde enquanto processamos sua inscricao.')
        else:
            return self.form_invalid(form)
        return super(RegisterInstituteView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Falha na requisicao.')
        return super(RegisterInstituteView, self).form_invalid(form)


class ListInstituteSingUps(LoginRequiredMixin, ListView, CustomContextMixin, UserContextMixin):
    login_url = '/login/'
    model = InstituteSingUp
    context_object_name = 'singups'
    template_name = 'admin_panel/listinstitutesingups.html'

    def get_queryset(self):
        return InstituteSingUp.objects.all()

class SingUpView(LoginRequiredMixin, DetailView, CustomContextMixin, UserContextMixin):
    login_url = '/login'
    context_object_name = 'singup'
    model = InstituteSingUp
    template_name = 'admin_panel/view_singup.html'

def reprove_singUp(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário precisa estar logado para esta operação")
        raise PermissionDenied("Usuário precisa estar logado para esta operação")
    else:
        singup = InstituteSingUp.objects.get(id=pk)
        if request.user.auditor:
            singup.delete()
            messages.success(request, "Cadastro de instituicao negado.")
            return HttpResponseRedirect('/list-singups')
        else:
            messages.error(request, "Você não tem permissao para isso.")
            raise PermissionDenied("Você não tem permissao para isso.")

def approve_singUp(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário precisa estar logado para esta operação")
        raise PermissionDenied("Usuário precisa estar logado para esta operação")
    else:
        singup = InstituteSingUp.objects.get(id=pk)
        if request.user.auditor:
            user_data = {}
            institute_data = {}
            user_data['first_name'] = singup.first_name
            user_data['email'] = singup.email
            user_data['username'] = singup.username
            user_data['password'] = singup.password
            institute_data['cnpj'] = singup.cnpj
            institute_data['phone'] = singup.phone
            institute_data['cep'] = singup.cep
            institute_data['address'] = singup.address
            institute_data['number'] = singup.number
            institute_data['state'] = singup.state
            institute_data['city'] = singup.city
            institute_data['district'] = singup.district
            institute_data['complement'] = singup.complement
            institute_data['site'] = singup.site
            institute_data['social'] = singup.social
            new_user = User.objects.create_user(**user_data)
            new_institute = Institute(user=new_user, **institute_data)
            new_user.save()
            new_institute.save()
            singup.delete()
            messages.success(request, "Cadastro de instituicao aprovado.")
            return HttpResponseRedirect('/list-singups')
        else:
            messages.error(request, "Você não tem permissao para isso.")
            raise PermissionDenied("Você não tem permissao para isso.")