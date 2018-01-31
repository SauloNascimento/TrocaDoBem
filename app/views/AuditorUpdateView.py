#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import UpdateView

from app.forms import FormAuditorUpdate
from app.mixins.CustomContextMixin import UserContextMixin

__author__ = "Saulo Samuel"
__copyright__ = "Copyright 2018, LES-UFCG"


class AuditorUpdateView(LoginRequiredMixin, UpdateView, UserContextMixin):
    login_url = '/login/'
    model = User
    form_class = FormAuditorUpdate
    template_name = 'admin_panel/edit-auditor.html'
    success_url = '/home'

    def get_initial(self):
        initial = super(AuditorUpdateView, self).get_initial()
        try:
            auditor = self.object.auditor
        except:
            pass
        else:
            initial['phone'] = auditor.phone
            initial['cep'] = auditor.cep
            initial['state'] = auditor.state
            initial['city'] = auditor.city
            initial['district'] = auditor.district
            initial['address'] = auditor.address
            initial['number'] = auditor.number
            initial['complement'] = auditor.complement
        return initial

    def form_valid(self, form):
        data = form.cleaned_data
        auditor = self.object.auditor
        auditor.phone = data['phone']
        auditor.cep = data['cep']
        auditor.address = data['address']
        auditor.number = data['number']
        auditor.state = data['state']
        auditor.city = data['city']
        auditor.district = data['district']
        auditor.complement = data['complement']
        auditor.save()
        return super(AuditorUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(AuditorUpdateView, self).form_invalid(form)
