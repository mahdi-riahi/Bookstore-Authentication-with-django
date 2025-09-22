from django.views import generic

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = 'home'
