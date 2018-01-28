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

from django.views.generic.base import TemplateView


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

class NewItemRequerimentView(LoginRequiredMixin, CreateView, CustomContextMixin,TemplateView):
    template_name = 'new_item_requeriment_view.html'
    form_class = FormNewItemRequeriment
    model = Requirement
    success_url = '/requirements'

    def get_initial(self):
        if self.request.method == 'GET':
            items = Item.objects.all().filter(status=True).get(id=self.kwargs['item_id'])
            return {'items':items}
        return {'owner': self.request.user}

    def form_valid(self, form):
        messages.success(self.request, "Nova Necessidade cadastrada com sucesso!")
        return super(NewItemRequerimentView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Não foi possível cadastrar.')
        return super(NewItemRequerimentView, self).form_invalid(form)
