#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from app.models import Item

__author__ = "Caio Marinho"
__copyright__ = "Copyright 2017, LES-UFCG"


class PainelView(LoginRequiredMixin, ListView):
    """
    Displays the login form.
    """
    login_url = '/login/'
    template_name = 'admin_panel/home.html'
    context_object_name = 'itens'
    model = Item
    ordering = '-created_at'
    page_kwarg = 'page'
    paginate_by = 6
    # queryset = None
