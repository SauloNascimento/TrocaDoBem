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
from app.mixins.CustomContextMixin import CustomContextMixin
from app.models import Requirement

__author__ = "Tainah Emmanuele"
__copyright__ = "Copyright 2018, LES-UFCG"

class RequirementShowCaseView(ListView, CustomContextMixin):
    context_object_name = 'requirements'
    model = Requirement
    form_class = FormRequirement
    template_name = 'view_showcase.html'


    def get_queryset(self):
        return Requirement.objects.all()