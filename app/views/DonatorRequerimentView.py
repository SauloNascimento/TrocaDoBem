#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.views.generic import FormView
from django.views.generic import FormView

from app.forms import FormRegisterUser
from app.models import CommonUser


from app.forms import FormDonatorUpdate
from app.mixins.CustomContextMixin import UserContextMixin

__author__ = "Tainah Emmanuele"
__copyright__ = "Copyright 2018, LES-UFCG"


class DonatorRequerimentView( LoginRequiredMixin, UpdateView, UserContextMixin):
    login_url = '/login/'
    model = User
    form_class = FormDonatorUpdate
    template_name = 'donator_requeriment_view.html'
    success_url = '/home'

    def get_initial(self):
        initial = super(DonatorRequerimentView, self).get_initial()
        try:
            commonuser = self.object.commonuser
        except:
            pass
        else:
            initial['cpf'] = commonuser.cpf
            initial['phone'] = commonuser.phone
            initial['anonymous'] = commonuser.anonymous
        return initial

    def form_valid(self, form):
        data = form.cleaned_data
        common_user = self.object.commonuser
        common_user.cpf = data['cpf']
        common_user.phone = data['phone']
        common_user.anonymous = data['anonymous']
        common_user.save()
        return super(DonatorRequerimentView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(DonatorRequerimentView, self).form_invalid(form)

class DonatorRequerimentViewAnonymous(FormView):
    """
    Displays the login form.
    """
    template_name = 'donator_requeriment_view.html'
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
        aux_obj = User.objects.filter(username=data['username'])
        if len(aux_obj) > 0:
            return self.form_invalid(form)
        user_data = {}
        common_data = {}
        user_data['first_name'] = data['first_name']
        user_data['email'] = data['email']
        user_data['username'] = data['username']
        common_data['cpf'] = data['cpf']
        common_data['phone'] = data['phone']
        common_data['anonymous'] = data['anonymous']
        if data['username'] and data['password']:
            new_user = User.objects.create_user(**user_data)
            new_common_user = CommonUser(user=new_user, **common_data)
            new_common_user.save()
        else:
            return self.form_invalid(form)
        return super(DonatorRequerimentViewAnonymous, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(DonatorRequerimentViewAnonymous, self).form_invalid(form)