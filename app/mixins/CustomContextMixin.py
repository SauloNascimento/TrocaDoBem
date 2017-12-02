from django.views.generic.base import ContextMixin

from app.models import Audit, Notification


class CustomContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        if 'audits' not in kwargs:
            kwargs['audits_l'] = Audit.objects.filter(new_owner=self.request.user, is_complete=False).order_by(
                '-created_at')
        if 'notifications' not in kwargs:
            kwargs['notifications_l'] = Notification.objects.filter(user=self.request.user, is_read=False).order_by(
                '-created_at')
        return kwargs
