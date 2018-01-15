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
from django.template import RequestContext
from app.forms import FormRequirement
from app.mixins.CustomContextMixin import CustomContextMixin
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.contrib.admin import widgets
from django.shortcuts import render
from app.models import Requirement
from django.core.urlresolvers import reverse_lazy

__author__ = "Tainah Emmanuele"
__copyright__ = "Copyright 2018, LES-UFCG"

class ShowcaseRequerimentView():
    template_name = 'view_showcase_requeriments.html'

def RequirementShowCaseView(request):
    context_object_name = 'requirements'
    model = Requirement
    template_name = 'view_showcase_requeriments.html'
    requeriments = Requirement.objects.all()

    form = FormRequirement
    return render(request, 'view_showcase_requeriments.html', {'requeriments': requeriments, 'form': form})

def RequerimentDetail(request, requeriment_id):
    requeriments = Requirement.objects.get(id=requeriment_id)
    #hashtags = HashTag.objects.filter(treasure=treasure_id)
    return render(request, 'view_showcase_requeriment_details.html', {'requeriments': requeriments})

