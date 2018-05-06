# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from AppOne import forms

# Create your views here.


def index(request):
    return render(request, 'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':                 # if someone hits the submit button and posts something back
        form = forms.FormName(request.POST)      # that request is passing by request.POST

        if form.is_valid():    # .is_valid is the boolean check for form validation
            # Do Something
            print("Validation Success!")
            print("Name: "+form.cleaned_data['name'])   # Here grabbing the data from form using the key
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])
    return render(request, 'basicapp/form_page.html', {'form': form})


