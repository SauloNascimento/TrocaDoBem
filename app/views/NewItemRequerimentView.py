#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.forms import FormNewItemRequeriment
from django.shortcuts import render
from app.models import User, Item
from django.contrib.auth.mixins import LoginRequiredMixin
from app.mixins.CustomContextMixin import CustomContextMixin
from django.views.generic import CreateView
from app.models import Requirement,Match, Donation,Notification
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic.base import TemplateView

from app.mixins.CustomContextMixin import CustomContextMixin, UserContextMixin
from django.views.generic import UpdateView
__author__ = "Tainah Emmanuele"
__copyright__ = "Copyright 2018, LES-UFCG"


def search_matches(**kwargs):
    reqs = Requirement.objects.filter(status=True)
    for req in reqs:
        if req.type == kwargs['type']:
            match = Match(requirement=req, item=Item.objects.get(id=kwargs['pk_item']))
            match.save()
            notification = Notification(user=req.owner, match=match)
            notification.save()
            donation = Donation(donator=Item.objects.get(id=kwargs['pk_item']).owner, institute=req.owner, data='', is_completed=False)
            donation.save()

class NewItemRequerimentView( LoginRequiredMixin, CreateView, CustomContextMixin):
    template_name = 'new_item_requeriment_view.html'
    form_class = FormNewItemRequeriment

    def get_initial(self):
        initial = super(NewItemRequerimentView, self).get_initial()
        try:
            item = Item.objects.get(id=self.kwargs['item_id'])
        except:
            pass
        else:
            initial['name'] = item.name_item
            initial['description'] = item.description
        return initial

    def get_context_data(self, **kwargs):
       context = super(NewItemRequerimentView, self).get_context_data(**kwargs)
       context['requeriment'] = Item.objects.get(id=self.kwargs['item_id'])
       return context

    def form_valid(self, form):
        data = form.cleaned_data
        item = Item.objects.get(id=self.kwargs['item_id'])
        item.name = data['name']
        item.description = data['description']
        item.type = data['object_type']
        requeriment = Requirement(name=item.name,type=item.type,status=True,owner=self.request.user,description=item.description)
        requeriment.save()
        messages.success(self.request, "Nova Necessidade cadastrada com sucesso!")
        return super(NewItemRequerimentView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Não foi possível cadastrar.')
        return super(NewItemRequerimentView, self).form_invalid(form)
