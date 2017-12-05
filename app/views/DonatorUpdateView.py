#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import UpdateView

from app.forms import FormDonatorUpdate

__author__ = "João Marcos e Saulo Samuel"
__copyright__ = "Copyright 2017, LES-UFCG"


class DonatorUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = User
    form_class = FormDonatorUpdate
    template_name = 'admin_panel/edit-donator.html'
    success_url = '/home'

    def get_initial(self):
        initial = super(DonatorUpdateView, self).get_initial()
        try:
            commonuser = self.object.commonuser
        except:
            a = 10
        else:
            initial['cpf'] = commonuser.cpf
            initial['birth_date'] = commonuser.birth_date
            initial['phone'] = commonuser.phone
            initial['anonymous'] = commonuser.anonymous
            initial['cep'] = commonuser.cep
            initial['state'] = commonuser.state
            initial['city'] = commonuser.city
            initial['district'] = commonuser.district
            initial['address'] = commonuser.address
            initial['number'] = commonuser.number
            initial['complement'] = commonuser.complement
        return initial

    def form_valid(self, form):
        data = form.cleaned_data
        common_user = self.object.commonuser
        common_user.cpf = data['cpf']
        common_user.phone = data['phone']
        common_user.birth_date = data['birth_date']
        common_user.cep = data['cep']
        common_user.address = data['address']
        common_user.number = data['number']
        common_user.state = data['state']
        common_user.city = data['city']
        common_user.district = data['district']
        common_user.complement = data['complement']
        common_user.anonymous = data['anonymous']
        common_user.save()
        return super(DonatorUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(DonatorUpdateView, self).form_invalid(form)
