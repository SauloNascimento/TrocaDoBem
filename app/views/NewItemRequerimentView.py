#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.forms import FormRequirement
from django.shortcuts import render
from app.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from app.mixins.CustomContextMixin import CustomContextMixin
from django.views.generic import CreateView
from app.models import Requirement
from django.contrib import messages

__author__ = "Tainah Emmanuele"
__copyright__ = "Copyright 2018, LES-UFCG"


class NewItemRequerimentView(LoginRequiredMixin, CreateView, CustomContextMixin):
    template_name = 'new_item_requeriment_view.html'
    form_class = FormRequirement
    model = Requirement
    success_url = '/requirements'

    def get_initial(self):
        initial = super(NewItemRequerimentView, self).get_initial()
        try:
            item = self.object.item
        except:
            pass
        else:
            initial['name'] =item.name_item
            initial['description'] = item.description
            initial['photo'] = item.photo
        return {'owner': self.request.user}, initial

    def form_valid(self, form):
        messages.success(self.request, "Nova Necessidade cadastrada com sucesso!")
        return super(NewItemRequerimentView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Não foi possível cadastrar.')
        return super(NewItemRequerimentView, self).form_invalid(form)