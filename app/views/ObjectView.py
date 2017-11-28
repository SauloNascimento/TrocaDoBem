#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import UpdateView

from app.forms import FormObject, FormObjectView, FormItemUpdate
from app.models import Item, Object

__author__ = "Joao Marcos e Saulo Samuel"
__copyright__ = "Copyright 2017, LES-UFCG"


class RegisterObjectView(FormView):
    """
    Displays the login form.
    """
    template_name = 'admin_panel/add-object.html'
    form_class = FormObject
    success_url = '/donations'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        data = form.cleaned_data
        item_data = {}
        object_data = {}
        item_data['name_item'] = data['name_item']
        item_data['description'] = data['description']
        object_data['type'] = data['object_type']
        if data['name_item'] and data['object_type']:
            new_item = Item(owner=self.request.user, **item_data)
            new_item.save()
            new_object = Object(item=new_item, **object_data)
            new_object.save()
            messages.success(self.request, "Novo Objeto cadastrado com sucesso!")
        else:
            return self.form_invalid(self, form)
        return super(RegisterObjectView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Não foi possível cadastrar o objeto.')
        return super(RegisterObjectView, self).form_invalid(form)


class ObjectView(LoginRequiredMixin, DetailView):
    login_url = '/login'
    context_object_name = 'object'
    model = Object
    form_class = FormObjectView
    template_name = 'admin_panel/view_object.html'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'


class MyDonationsListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Item
    context_object_name = 'itens'
    template_name = 'admin_panel/my_donations.html'

    def get_queryset(self):
        return Item.objects.filter(owner=self.request.user).order_by('-created_at')


class ObjectUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Item
    form_class = FormItemUpdate
    template_name = 'admin_panel/edit_object.html'
    success_url = '/home'

    def form_valid(self, form):
        data = form.cleaned_data
        object = self.object.object_set.first()
        object.type = data['object_type']
        object.save()
        return super(ObjectUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(ObjectUpdateView, self).form_invalid(form)


def delete_object(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário precisa estar logado para esta operação")
        raise PermissionDenied("Usuário precisa estar logado para esta operação")
    else:
        item = Item.objects.get(id=pk)
        if item.owner.pk == request.user.id:
            item.delete()
            messages.success(request, "Objeto deletado com sucesso")
            return HttpResponseRedirect('/donations')
        else:
            messages.error(request, "Você não pode deletar este objeto")
            return HttpResponseRedirect('/donations')