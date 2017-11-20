from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import FormView

from app.forms import FormObjectDonation
from app.models import Item, Object

__author__ = "Joao Marcos e Saulo Samuel"
__copyright__ = "Copyright 2017, LES-UFCG"


class RegisterObjectView(FormView):
    """
    Displays the login form.
    """
    template_name = 'register-object.html'
    form_class = FormObjectDonation
    success_url = '/home'

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
        object_data['object_type'] = data['object_type']
        if data['name_item'] and data['object_type']:
            if self.request.user.commonuser_set.all()[0].anonymous:
                new_item = Item(**item_data)
            else:
                new_item = Item(owner=self.request.user, **item_data)
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