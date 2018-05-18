# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
# Reverse lazy is for used to redirect user if he login or logout, it tells the user where to go.
from . import forms
from django.views.generic import CreateView

# Create your views here.


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')   # Once someone has signed up for actual website on successful signup he will
    # be redirected to login page
    template_name = 'accounts/signup.html'
