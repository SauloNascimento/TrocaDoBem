#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import UpdateView

from app.forms import FormDonationView
from app.models import Item

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
