#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from app.forms import FormDonationView, FormAnonDonation
from app.models import Item, CommonUser, Object
from app.views.ObjectView import search_matches

__author__ = "Caio F Marinho"
__copyright__ = "Copyright 2017, LES-UFCG"


class DonationListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Item
    context_object_name = 'itens'
    template_name = 'admin_panel/audit_panel/list-itens.html'

    def get_queryset(self):
        return Item.objects.all().order_by('-created_at')


class DonationUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Item
    form_class = FormDonationView
    template_name = 'admin_panel/audit_panel/edit_item.html'
    success_url = '/itens'


def delete_donation(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário precisa estar logado para esta operação")
        raise PermissionDenied("Usuário precisa estar logado para esta operação")
    else:
        mat = Item.objects.get(id=pk)
        mat.delete()
        messages.success(request, "Objeto deletado com sucesso")
        return HttpResponseRedirect('/itens')


class ChooseDonation(TemplateView):
    template_name = 'anonymous/choose_donation.html'


class AnonDonationFormView(FormView):
    template_name = 'anonymous/register-anonymous.html'
    success_url = '/'
    form_class = FormAnonDonation

    def form_valid(self, form):
        data = form.cleaned_data
        user_data = {}
        common_data = {}
        item_data = {}
        object_data = {}
        common_data['phone'] = data['phone']
        common_data['anonymous'] = True
        user_data['username'] = 'anon' + str(uuid.uuid4())
        user_data['password'] = 'anon' + str(uuid.uuid4())
        user_data['email'] = data['email']
        user = User.objects.create_user(**user_data)
        user.save()
        new_common_user = CommonUser(user=user, **common_data)
        new_common_user.save()
        item_data['name_item'] = data['name_item']
        item_data['description'] = data['description']
        object_data['type'] = data['object_type']
        new_item = Item(owner=user, **item_data)
        new_item.save()
        new_object = Object(item=new_item, **object_data)
        new_object.save()
        object_data['pk_item'] = new_item.pk
        search_matches(**object_data)
        messages.success(self.request, 'Muito Obrigado pela sua Doação!')
        return super(AnonDonationFormView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Houve algum erro!')
        return super(AnonDonationFormView, self).form_invalid(form)
