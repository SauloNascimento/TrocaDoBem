#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.forms import FormNewItemRequeriment
from app.models import Item, Object, Notification
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from app.models import Requirement, Match, Donation
from django.contrib import messages
import datetime
from app.mixins.CustomContextMixin import CustomContextMixin

__author__ = "Tainah Emmanuele"
__copyright__ = "Copyright 2018, LES-UFCG"


class NewItemRequerimentView(LoginRequiredMixin, CreateView, CustomContextMixin):
    template_name = 'new_item_requeriment_view.html'
    form_class = FormNewItemRequeriment
    success_url = '/home'

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

    def form_valid(self, form):
        data = form.cleaned_data
        item = Item.objects.get(id=self.kwargs['item_id'])
        item.name_item = data['name']
        item.description = data['description']
        object = Object.objects.get(item=item)
        object.type = data['type']
        requeriment = Requirement(name=item.name_item, type=object.type,
                                  status=True, owner=self.request.user,
                                  description=item.description)
        requeriment.save()
        match = Match(requirement=requeriment, item=item)
        match.save()
        donation = Donation(donator=item.owner, institute=requeriment.owner, item=item,
                            data=datetime.datetime.today().strftime('%Y-%m-%d'), is_completed=False)
        donation.save()
        notification = Notification(user=requeriment.owner, match=match)
        notification.save()
        notification = Notification(user=item.owner, match=match)
        notification.save()
        messages.success(self.request, "Nova Necessidade cadastrada com sucesso!")
        return super(NewItemRequerimentView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Não foi possível cadastrar.')
        return super(NewItemRequerimentView, self).form_invalid(form)
