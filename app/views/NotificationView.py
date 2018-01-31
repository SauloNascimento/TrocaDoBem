#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView

from app.mixins.CustomContextMixin import CustomContextMixin
from app.models import Audit, Notification

__author__ = "Caio F Marinho"
__copyright__ = "Copyright 2017, LES-UFCG"


class NotificationListView(LoginRequiredMixin, ListView, CustomContextMixin):
    login_url = '/login/'
    model = Notification
    context_object_name = 'notifications'
    template_name = 'admin_panel/notifications.html'

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')


def accept_notification(request, pk):
    # data = request.GET

    notification = Notification.objects.get(id=pk)
    notification.status = 'ACEITO'
    notification.is_read = True
    notification.save()
    audit = Audit(new_owner=request.user, donor=notification.match.item.owner,
                  item=notification.match.item,
                  match=notification.match)
    audit.save()
    messages.success(request, 'Uma nova auditoria foi criada')
    return redirect('/notifications')


def refuse_notification(request, pk):
    # data = request.GET
    notification = Notification.objects.get(id=pk)
    notification.status = 'RECUSADO'
    notification.is_read = True
    notification.save()
    messages.success(request, 'Notificação cancelada com sucesso')
    return redirect('/notifications')
