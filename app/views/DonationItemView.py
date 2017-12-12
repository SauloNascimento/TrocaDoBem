#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import UpdateView

from app.forms import FormInstituteUpdate

__author__ = "Tainah Emmanuele"
__copyright__ = "Copyright 2017, LES-UFCG"