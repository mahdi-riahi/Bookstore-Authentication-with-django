from django.views import generic
from django.contrib.auth.forms import UserCreationForm


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = 'home'
