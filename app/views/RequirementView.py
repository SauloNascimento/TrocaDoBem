#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from app.forms import FormRequirement
from app.models import Requirement

__author__ = "Caio Marinho"
__copyright__ = "Copyright 2017, LES-UFCG"


class AddRequirementView(CreateView):
    """
    Displays the login form.
    """
    login_url = '/login/'
    template_name = 'admin_panel/add-requirement.html'
    form_class = FormRequirement
    model = Requirement
    success_url = '/requirements'

    def get_initial(self):
        return {'owner': self.request.user}

    def form_valid(self, form):
        messages.success(self.request, "Nova Necessidade cadastrada com sucesso!")
        return super(AddRequirementView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Não foi possível cadastrar.')
        return super(AddRequirementView, self).form_invalid(form)


class RequirementView(LoginRequiredMixin, DetailView):
    login_url = '/login'
    context_object_name = 'object'
    model = Requirement
    form_class = FormRequirement
    template_name = 'admin_panel/view_requirement.html'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'


class RequirementListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Requirement
    context_object_name = 'requirements'
    template_name = 'admin_panel/my_requirements.html'

    def get_queryset(self):
        return Requirement.objects.filter(owner=self.request.user).order_by('-created_at')


class RequirementUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Requirement
    form_class = FormRequirement
    template_name = 'admin_panel/edit_requirement.html'
    success_url = '/requirements'

    def form_invalid(self, form):
        print(form.errors)
        return super(RequirementUpdateView, self).form_invalid(form)


def delete_requirement(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário precisa estar logado para esta operação")
        raise PermissionDenied("Usuário precisa estar logado para esta operação")
    else:
        req = Requirement.objects.get(id=pk)
        if req.owner.pk == request.user.id:
            req.delete()
            messages.success(request, "Necessidade deletada com sucesso")
            return HttpResponseRedirect('/requirements')
        else:
            messages.error(request, "Você não pode deletar este objeto")
            return HttpResponseRedirect('/requirements')
