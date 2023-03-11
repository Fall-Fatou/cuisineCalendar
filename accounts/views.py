# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm  # Setting form_class to UserCreationForm
    success_url = reverse_lazy("login")  # Setting success_url to login using reverse_lazy
    template_name = "registration/signup.html"  # Setting template_name to registration/signup.html
