#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import UpdateView

from app.forms import FormMatchView
from app.models import Match

__author__ = "Caio F Marinho"
__copyright__ = "Copyright 2017, LES-UFCG"


class MatchListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Match
    context_object_name = 'matches'
    template_name = 'admin_panel/audit_panel/list-matches.html'

    def get_queryset(self):
        return Match.objects.all().order_by('-created_at')


class MatchUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Match
    form_class = FormMatchView
    template_name = 'admin_panel/audit_panel/edit_matches.html'
    success_url = '/matches'


def delete_match(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário precisa estar logado para esta operação")
        raise PermissionDenied("Usuário precisa estar logado para esta operação")
    else:
        mat = Match.objects.get(id=pk)
        mat.delete()
        messages.success(request, "Objeto deletado com sucesso")
        return HttpResponseRedirect('/matches')
