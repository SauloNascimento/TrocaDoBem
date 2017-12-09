#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import UpdateView

from app.forms import FormOrderView
from app.models import Requirement

__author__ = "Caio F Marinho"
__copyright__ = "Copyright 2017, LES-UFCG"


class OrderListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Requirement
    context_object_name = 'orders'
    template_name = 'admin_panel/audit_panel/list-orders.html'

    def get_queryset(self):
        return Requirement.objects.all().order_by('-created_at')


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Requirement
    form_class = FormOrderView
    template_name = 'admin_panel/audit_panel/edit_order.html'
    success_url = '/orders'


def delete_order(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário precisa estar logado para esta operação")
        raise PermissionDenied("Usuário precisa estar logado para esta operação")
    else:
        mat = Requirement.objects.get(id=pk)
        mat.delete()
        messages.success(request, "Objeto deletado com sucesso")
        return HttpResponseRedirect('/orders')
