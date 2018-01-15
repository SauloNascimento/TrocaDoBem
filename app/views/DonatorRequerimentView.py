#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import UpdateView

from app.forms import FormDonatorUpdate
from app.mixins.CustomContextMixin import UserContextMixin

__author__ = "Tainah Emmanuele"
__copyright__ = "Copyright 2018, LES-UFCG"


class DonatorRequerimentView(LoginRequiredMixin, UpdateView, UserContextMixin):
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