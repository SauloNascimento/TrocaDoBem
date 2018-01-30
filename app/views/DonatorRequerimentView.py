#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.views.generic import FormView
from app.models import Item, Object, Requirement, Match, Notification, Donation
from app.forms import FormDonatorRequeriment, FormDonatorRequerimentNewUser
from app.models import CommonUser
from django.contrib import messages
from app.mixins.CustomContextMixin import UserContextMixin
from django.shortcuts import render
import datetime
from datetime import *

__author__ = "Tainah Emmanuele"
__copyright__ = "Copyright 2018, LES-UFCG"


class DonatorRequerimentView(LoginRequiredMixin, UpdateView, UserContextMixin):
    login_url = '/login/'
    model = User
    form_class = FormDonatorRequeriment
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

    def get_context_data(self, **kwargs):
       context = super(DonatorRequerimentView, self).get_context_data(**kwargs)
       context['requeriment'] = Requirement.objects.get(id=self.kwargs['requeriment_id'])
       return context

    def form_valid(self, form):
        data = form.cleaned_data
        common_user = self.object.commonuser
        common_user.cpf = data['cpf']
        common_user.phone = data['phone']
        common_user.anonymous = data['anonymous']
        common_user.save()
        requeriments = Requirement.objects.get(id=self.kwargs['requeriment_id'])
        new_item = Item(owner=self.request.user, description=requeriments.description, name_item=requeriments.name)
        new_item.save()
        new_object = Object(item=new_item, type=requeriments.type)
        new_object.save()
        messages.success(self.request, "Novo Objeto cadastrado com sucesso!")
        match = Match(requirement=requeriments, item=new_item)
        match.save()
        notification = Notification(user=requeriments.owner, match=match)
        notification.save()
        donation = Donation(donator=self.request.user,institute=requeriments.owner,item=new_item,data=new_item.created_at, is_completed=False)
        donation.save()
        messages.success(self.request, 'Muito Obrigado pela sua Doação!')
        return super(DonatorRequerimentView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(DonatorRequerimentView, self).form_invalid(form)


class DonatorRequerimentViewAnonymous(FormView):
    """
    Displays the login form.
    """
    template_name = 'donator_requeriment_view.html'
    form_class = FormDonatorRequerimentNewUser
    success_url = '/login'




    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_queryset(self):
        return Requirement.objects.get(id=self.kwargs['requeriment_id'])

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
        if data['username'] and data['password']:
            new_user = User.objects.create_user(**user_data)
            new_common_user = CommonUser(user=new_user, **common_data)
            new_common_user.save()
            messages.success(self.request, 'Novo usuário cadastrado com sucesso.')
        else:
            return self.form_invalid(form)

        requeriments = Requirement.objects.get(id=self.kwargs['requeriment_id'])
        new_item = Item(owner=new_user, description=requeriments.description, name_item=requeriments.name)
        new_item.save()
        new_object = Object(item=new_item, type=requeriments.type)
        new_object.save()
        messages.success(self.request, "Novo Objeto cadastrado com sucesso!")
        match = Match(requirement=requeriments, item=new_item)
        match.save()
        notification = Notification(user=requeriments.owner, match=match)
        notification.save()
        donation = Donation(donator=new_user,institute=requeriments.owner,item=new_item,data=new_item.created_at, is_completed=False)
        donation.save()
        messages.success(self.request, 'Muito Obrigado pela sua Doação!')
        return super(DonatorRequerimentViewAnonymous, self).form_valid(form)


    def form_invalid(self, form):
        print(form.errors)
        return super(DonatorRequerimentViewAnonymous, self).form_invalid(form)

    def get_context_data(self, **kwargs):
       context = super(DonatorRequerimentViewAnonymous, self).get_context_data(**kwargs)
       context['requeriment'] = Requirement.objects.get(id=self.kwargs['requeriment_id'])
       return context