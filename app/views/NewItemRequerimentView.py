#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.forms import FormRequirement
from django.shortcuts import render
from app.models import User, Item
from django.contrib.auth.mixins import LoginRequiredMixin
from app.mixins.CustomContextMixin import CustomContextMixin
from django.views.generic import CreateView
from app.models import Requirement
from django.contrib import messages

from django.views.generic.base import TemplateView


__author__ = "Tainah Emmanuele"
__copyright__ = "Copyright 2018, LES-UFCG"


class NewItemRequerimentView(LoginRequiredMixin, CreateView, CustomContextMixin,TemplateView):
    template_name = 'new_item_requeriment_view.html'
    form_class = FormRequirement
    model = Requirement

    def get_initial(self):
        return {'owner': self.request.user}

    def get_context_data(self, **kwargs):
        items = Item.objects.all().filter(status=True).get(id=kwargs['item_id'])
        form = FormRequirement
        return {'items':items, 'form':form}

    def form_valid(self, form):
        messages.success(self.request, "Nova Necessidade cadastrada com sucesso!")
        return super(NewItemRequerimentView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Não foi possível cadastrar.')
        return super(NewItemRequerimentView, self).form_invalid(form)
