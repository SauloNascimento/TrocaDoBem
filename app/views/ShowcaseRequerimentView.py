#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.forms import FormRequirement
from django.shortcuts import render
from app.models import Requirement

__author__ = "Tainah Emmanuele"
__copyright__ = "Copyright 2018, LES-UFCG"


class ShowcaseRequerimentView():
    template_name = 'view_showcase_requeriments.html'


def requirement_showcase_view(request):
    requeriments = Requirement.objects.all()

    form = FormRequirement
    return render(request, 'view_showcase_requeriments.html',
                  {'requeriments': requeriments, 'form': form})


def requeriment_detail(request, requeriment_id):
    requeriments = Requirement.objects.get(id=requeriment_id)
    return render(request, 'view_showcase_requeriment_details.html',
                  {'requeriments': requeriments})
