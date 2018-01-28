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

__author__ = "Tainah Emmanuele"
__copyright__ = "Copyright 2018, LES-UFCG"


def search_matches(**kwargs):
    reqs = Requirement.objects.filter(status=True)
    for req in reqs:
        if req.type == kwargs['type']:
            match = Match(requirement=req, item=Item.objects.get(id=kwargs['pk_item']))
            match.save()
            notification = Notification(user=req.owner, match=match)
            notification.save()

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

    def form_valid(self, form):
        data = form.cleaned_data
        common_user = self.object.commonuser
        common_user.cpf = data['cpf']
        common_user.phone = data['phone']
        common_user.anonymous = data['anonymous']
        common_user.save()
        data = form.cleaned_data
        item_data = {}
        object_data = {}
        item_data['name_item'] = data['name_item']
        item_data['description'] = data['description']
        object_data['type'] = data['object_type']
        if data['name_item'] and data['object_type']:
            new_item = Item(owner=self.request.user, **item_data)
            new_item.save()
            new_object = Object(item=new_item, **object_data)
            new_object.save()
            messages.success(self.request, "Novo Objeto cadastrado com sucesso!")
            object_data['pk_item'] = new_item.pk
            search_matches(**object_data)
        else:
            return self.form_invalid(self, form)
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

    def form_valid(self, form):
        data = form.cleaned_data
        user_data = {}
        common_data = {}
        item_data = {}
        object_data = {}
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
        item_data['name_item'] = data['name_item']
        item_data['description'] = data['description']
        object_data['type'] = data['object_type']
        if data['name_item'] and data['object_type']:
            new_item = Item(owner=new_user, **item_data)
            new_item.save()
            new_object = Object(item=new_item, **object_data)
            new_object.save()
            messages.success(self.request, "Novo Objeto cadastrado com sucesso!")
            object_data['pk_item'] = new_item.pk
            search_matches(**object_data)
        else:
            return self.form_invalid(self, form)
        messages.success(self.request, 'Muito Obrigado pela sua Doação!')
        return super(DonatorRequerimentViewAnonymous, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(DonatorRequerimentViewAnonymous, self).form_invalid(form)
