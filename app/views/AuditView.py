#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from app.forms import FormAuditView
from app.mixins.CustomContextMixin import CustomContextMixin, UserContextMixin
from app.models import Audit, Item, Requirement, Match, Step

__author__ = "Caio F Marinho"
__copyright__ = "Copyright 2017, LES-UFCG"


class AuditListView(LoginRequiredMixin, ListView, CustomContextMixin):
    login_url = '/login/'
    model = Audit
    context_object_name = 'audits'
    template_name = 'admin_panel/audit.html'

    def get_queryset(self):
        return Audit.objects.filter(new_owner=self.request.user).order_by('-created_at')


class AuditUserListView(LoginRequiredMixin, ListView, UserContextMixin):
    login_url = '/login/'
    model = Audit
    context_object_name = 'audits'
    template_name = 'admin_panel/audit-user.html'

    def get_queryset(self):
        return Audit.objects.filter(donor=self.request.user).order_by('-created_at')


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


class AuditAllListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Audit
    context_object_name = 'audits'
    template_name = 'admin_panel/audit_panel/list-audits.html'

    def get_queryset(self):
        return Audit.objects.all().order_by('-created_at')


class AuditDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login'
    context_object_name = 'object'
    model = Audit
    form_class = FormAuditView
    template_name = 'admin_panel/audit_panel/view_audit.html'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'


class AuditUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Audit
    form_class = FormAuditView
    template_name = 'admin_panel/audit_panel/edit_audit.html'
    success_url = '/audits-panel'


def delete_audit(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário precisa estar logado para esta operação")
        raise PermissionDenied("Usuário precisa estar logado para esta operação")
    else:
        audit = Audit.objects.get(id=pk)
        audit.delete()
        messages.success(request, "Objeto deletado com sucesso")
        return HttpResponseRedirect('/audits-panel')


class HomeAuditView(TemplateView):
    template_name = 'admin_panel/audit_panel/home-audit.html'

    def get_context_data(self, **kwargs):
        return {
            'itens': Item.objects.all(),
            'requirements': Requirement.objects.all(),
            'matches': Match.objects.all(),
            'audits': Audit.objects.all()
        }


def accept_audit(request, pk):
    audit = Audit.objects.get(id=pk)
    item = audit.item
    item.status = False
    item.save()
    for au in audit.item.audit_set.all():
        au.is_deferred = 'INDEFERIDO'
        au.save()
    audit.is_deferred = 'DEFERIDO'
    audit.save()
    step = Step(audit=audit, note='Doador confirmou a proposta e irá doar o item')
    step.save()
    messages.success(request, 'Proposta Confirmada!')
    return redirect('/audits-user')


def refuse_audit(request, pk):
    audit = Audit.objects.get(id=pk)
    audit.is_deferred = 'INDEFERIDO'
    audit.save()
    messages.success(request, 'Proposta foi indeferida!')
    return redirect('/notifications')


def final_delivery(request, pk):
    audit = Audit.objects.get(id=pk)
    audit.is_complete = True
    audit.save()
    req = audit.match.requirement
    req.status = False
    req.save()
    step = Step(audit=audit, note='Item foi entregue para a instituicao')
    step.save()
    messages.success(request, 'Obrigado!')
    return redirect('/audits')


def refuse_delivery(request, pk):
    audit = Audit.objects.get(id=pk)
    item = audit.item
    item.status = True
    item.save()
    audit.delete()
    messages.success(request, 'Item foi deletado com sucesso!')
    return redirect('/audits')
