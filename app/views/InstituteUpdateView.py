#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import UpdateView

from app.forms import FormInstituteUpdate

__author__ = "João Marcos e Saulo Samuel"
__copyright__ = "Copyright 2017, LES-UFCG"


class InstituteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = User
    form_class = FormInstituteUpdate
    template_name = 'admin_panel/edit-institute.html'
    success_url = '/home'

    def get_initial(self):
        initial = super(InstituteUpdateView, self).get_initial()
        try:
            institute = self.object.institute
        except:
            pass
        else:
            initial['cnpj'] = institute.cnpj
            initial['description'] = institute.description
            initial['phone'] = institute.phone
            initial['cep'] = institute.cep
            initial['state'] = institute.state
            initial['city'] = institute.city
            initial['district'] = institute.district
            initial['address'] = institute.address
            initial['number'] = institute.number
            initial['complement'] = institute.complement
            initial['site'] = institute.site
            initial['social'] = institute.social
        return initial

    def form_valid(self, form):
        data = form.cleaned_data
        institute = self.object.institute
        institute.cpf = data['cnpj']
        institute.phone = data['phone']
        institute.description = data['description']
        institute.cep = data['cep']
        institute.address = data['address']
        institute.number = data['number']
        institute.state = data['state']
        institute.city = data['city']
        institute.district = data['district']
        institute.complement = data['complement']
        institute.site = data['site']
        institute.social = data['social']
        institute.save()
        return super(InstituteUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(InstituteUpdateView, self).form_invalid(form)
