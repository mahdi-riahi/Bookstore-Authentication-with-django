from django.views import generic
from django.urls import reverse_lazy,reverse

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')
