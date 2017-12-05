#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import FormView, UpdateView

from app.forms import FormRegisterUser, FormUpdateUser, FormUpdateInstitute
from app.mixins.CustomContextMixin import CustomContextMixin
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

    def str_to_bool(self, s):
        if s == 'True':
            return True
        elif s == 'False':
            return False
        else:
            raise ValueError


class UpdateUserView(LoginRequiredMixin, FormView, CustomContextMixin):
    login_url = '/login/'
    form_class = FormUpdateUser
    template_name = 'admin_panel/update_user.html'
    success_url = '/profile'

    def get_form_class(self):
        if self.request.user.institute_set.first():
            form = FormUpdateInstitute().__class__
        else:
            form = FormUpdateUser().__class__
        return form

    def get_initial(self):
        dict = {}
        dict['first_name'] = self.request.user.first_name
        dict['last_name'] = self.request.user.last_name
        dict['email'] = self.request.user.email
        if self.request.user.institute_set.first():
            dict['cep'] = self.request.user.institute_set.first().cep
            dict['address'] = self.request.user.institute_set.first().address
            dict['number'] = self.request.user.institute_set.first().number
            dict['district'] = self.request.user.institute_set.first().district
            dict['city'] = self.request.user.institute_set.first().city
            dict['state'] = self.request.user.institute_set.first().state
            dict['complement'] = self.request.user.institute_set.first().complement
            dict['cnpj'] = self.request.user.institute_set.first().cnpj
            dict['phone'] = self.request.user.institute_set.first().phone
            dict['site'] = self.request.user.institute_set.first().site
            dict['description'] = self.request.user.institute_set.first().description
            dict['social'] = self.request.user.institute_set.first().social
        else:
            dict['cep'] = self.request.user.commonuser_set.first().cep
            dict['address'] = self.request.user.commonuser_set.first().address
            dict['number'] = self.request.user.commonuser_set.first().number
            dict['district'] = self.request.user.commonuser_set.first().district
            dict['city'] = self.request.user.commonuser_set.first().city
            dict['state'] = self.request.user.commonuser_set.first().state
            dict['complement'] = self.request.user.commonuser_set.first().complement
            dict['birth_date'] = self.request.user.commonuser_set.first().birth_date
            dict['phone'] = self.request.user.commonuser_set.first().phone
            dict['anonymous'] = self.request.user.commonuser_set.first().anonymous
        return dict


    def form_valid(self, form):
        data = form.cleaned_data
        user = self.request.user
        user.first_name = data['first_name']
        user.email = data['email']
        if self.request.user.institute_set.first():
            entity = self.request.user.institute_set.first()
            entity.cnpj = data['cnpj']
            entity.phone = data['phone']
            entity.cep = data['cep']
            entity.address = data['address']
            entity.number = data['number']
            entity.state = data['state']
            entity.city = data['city']
            entity.district = data['district']
            entity.complement = data['complement']
            entity.site = data['site']
            entity.social = data['social']
            entity.save()
            user.save()
            messages.success(self.request, 'Perfil alterado com sucesso.')
        else:
            entity = self.request.user.commonuser_set.first()
            entity.cpf = data['cpf']
            entity.phone = data['phone']
            entity.cep = data['cep']
            entity.address = data['address']
            entity.number = data['number']
            entity.state = data['state']
            entity.city = data['city']
            entity.district = data['district']
            entity.complement = data['complement']
            entity.birth_date = data['birth_date']
            entity.anonymous = data['anonymous']
            entity.save()
            user.save()
            messages.success(self.request, 'Perfil alterado com sucesso.')
        return super(UpdateUserView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Não foi possível alterar perfil.')
        return super(UpdateUserView, self).form_invalid(form)
