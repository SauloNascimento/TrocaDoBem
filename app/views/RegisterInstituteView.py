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
    success_url = '/login'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        data = form.cleaned_data
        user_data = {}
        institute_data = {}
        user_data['first_name'] = data['first_name']
        user_data['email'] = data['email']
        user_data['username'] = data['username']
        user_data['password'] = data['password']
        institute_data['cnpj'] = data['cnpj']
        institute_data['phone'] = data['phone']
        institute_data['cep'] = data['cep']
        institute_data['address'] = data['address']
        institute_data['number'] = data['number']
        institute_data['state'] = data['state']
        institute_data['city'] = data['city']
        institute_data['district'] = data['district']
        institute_data['complement'] = data['complement']
        if data['username'] and data['password']:
            new_user = User.objects.create_user(**user_data)
            new_institute = Institute(user=new_user, **institute_data)
            new_institute.save()
            messages.success(self.request, 'Nova Instituição cadastrada com sucesso.')
        else:
            return self.form_invalid(form)
        return super(RegisterInstituteView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Não foi possível cadastrar.')
        return super(RegisterInstituteView, self).form_invalid(form)
