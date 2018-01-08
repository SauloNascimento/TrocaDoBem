#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from app.views.ObjectView import RegisterObjectView
from app.mixins.CustomContextMixin import UserContextMixin

__author__ = "Tainah Emmanuele"
__copyright__ = "Copyright 2017, LES-UFCG"

class DonationItemView (LoginRequiredMixin, UpdateView, UserContextMixin):
    login_url = '/login/'
    template_name = 'admin_panel/donation-item.html'
    success_url = '/donationitem'

    def get_initial(self):
        initial = super(DonationItemView,self).get_initial()
        try:
            commonuser = self.object.commonuser
            item = self.object.item
        except:
            pass
        else:
            initial['email'] = commonuser.email
            initial['phone'] = commonuser.phone
            initial['cep'] = commonuser.cep
            initial['district'] = commonuser.district
            initial['address'] = commonuser.address
            initial['number'] = commonuser.number
            initial['complement'] = commonuser.complement
            initial['state'] = commonuser.state
            initial['city'] = commonuser.city
        return initial

    def form_valid(self, form):
        data = form.cleaned_data
        common_user = self.object.commonuser
        common_user.phone = data['phone']
        common_user.cep = data['cep']
        common_user.address = data['address']
        common_user.number = data['number']
        common_user.district = data['district']
        common_user.complement = data['complement']
        common_user.state = data['state']
        common_user.city = data['city']
        common_user.save()
        return super(DonationItemView,self).form_valid(form)

