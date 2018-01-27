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
from app.views.ObjectView import search_matches

__author__ = "Tainah Emmanuele"
__copyright__ = "Copyright 2018, LES-UFCG"


class NewItemRequerimentView(LoginRequiredMixin, CreateView, CustomContextMixin,):
    template_name = 'new_item_requeriment_view.html'
    form_class = FormRequirement
    model = Requirement


    def get_initial(id_item):
        initial = super(NewItemRequerimentView, id_item).get_initial()
        try:
            item = Item.objects.all().filter(status=True).get(id_item)
        except:
            pass
        else:
            initial['name_item'] =item.name_item
            initial['description'] = item.description
            initial['photo'] = item.photo
        return  initial

    def form_valid(self, form,id_item):
        data = form.cleaned_data
        item = Item.objects.all().filter(status=True).get(id_item)
        item.name_item = data['name']
        item.description = data['description']
        item.photo = data['photo']
        messages.success(self.request, "Nova Necessidade cadastrada com sucesso!")
        return super(NewItemRequerimentView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Não foi possível cadastrar.')
        return super(NewItemRequerimentView, self).form_invalid(form)