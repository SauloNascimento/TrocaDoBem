#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.views import PasswordChangeView

from app.forms import FormChangePassword

__author__ = "Saulo Samuel"
__copyright__ = "Copyright 2017, LES-UFCG"


class ChangePasswordView(PasswordChangeView):
    template_name = 'admin_panel/change-password.html'
    success_url = '/home'
    form_class = FormChangePassword
