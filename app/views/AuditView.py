#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView

from app.mixins.CustomContextMixin import CustomContextMixin
from app.models import Audit, Item

__author__ = "Caio F Marinho"
__copyright__ = "Copyright 2017, LES-UFCG"


class AuditListView(LoginRequiredMixin, ListView, CustomContextMixin):
    login_url = '/login/'
    model = Audit
    context_object_name = 'audits'
    template_name = 'admin_panel/audit.html'

    def get_queryset(self):
        return Audit.objects.filter(new_owner=self.request.user).order_by('-created_at')


def order_item(request, pk):
    item = Item.objects.get(id=pk)
    qs = Audit.objects.filter(item_id=pk, new_owner=request.user, donor_id=item.owner.pk)
    if qs:
        messages.error(request, 'Você já requisitou este Item')
        return redirect('/home')
    else:
        audit = Audit(new_owner=request.user, donor=item.owner, item=item)
        audit.save()
        messages.success(request, 'Uma nova auditoria foi criada')
        return redirect('/audits')
