from django import forms
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model  
from django.urls import reverse_lazy

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

class LoginView(TemplateView):
    template_name = "registration/login.html"

class ProfileView(TemplateView):
    template_name = "pages/profile.html"    
  