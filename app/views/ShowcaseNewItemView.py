#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from app.models import Item

__author__ = "Tainah Emmanuele"
__copyright__ = "Copyright 2018, LES-UFCG"

class ShowcaseNewItemView():
    template_name = 'view_showcase_new_items.html'


def new_item_showcase_view(request):
    items = Item.objects.all().filter(status=True)

    return render(request, 'view_showcase_new_items.html',
                  {'items':items})


def new_item_detail(request, new_item_id):
    items  = Item.objects.all().filter(status=True).get(id=new_item_id)
    return render(request, 'view_showcase_new_item_details.html',
                  {'items': items})
