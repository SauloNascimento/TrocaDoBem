from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import FormView

from app.forms import FormRegisterInstitute
from app.models import Institute

__author__ = "Raphaeldobu"
__copyright__ = "Copyright 2017, LES-UFCG"


class RegisterInstituteView(FormView):
    """
    Displays the login form.
    """
    template_name = 'registers/register-institute.html'
    form_class = FormRegisterInstitute
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        data = form.cleaned_data
        cnpj = data['cnpj']
        password = data['password']
        first_name = data['first_name']
        email = data['email']

        if cnpj and password:
            new_user = User(username=cnpj, password=password, first_name=first_name, email=email, is_staff=True,
                            is_active=True)
            new_user.save()
            new_institute = Institute(user=new_user, cnpj=cnpj)
            new_institute.save()
            messages.success(self.request, 'Nova Instituição cadastrada com sucesso.')
        else:
            return self.form_invalid(form)
        return super(RegisterInstituteView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Não foi possível cadastrar.')
        return super(RegisterInstituteView, self).form_invalid(form)
